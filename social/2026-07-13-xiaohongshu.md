---
layout: default
title: "小红书文案｜2026-07-13"
date: 2026-07-13
---

# 小红书文案｜2026-07-13

> 用法：复制“正文”部分发布即可；标题可从下面 3 个里挑一个。

## 标题备选

1. 今天 AI/开发者圈这几件事值得看
2. 2026-07-13 科技晨报：我帮你筛出了重点
3. 别被信息流淹没：今天这几条技术动态够了

## 正文

今天帮你从技术资讯里捞了几条真正值得看的：

1）Claude Code 提示前消耗 33k 令牌，OpenCode 仅 7k
一项研究测量了处理提示前的令牌消耗，发现 Claude Code 因缓存策略和代理框架开销低效而发送 33,000 个令牌，而 OpenCode 仅发送 7,000 个。 这揭示了热门 AI 编码工具在成本和效率上的显著差距，影响开发者预算，并凸显了代理工具中令牌消耗膨胀的普遍趋势。

2）陶哲轩谈使用 AI 编码智能体构建数学可视化
著名数学家陶哲轩分享了他使用现代 AI 编码智能体移植二十多个旧 Java 小程序并创建新的复杂分析交互式可视化的经验，发现它们非常有效，仅出现一个微小 bug。 这表明 AI 编码工具使得没有深厚编程技能的领域专家也能创建定制软件，可能通过使交互式补充材料更易于制作，从而革新科学出版和教育。

3）George Hotz 谈热爱大语言模型但厌恶炒作
George Hotz 发表了一篇博文，反思大语言模型的真正实用性，同时批评过度炒作的预期，并认为前沿 AI 实验室无法捕获其创造的价值。 这一观点挑战了前沿 AI 实验室的高估值，并凸显了价值创造与价值捕获之间的脱节，这对投资者和 AI 行业的发展方向至关重要。

4）Claude Code 新增内置浏览器，实现 AI 与网页交互
Claude Code 现在内置了浏览器，使 AI 能够直接在开发环境中打开、阅读、点击和输入外部网站。写入操作会经过安全分类器筛查，以防范风险行为。 这一集成使 AI 助手更接近自主网页交互，开发者无需离开编码环境即可自动化文档查询、数据提取和测试，标志着向更强大的智能体编程工具的转变。

5）llama.cpp b9979 修复嵌入式 NUL 字节导致的静默提示截断
llama.cpp 的 b9979 版本修复了一个错误：当多模态文本输入中包含嵌入式 NUL 字节时，会导致提示被静默截断。修复方案改为显式传递文本长度，而非依赖 C 风格的空字符终止。 这确保了包含二进制数据或编码内容的提示能被正确处理，避免意外的模型输出，并增强了多模态应用的健壮性。

如果只看一条，我会先看第 1 条；如果你做开发/AI 产品，第 2、3 条也值得顺手收藏。

你今天最关注哪条？

#AI #科技资讯 #开发者 #程序员 #效率工具 #每日资讯

## 链接备查

- Claude Code 提示前消耗 33k 令牌，OpenCode 仅 7k: https://systima.ai/blog/claude-code-vs-opencode-token-overhead
- 陶哲轩谈使用 AI 编码智能体构建数学可视化: https://terrytao.wordpress.com/2026/07/11/old-and-new-apps-via-modern-coding-agents/
- George Hotz 谈热爱大语言模型但厌恶炒作: https://geohot.github.io//blog/jekyll/update/2026/07/12/i-love-llms.html
- Claude Code 新增内置浏览器，实现 AI 与网页交互: https://the-decoder.com/claude-code-now-has-a-built-in-browser-that-lets-the-ai-read-click-and-type-on-external-websites/
- llama.cpp b9979 修复嵌入式 NUL 字节导致的静默提示截断: https://github.com/ggml-org/llama.cpp/releases/tag/b9979
