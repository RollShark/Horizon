#!/usr/bin/env python3
"""Generate copy-and-paste social posts from the Chinese Horizon summary.

This script is intentionally conservative:
- it only calls Feishu/Lark webhook when explicitly asked;
- it does not publish to any platform;
- it reads the generated Chinese daily summary and writes platform-ready drafts.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import urllib.request
from dataclasses import dataclass
from pathlib import Path


SUMMARY_RE = re.compile(r"^horizon-(?P<date>\d{4}-\d{2}-\d{2})-zh\.md$")
POST_RE = re.compile(r"^(?P<date>\d{4}-\d{2}-\d{2})-summary-zh\.md$")
ITEM_HEADING_RE = re.compile(
    r"^## \[(?P<title>.+?)\]\((?P<url>.+?)\) \u2b50\ufe0f (?P<score>[\d.]+|\?)/10\s*$",
    re.MULTILINE,
)


@dataclass
class SummaryItem:
    title: str
    url: str
    score: str
    summary: str


def strip_front_matter(markdown: str) -> str:
    if markdown.startswith("---\n"):
        parts = markdown.split("---\n", 2)
        if len(parts) == 3:
            return parts[2].lstrip()
    return markdown


def clean_text(text: str) -> str:
    text = html.unescape(text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def compact(text: str, max_chars: int) -> str:
    text = clean_text(text)
    if len(text) <= max_chars:
        return text

    clipped = text[: max_chars + 1]
    for mark in "。！？；.!?;":
        pos = clipped.rfind(mark)
        if max_chars * 0.45 <= pos <= max_chars:
            return clipped[: pos + 1]
    return text[:max_chars].rstrip("，,、；;：: ") + "…"


def find_latest_summary() -> Path:
    candidates: list[tuple[str, Path]] = []

    for path in Path("data/summaries").glob("horizon-*-zh.md"):
        match = SUMMARY_RE.match(path.name)
        if match:
            candidates.append((match.group("date"), path))

    for path in Path("docs/_posts").glob("*-summary-zh.md"):
        match = POST_RE.match(path.name)
        if match:
            candidates.append((match.group("date"), path))

    if not candidates:
        raise FileNotFoundError("No Chinese summary found in data/summaries/ or docs/_posts/.")

    return sorted(candidates, key=lambda item: item[0])[-1][1]


def infer_date(summary_path: Path) -> str:
    for pattern in (SUMMARY_RE, POST_RE):
        match = pattern.match(summary_path.name)
        if match:
            return match.group("date")
    return "unknown-date"


def parse_items(markdown: str) -> list[SummaryItem]:
    markdown = strip_front_matter(markdown)
    matches = list(ITEM_HEADING_RE.finditer(markdown))
    items: list[SummaryItem] = []

    for index, match in enumerate(matches):
        body_start = match.end()
        body_end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        body = markdown[body_start:body_end]

        paragraphs = [
            clean_text(part)
            for part in re.split(r"\n\s*\n", body)
            if clean_text(part)
        ]
        summary = ""
        for paragraph in paragraphs:
            if paragraph.startswith(("reddit ·", "hackernews ·", "rss ·", "github ·")):
                continue
            if paragraph.startswith(("背景:", "社区讨论:", "标签:", "参考链接")):
                continue
            if paragraph == "---":
                continue
            summary = paragraph
            break

        items.append(
            SummaryItem(
                title=clean_text(match.group("title")),
                url=match.group("url").strip(),
                score=match.group("score").strip(),
                summary=summary,
            )
        )

    return items


def render_xiaohongshu(date: str, items: list[SummaryItem]) -> str:
    top_items = items[:5]
    title_candidates = [
        "今天 AI/开发者圈这几件事值得看",
        f"{date} 科技晨报：我帮你筛出了重点",
        "别被信息流淹没：今天这几条技术动态够了",
    ]

    lines = [
        f"# 小红书文案｜{date}",
        "",
        "> 用法：复制“正文”部分发布即可；标题可从下面 3 个里挑一个。",
        "",
        "## 标题备选",
        "",
    ]
    lines += [f"{i}. {title}" for i, title in enumerate(title_candidates, start=1)]
    lines += [
        "",
        "## 正文",
        "",
        "今天帮你从技术资讯里捞了几条真正值得看的：",
        "",
    ]

    for index, item in enumerate(top_items, start=1):
        lines += [
            f"{index}）{item.title}",
            compact(item.summary, 150),
            "",
        ]

    lines += [
        "如果只看一条，我会先看第 1 条；如果你做开发/AI 产品，第 2、3 条也值得顺手收藏。",
        "",
        "你今天最关注哪条？",
        "",
        "#AI #科技资讯 #开发者 #程序员 #效率工具 #每日资讯",
        "",
        "## 链接备查",
        "",
    ]
    lines += [f"- {item.title}: {item.url}" for item in top_items]
    lines.append("")
    return "\n".join(lines)


def render_xiaoheihe(date: str, items: list[SummaryItem]) -> str:
    top_items = items[:8]
    lines = [
        f"# 小黑盒文案｜{date}",
        "",
        "## 标题",
        "",
        f"{date} AI/开发者技术速递：{len(top_items)} 条值得关注的更新",
        "",
        "## 正文",
        "",
        f"今天从 Horizon 晨报里筛了 {len(top_items)} 条相对值得看的 AI / 开发者动态，按重要性排序：",
        "",
    ]

    for index, item in enumerate(top_items, start=1):
        lines += [
            f"{index}. {item.title}（{item.score}/10）",
            f"   - 看点：{compact(item.summary, 190)}",
            f"   - 原文：{item.url}",
            "",
        ]

    lines += [
        "整体看，今天的信息流更偏开发工具、模型生态和工程实践。如果只挑一条细看，建议优先看排在前面的高分项。",
        "",
    ]
    return "\n".join(lines)


def render_image_prompt(date: str, items: list[SummaryItem]) -> str:
    top_items = items[:8]
    topic_lines = [
        f"{index}. {item.title}（重要度 {item.score}/10）：{compact(item.summary, 130)}"
        for index, item in enumerate(top_items, start=1)
    ]

    return "\n".join(
        [
            f"# ChatGPT 生图提示词｜{date}",
            "",
            "> 用法：复制下面整段给 ChatGPT，让它基于今天晨报生成几张可用于小黑盒/小红书的配图。建议先让 ChatGPT 出 3-4 张，再挑最顺眼的一张做封面。",
            "",
            "## 可直接复制给 ChatGPT 的提示词",
            "",
            "你是一名中文科技资讯视觉设计师。请基于下面这份 AI/开发者日报内容，生成 4 张适合发布到小黑盒、小红书等文字平台的配图方案，并直接生成图片。",
            "",
            "目标：",
            "- 让读者一眼看出这是“AI / 开发者技术日报”",
            "- 画面干净、专业、有科技感，但不要像广告海报",
            "- 适合作为文章封面和正文配图",
            "- 信息不要堆太满，优先突出 3-5 个关键词/主题",
            "",
            "请生成 4 张图：",
            "1. 横版封面图，16:9，适合小黑盒文章封面。",
            "2. 竖版长图，3:4，适合小红书首图。",
            "3. 极简科技封面，留出大标题区域，适合后期加字。",
            "4. 信息卡片式配图，展示今天最重要的 5 条主题。",
            "",
            "推荐视觉风格：",
            "- 暖白或浅米色背景，橙色/蓝紫色作为点缀",
            "- 现代中文科技媒体排版，干净、有留白",
            "- 可加入抽象的芯片、代码窗口、信息流卡片、网络节点、AI 助手等元素",
            "- 避免赛博朋克过暗风格，避免廉价 3D 图标堆砌",
            "- 整体像一张高质量科技日报/开发者周报封面",
            "",
            "文字处理要求：",
            "- 如果可以稳定生成中文，请使用短标题：“AI / 开发者技术速递”",
            "- 如果中文渲染不稳定，请不要生成大段文字，只保留清晰的标题留白区域",
            "- 不要生成二维码、水印、真实人物、虚假的公司 Logo 或商标细节",
            "- 不要把原文链接画进图片里",
            "",
            "今天日报的核心内容如下：",
            *topic_lines,
            "",
            "请先整体理解主题，再生成图片。图片要适合直接搭配一篇中文技术资讯文章发布。",
            "",
        ]
    )


def with_front_matter(title: str, date: str, content: str) -> str:
    return (
        "---\n"
        "layout: default\n"
        f'title: "{title}"\n'
        f"date: {date}\n"
        "---\n\n"
        + content
    )


def render_feishu_text(
    date: str,
    xiaohongshu: str,
    xiaoheihe: str,
    image_prompt: str,
) -> str:
    lines = [
        f"📣 Horizon 平台文案｜{date}",
        "",
        "下面两段是给文字平台直接复制用的草稿，最后一段是给 ChatGPT 生图用的提示词。",
    ]

    lines += [
        "",
        "====================",
        "小红书文案",
        "====================",
        "",
        strip_front_matter(xiaohongshu).strip(),
        "",
        "====================",
        "小黑盒文案",
        "====================",
        "",
        strip_front_matter(xiaoheihe).strip(),
        "",
        "====================",
        "ChatGPT 生图提示词",
        "====================",
        "",
        strip_front_matter(image_prompt).strip(),
        "",
    ]
    return "\n".join(lines)


def send_feishu_text(text: str, webhook_url: str) -> None:
    payload = {
        "msg_type": "text",
        "content": {
            "text": text,
        },
    }
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        webhook_url,
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )

    with urllib.request.urlopen(request, timeout=30) as response:
        body = response.read().decode("utf-8", errors="replace")
        if response.status >= 400:
            raise RuntimeError(f"Feishu webhook returned HTTP {response.status}: {body}")

        try:
            result = json.loads(body)
        except json.JSONDecodeError:
            return

        if result.get("code", 0) != 0:
            raise RuntimeError(f"Feishu webhook rejected message: {body}")


def write_posts(
    summary_path: Path,
    output_dir: Path,
    *,
    send_feishu: bool = False,
) -> list[Path]:
    markdown = summary_path.read_text(encoding="utf-8")
    date = infer_date(summary_path)
    items = parse_items(markdown)

    if not items:
        raise ValueError(f"No summary items found in {summary_path}.")

    output_dir.mkdir(parents=True, exist_ok=True)
    xiaohongshu = with_front_matter(
        title=f"小红书文案｜{date}",
        date=date,
        content=render_xiaohongshu(date, items),
    )
    xiaoheihe = with_front_matter(
        title=f"小黑盒文案｜{date}",
        date=date,
        content=render_xiaoheihe(date, items),
    )
    image_prompt = with_front_matter(
        title=f"ChatGPT 生图提示词｜{date}",
        date=date,
        content=render_image_prompt(date, items),
    )

    outputs = [
        (
            output_dir / f"{date}-xiaohongshu.md",
            xiaohongshu,
        ),
        (
            output_dir / f"{date}-xiaoheihe.md",
            xiaoheihe,
        ),
        (
            output_dir / "latest-xiaohongshu.md",
            xiaohongshu,
        ),
        (
            output_dir / "latest-xiaoheihe.md",
            xiaoheihe,
        ),
        (
            output_dir / f"{date}-image-prompts.md",
            image_prompt,
        ),
        (
            output_dir / "latest-image-prompts.md",
            image_prompt,
        ),
    ]

    written: list[Path] = []
    for path, content in outputs:
        path.write_text(content, encoding="utf-8")
        written.append(path)

    if send_feishu:
        webhook_url = os.environ.get("HORIZON_WEBHOOK_URL", "").strip()
        if not webhook_url:
            raise RuntimeError("Missing HORIZON_WEBHOOK_URL for --send-feishu.")

        send_feishu_text(
            text=render_feishu_text(date, xiaohongshu, xiaoheihe, image_prompt),
            webhook_url=webhook_url,
        )

    return written


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--summary", type=Path, help="Path to a Chinese Horizon summary Markdown file.")
    parser.add_argument("--output-dir", type=Path, default=Path("docs/social"))
    parser.add_argument("--send-feishu", action="store_true", help="Send generated drafts to Feishu/Lark.")
    args = parser.parse_args()

    summary_path = args.summary or find_latest_summary()
    written = write_posts(
        summary_path,
        args.output_dir,
        send_feishu=args.send_feishu,
    )

    print(f"Generated social drafts from: {summary_path}")
    for path in written:
        print(f"  - {path}")
    if args.send_feishu:
        print("Sent social drafts to Feishu/Lark.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
