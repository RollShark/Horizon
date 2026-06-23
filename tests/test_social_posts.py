from scripts.generate_social_posts import (
    parse_items,
    render_feishu_text,
    render_image_prompt,
    render_xiaoheihe,
    render_xiaohongshu,
    write_posts,
)


SAMPLE_ZH_SUMMARY = """# Horizon 每日速递 - 2026-06-23

> 从 23 条内容中筛选出 2 条重要资讯。

---

<a id="item-1"></a>
## [Codex 日志漏洞可能导致 SSD 写入数 TB 数据](https://example.com/codex) ⭐️ 8.0/10

OpenAI Codex 存在一个日志漏洞，可能向本地 SSD 写入数 TB 数据，同时一个旋转动画会导致 GPU 使用率达到 100%。

hackernews · test · 6月23日 08:00

**背景**: 这是背景。

---

<a id="item-2"></a>
## [Cloudflare 推出临时 60 分钟账户](https://example.com/cf) ⭐️ 7.0/10

Cloudflare 现在允许任何人通过命令部署临时 Workers 项目，部署持续 60 分钟。

rss · Simon Willison · 6月23日 08:10

---
"""


def test_parse_items_from_chinese_summary():
    items = parse_items(SAMPLE_ZH_SUMMARY)

    assert len(items) == 2
    assert items[0].title == "Codex 日志漏洞可能导致 SSD 写入数 TB 数据"
    assert items[0].url == "https://example.com/codex"
    assert items[0].score == "8.0"
    assert items[0].summary.startswith("OpenAI Codex")


def test_render_social_posts():
    items = parse_items(SAMPLE_ZH_SUMMARY)

    xiaohongshu = render_xiaohongshu("2026-06-23", items)
    xiaoheihe = render_xiaoheihe("2026-06-23", items)

    assert "小红书文案｜2026-06-23" in xiaohongshu
    assert "#AI" in xiaohongshu
    assert "小黑盒文案｜2026-06-23" in xiaoheihe
    assert "原文：https://example.com/codex" in xiaoheihe


def test_render_feishu_text_strips_page_front_matter():
    items = parse_items(SAMPLE_ZH_SUMMARY)
    xiaohongshu = render_xiaohongshu("2026-06-23", items)
    xiaoheihe = render_xiaoheihe("2026-06-23", items)
    image_prompt = render_image_prompt("2026-06-23", items)

    text = render_feishu_text("2026-06-23", xiaohongshu, xiaoheihe, image_prompt)

    assert "Horizon 平台文案｜2026-06-23" in text
    assert "小红书文案" in text
    assert "小黑盒文案" in text
    assert "ChatGPT 生图提示词" in text
    assert "横版封面图，16:9" in text
    assert "layout: default" not in text


def test_render_image_prompt_mentions_daily_topics():
    items = parse_items(SAMPLE_ZH_SUMMARY)
    prompt = render_image_prompt("2026-06-23", items)

    assert "请生成 4 张图" in prompt
    assert "Codex 日志漏洞可能导致 SSD 写入数 TB 数据" in prompt
    assert "Cloudflare 推出临时 60 分钟账户" in prompt
    assert "不要生成二维码、水印、真实人物" in prompt


def test_write_posts_outputs_image_prompt_drafts(tmp_path):
    summary_path = tmp_path / "horizon-2026-06-23-zh.md"
    output_dir = tmp_path / "social"
    summary_path.write_text(SAMPLE_ZH_SUMMARY, encoding="utf-8")

    written = write_posts(summary_path, output_dir)

    assert output_dir / "2026-06-23-image-prompts.md" in written
    assert output_dir / "latest-image-prompts.md" in written
    assert not list(output_dir.glob("*.png"))
    assert "ChatGPT 生图提示词" in (output_dir / "latest-image-prompts.md").read_text(encoding="utf-8")
