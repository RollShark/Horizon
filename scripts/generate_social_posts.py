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


def with_front_matter(title: str, date: str, content: str) -> str:
    return (
        "---\n"
        "layout: default\n"
        f'title: "{title}"\n'
        f"date: {date}\n"
        "---\n\n"
        + content
    )


def render_feishu_text(date: str, xiaohongshu: str, xiaoheihe: str) -> str:
    return "\n".join(
        [
            f"📣 Horizon 平台文案｜{date}",
            "",
            "下面两段是给文字平台直接复制用的草稿。",
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
        ]
    )


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


def write_posts(summary_path: Path, output_dir: Path, *, send_feishu: bool = False) -> list[Path]:
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
            text=render_feishu_text(date, xiaohongshu, xiaoheihe),
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
    written = write_posts(summary_path, args.output_dir, send_feishu=args.send_feishu)

    print(f"Generated social drafts from: {summary_path}")
    for path in written:
        print(f"  - {path}")
    if args.send_feishu:
        print("Sent social drafts to Feishu/Lark.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
