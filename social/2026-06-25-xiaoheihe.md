---
layout: default
title: "小黑盒文案｜2026-06-25"
date: 2026-06-25
---

# 小黑盒文案｜2026-06-25

## 标题

2026-06-25 AI/开发者技术速递：8 条值得关注的更新

## 正文

今天从 Horizon 晨报里筛了 8 条相对值得看的 AI / 开发者动态，按重要性排序：

1. OpenAI 与 Broadcom 推出首款定制 AI 推理芯片 Jalapeño（9.0/10）
   - 看点：OpenAI 与 Broadcom 合作推出了首款定制 AI 芯片 Jalapeño，专为大语言模型推理设计，旨在提升效率并减少对通用 GPU 的依赖。 此举标志着 AI 推理向专用硬件的重大转变，有望降低运营成本、更高效地扩展 ChatGPT 等 AI 服务，并挑战 Nvidia 在 GPU 领域的主导地位。
   - 原文：https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/

2. Gemini 3.5 Flash 获得自主计算机使用能力（9.0/10）
   - 看点：谷歌 DeepMind 在 Gemini 3.5 Flash 中引入了计算机使用功能，使模型能够通过解读屏幕截图并生成鼠标和键盘操作，自主与桌面应用进行交互。 这标志着向实用化 AI 智能体迈出的重要一步，此类智能体能够在数字环境中执行复杂的多步骤任务，有望改变自动化、无障碍访问和用户工作流程。
   - 原文：https://deepmind.google/blog/introducing-computer-use-in-gemini-3-5-flash/

3. 高通以 40 亿美元收购 Mojo 语言开发商 Modular（8.0/10）
   - 看点：高通宣布以 40 亿美元收购 AI 初创公司 Modular，该公司由 Chris Lattner 领导，并开发了 Mojo 编程语言。这笔交易标志着高通在 AI 软件与硬件集成方面迈出的战略一步。 此次收购可能强化高通的 AI 软件栈，使其芯片能更高效地运行 AI 工作负载，从而在 AI 基础设施市场加剧竞争。同时，这也引发了对 Mojo 语言未来开源发展的担忧。
   - 原文：https://www.reuters.com/business/qualcomm-buy-ai-startup-modular-2026-06-24/

4. Bunny.net 免费提供最多 500 域名的 DNS 服务（8.0/10）
   - 看点：Bunny.net 已全面取消 DNS 查询费用，现在为每个账户提供最多 500 个域名的免费 DNS 托管，无查询次数限制，也无隐藏的企业功能。 此举使 Bunny.net 成为 Cloudflare 的高性价比欧盟替代方案，加剧了 CDN/DNS 市场竞争，并吸引追求数据主权的用户。
   - 原文：https://bunny.net/blog/were-making-bunny-dns-free/

5. NVIDIA 45°C 液冷设计使数据中心用水量趋近于零（8.0/10）
   - 看点：NVIDIA 推出了一种直触芯片液冷设计，其冷却液工作温度为 45°C，无需传统冷水机，从而使数据中心实现近乎零的用水量。 这一创新大幅降低了 AI 数据中心的环境影响，应对日益严重的水资源短缺和能耗问题。它可能为可持续的高性能计算基础设施树立新标准。 通过使用 45°C 冷却液，该设计省去了能耗巨大的冷水机，但全液冷架构可能需要新的维护流程，部件更换可能更复杂。
   - 原文：https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/

6. 约翰·卡马克反思 id Software 早期领导错误（8.0/10）
   - 看点：约翰·卡马克发布了一条推特长文，承认他在 id Software 早期的领导错误，包括以不可持续的强度推动团队，引发了深入的行业讨论。 这一反思来自游戏开发领域的先驱人物，凸显了技术创新中常被忽视的人力成本，并引发了关于领导力与可持续工作文化的重要对话。
   - 原文：https://twitter.com/ID_AA_Carmack/status/2069799283369345247

7. Show HN: Nub – 类似 Bun 的 Node.js 一体化工具包（8.0/10）
   - 看点：Nub 通过为原生 Node 添加转译器和模块钩子，提供类似 Bun 的 Node.js 开发体验，由 Zod 作者 Colin McDonnell 创建。
   - 原文：https://github.com/nubjs/nub

8. Rust 项目着手解除 crates.io 对 GitHub 的依赖（8.0/10）
   - 看点：Rust 项目已合并一项 RFC，旨在解除向 crates.io 发布 crate 时对 GitHub 的依赖，并已开始实施，但进展取决于志愿者工作和资金支持。 这降低了供应链风险和单点故障，使 Rust 生态系统更加健壮和去中心化，符合软件供应链安全的行业趋势。 该 RFC（rust-lang/rfcs#3963）制定了允许无 GitHub 仓库发布 crate 的计划。
   - 原文：https://infosec.exchange/@mttaggart/116806641273303255

整体看，今天的信息流更偏开发工具、模型生态和工程实践。如果只挑一条细看，建议优先看排在前面的高分项。
