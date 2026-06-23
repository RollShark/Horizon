from scripts.generate_social_posts import (
    parse_items,
    render_xiaoheihe,
    render_xiaohongshu,
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
