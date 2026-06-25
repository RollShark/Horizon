---
layout: default
title: "Horizon Summary: 2026-06-25 (ZH)"
date: 2026-06-25
lang: zh
---

> 从 59 条内容中筛选出 10 条重要资讯。

---

1. [OpenAI 与 Broadcom 推出首款定制 AI 推理芯片 Jalapeño](#item-1) ⭐️ 9.0/10
2. [Gemini 3.5 Flash 获得自主计算机使用能力](#item-2) ⭐️ 9.0/10
3. [高通以 40 亿美元收购 Mojo 语言开发商 Modular](#item-3) ⭐️ 8.0/10
4. [Bunny.net 免费提供最多 500 域名的 DNS 服务](#item-4) ⭐️ 8.0/10
5. [NVIDIA 45°C 液冷设计使数据中心用水量趋近于零](#item-5) ⭐️ 8.0/10
6. [约翰·卡马克反思 id Software 早期领导错误](#item-6) ⭐️ 8.0/10
7. [Show HN: Nub – 类似 Bun 的 Node.js 一体化工具包](#item-7) ⭐️ 8.0/10
8. [Rust 项目着手解除 crates.io 对 GitHub 的依赖](#item-8) ⭐️ 8.0/10
9. [业余操作系统借助 Wine 运行 Windows 游戏](#item-9) ⭐️ 8.0/10
10. [为何前沿生态需向 Agent 云开放](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 与 Broadcom 推出首款定制 AI 推理芯片 Jalapeño](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 9.0/10

OpenAI 与 Broadcom 合作推出了首款定制 AI 芯片 Jalapeño，专为大语言模型推理设计，旨在提升效率并减少对通用 GPU 的依赖。 此举标志着 AI 推理向专用硬件的重大转变，有望降低运营成本、更高效地扩展 ChatGPT 等 AI 服务，并挑战 Nvidia 在 GPU 领域的主导地位。 该芯片由台积电制造，借助 OpenAI 的模型从设计到生产仅用九个月；初步测试显示其每瓦性能优于现有加速器，但详细基准测试结果尚未公布。

hackernews · jamdesk · 6月24日 17:47 · [社区讨论](https://news.ycombinator.com/item?id=48663324)

**背景**: AI 推理是指已训练模型生成响应的过程，需要高吞吐、低延迟的计算。与训练芯片（如 Nvidia H100）不同，推理芯片专为大规模运行预训练模型而优化。像 Jalapeño 这样的定制芯片允许企业针对特定模型架构定制硬件，可能比通用 GPU 实现更高效率。这延续了谷歌 TPU 等 AI 加速器开创的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/openai-broadcom-jalapeno-inference-chip/">OpenAI and Broadcom unveil LLM-optimized inference chip | OpenAI</a></li>
<li><a href="https://www.cnbc.com/2026/06/24/openai-and-broadcom-reveal-jalapeno-first-ai-chip-in-partnership.html">OpenAI and Broadcom reveal Jalapeno, first AI chip in partnership</a></li>
<li><a href="https://interestingengineering.com/ai-robotics/openai-jalapeno-ai-inference-chip-broadcom">OpenAI unveils Jalapeño chip for large-scale inference workloads</a></li>

</ul>
</details>

**社区讨论**: 评论既有对效率提升的兴奋，也有对 OpenAI 模型加速芯片设计这一说法的怀疑。一些用户指出制造方是台积电而非英特尔。此外，还有人关注更激进的定制设计，例如将模型权重直接刻入硅片。

**标签**: `#OpenAI`, `#custom chip`, `#Broadcom`, `#AI hardware`, `#inference`

---

<a id="item-2"></a>
## [Gemini 3.5 Flash 获得自主计算机使用能力](https://deepmind.google/blog/introducing-computer-use-in-gemini-3-5-flash/) ⭐️ 9.0/10

谷歌 DeepMind 在 Gemini 3.5 Flash 中引入了计算机使用功能，使模型能够通过解读屏幕截图并生成鼠标和键盘操作，自主与桌面应用进行交互。 这标志着向实用化 AI 智能体迈出的重要一步，此类智能体能够在数字环境中执行复杂的多步骤任务，有望改变自动化、无障碍访问和用户工作流程。 该能力可能依赖视觉理解和动作预测；早期用户反馈表明可靠性有限，且模型目前缺少 MCP（模型上下文协议）支持，这可能限制其在某些任务中的实用性。

rss · Google DeepMind Blog · 6月24日 16:30

**背景**: 计算机使用是指 AI 模型通过观察屏幕像素并生成输入事件来控制图形用户界面。多家公司正在开发类似功能，例如 OpenAI 的 Computer-Using Agent 和 Anthropic 的 Claude。Gemini 3.5 Flash 是谷歌 DeepMind 的多模态模型，专为速度和智能体任务设计，在编码和智能体基准测试中表现出色。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/gemini/flash/">Gemini 3.5 Flash — Google DeepMind</a></li>
<li><a href="https://openai.com/index/computer-using-agent/">Computer-Using Agent - OpenAI</a></li>

</ul>
</details>

**社区讨论**: Hacker News 用户对此持怀疑态度：有人报告 Gemini 在数据提取等简单任务中失败并放弃；另有人指出其基准测试得分落后于 Opus 4.8 和 GPT 5.5 等竞品，并慨叹缺少 MCP 支持。有人提到逆向工程 API 等替代方法更高效，导致对基于截图的计算机使用方式整体持谨慎态度。

**标签**: `#AI`, `#Gemini`, `#Google DeepMind`, `#Computer Use`, `#Autonomous Agents`

---

<a id="item-3"></a>
## [高通以 40 亿美元收购 Mojo 语言开发商 Modular](https://www.reuters.com/business/qualcomm-buy-ai-startup-modular-2026-06-24/) ⭐️ 8.0/10

高通宣布以 40 亿美元收购 AI 初创公司 Modular，该公司由 Chris Lattner 领导，并开发了 Mojo 编程语言。这笔交易标志着高通在 AI 软件与硬件集成方面迈出的战略一步。 此次收购可能强化高通的 AI 软件栈，使其芯片能更高效地运行 AI 工作负载，从而在 AI 基础设施市场加剧竞争。同时，这也引发了对 Mojo 语言未来开源发展的担忧。 Mojo 语言在 2026 年 5 月发布了 1.0 测试版，原计划于 2026 年秋季开源，但收购可能影响这一时间表。Mojo 基于 MLIR 编译器框架而非直接使用 LLVM，可生成针对 CPU、GPU 和 ASIC 等多种加速器的代码。

hackernews · timmyd · 6月24日 13:49 · [社区讨论](https://news.ycombinator.com/item?id=48659798)

**背景**: Modular 是一家由 Chris Lattner 创立的 AI 初创公司，Lattner 因创建 LLVM 和 Swift 而闻名。其核心产品是 Mojo 编程语言，旨在结合 Python 的易用性和 C++、Rust 的性能，适用于高性能 AI 和系统编程。高通是一家领先的半导体公司，以移动芯片闻名，近年来正将业务扩展到 AI 推理和边缘计算领域。此次收购反映了高通构建全面 AI 软件栈以与 NVIDIA 等公司竞争的雄心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Modular_AI">Modular AI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mojo_(programming_language)">Mojo (programming language)</a></li>
<li><a href="https://www.modular.com/">Modular : Inference from Kernel to Cloud</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：有人对收购时机感到意外，质疑高通在高端 AI 市场的地位；有人担忧 Mojo 的开源前景，并指出 Lattner 过去对硬件公司 AI 软件栈的批评颇具讽刺意味。也有观点认为这是高通战略布局的一部分，旨在超越移动领域，进军 AI 推理市场。

**标签**: `#AI`, `#acquisition`, `#Qualcomm`, `#Modular`, `#Mojo`

---

<a id="item-4"></a>
## [Bunny.net 免费提供最多 500 域名的 DNS 服务](https://bunny.net/blog/were-making-bunny-dns-free/) ⭐️ 8.0/10

Bunny.net 已全面取消 DNS 查询费用，现在为每个账户提供最多 500 个域名的免费 DNS 托管，无查询次数限制，也无隐藏的企业功能。 此举使 Bunny.net 成为 Cloudflare 的高性价比欧盟替代方案，加剧了 CDN/DNS 市场竞争，并吸引追求数据主权的用户。 免费套餐包含智能记录和健康监控功能，但每个账户限制 500 个域名；Bunny 的其他产品（如 CDN）仍会产生费用。

hackernews · dabinat · 6月24日 08:50 · [社区讨论](https://news.ycombinator.com/item?id=48657030)

**背景**: DNS（域名系统）将域名转换为 IP 地址。Bunny.net 是一家欧洲边缘平台，此前按 DNS 查询次数收费。此次免费举措顺应了 Cloudflare 开创的免费 DNS 托管趋势，旨在吸引用户使用更广泛的付费服务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bunny.net/dns/">Bunny DNS | The #1 Scriptable DNS Platform | bunny .net</a></li>
<li><a href="https://grokipedia.com/page/Bunnynet">Bunny.net</a></li>
<li><a href="https://euroalternative.eu/bunny-dns">Bunny DNS : European Alternative to Amazon Route 53 and...</a></li>

</ul>
</details>

**社区讨论**: 评论者赞赏 Bunny 作为美国 Cloudflare 的欧洲替代品，但部分人希望更清晰地说明价值。有人担心 Bunny 其他产品可能产生意外费用，同时认为此举是颇具竞争力的自主发展策略。

**标签**: `#DNS`, `#CDN`, `#free-tier`, `#Cloudflare-alternative`, `#networking`

---

<a id="item-5"></a>
## [NVIDIA 45°C 液冷设计使数据中心用水量趋近于零](https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/) ⭐️ 8.0/10

NVIDIA 推出了一种直触芯片液冷设计，其冷却液工作温度为 45°C，无需传统冷水机，从而使数据中心实现近乎零的用水量。 这一创新大幅降低了 AI 数据中心的环境影响，应对日益严重的水资源短缺和能耗问题。它可能为可持续的高性能计算基础设施树立新标准。 通过使用 45°C 冷却液，该设计省去了能耗巨大的冷水机，但全液冷架构可能需要新的维护流程，部件更换可能更复杂。

hackernews · nitin_flanker · 6月24日 14:10 · [社区讨论](https://news.ycombinator.com/item?id=48660178)

**背景**: 直触芯片液冷技术将冷却液直接导入 GPU 等高发热元件，比传统风冷散热效率更高。传统液冷系统通常需用冷水机将冷却液降至较低温度，会消耗大量水和能源。NVIDIA 的设计利用现代芯片能承受更高温度的特性，使用 45°C 冷却液，只需借助环境空气或简单蒸发即可散热，从而省去冷水机并大幅减少用水。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.parkplacetechnologies.com/blog/direct-to-chip-cooling-how-it-works-effectiveness/">Direct-to-Chip Cooling - How it Works and its Effectiveness</a></li>
<li><a href="https://www.supermicro.com/en/glossary/direct-to-chip-liquid-cooling">What Is Direct-to-Chip Liquid Cooling? - Supermicro</a></li>
<li><a href="https://attom.tech/direct-to-chip-liquid-cooling-how-it-works-and-application/">Direct-to-Chip Liquid Cooling : How It Works and Application</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了全液冷服务器的可行性，指出了维护方面的挑战，并对 45°C 方案的新颖性提出疑问。一些人强调了利用废热进行区域供暖的机会，另一些人则提到了 NASA 等已有的高温液冷系统。

**标签**: `#liquid cooling`, `#data center`, `#sustainability`, `#AI hardware`, `#energy efficiency`

---

<a id="item-6"></a>
## [约翰·卡马克反思 id Software 早期领导错误](https://twitter.com/ID_AA_Carmack/status/2069799283369345247) ⭐️ 8.0/10

约翰·卡马克发布了一条推特长文，承认他在 id Software 早期的领导错误，包括以不可持续的强度推动团队，引发了深入的行业讨论。 这一反思来自游戏开发领域的先驱人物，凸显了技术创新中常被忽视的人力成本，并引发了关于领导力与可持续工作文化的重要对话。 卡马克指出，对《雷神之锤》开发的强力推动可能让公司‘元气大伤’，但他认为这款标志性游戏值得付出代价；社区评论中提到了 Sandy Petersen 关于团队透支的不同观点。

hackernews · shadowtree · 6月24日 15:56 · [社区讨论](https://news.ycombinator.com/item?id=48661825)

**背景**: id Software 是一家开创性的游戏公司，以《毁灭战士》和《雷神之锤》闻名，由技术远见者约翰·卡马克联合创立。其早期文化以高强度工作推动技术极限，常被称为‘创业强度’，导致团队成员出现透支。

**社区讨论**: 社区普遍认可卡马克的技术成就，但对其取舍进行了辩论：一些人认为《雷神之锤》的遗产证明了付出的代价，而另一些人则指出随后创意人才的流失和团队士气问题。

**标签**: `#leadership`, `#software engineering management`, `#game development`, `#company culture`, `#tech history`

---

<a id="item-7"></a>
## [Show HN: Nub – 类似 Bun 的 Node.js 一体化工具包](https://github.com/nubjs/nub) ⭐️ 8.0/10

Nub 通过为原生 Node 添加转译器和模块钩子，提供类似 Bun 的 Node.js 开发体验，由 Zod 作者 Colin McDonnell 创建。

hackernews · colinmcd · 6月24日 14:14 · [社区讨论](https://news.ycombinator.com/item?id=48660267)

**标签**: `#nodejs`, `#typescript`, `#developer-tools`, `#bun`, `#javascript`

---

<a id="item-8"></a>
## [Rust 项目着手解除 crates.io 对 GitHub 的依赖](https://infosec.exchange/@mttaggart/116806641273303255) ⭐️ 8.0/10

Rust 项目已合并一项 RFC，旨在解除向 crates.io 发布 crate 时对 GitHub 的依赖，并已开始实施，但进展取决于志愿者工作和资金支持。 这降低了供应链风险和单点故障，使 Rust 生态系统更加健壮和去中心化，符合软件供应链安全的行业趋势。 该 RFC（rust-lang/rfcs#3963）制定了允许无 GitHub 仓库发布 crate 的计划。实施情况在 crates.io 的问题跟踪器中记录，但工作量巨大，需小心迁移以避免中断。

hackernews · speckx · 6月24日 19:40 · [社区讨论](https://news.ycombinator.com/item?id=48664733)

**背景**: crates.io 是 Rust 的官方包注册中心，类似于 JavaScript 的 npm 或 Python 的 PyPI。目前，发布 crate 需要链接到 GitHub 仓库，形成了对单一平台的依赖。该 RFC 旨在解耦发布流程，允许其他代码托管方案。Rust 项目主要由志愿者驱动，因此这类基础设施变更可能需要较长时间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Crates.io">Crates.io</a></li>
<li><a href="https://github.com/rust-lang/crates.io">GitHub - rust-lang/crates.io: The Rust package registry</a></li>
<li><a href="https://rust-lang.github.io/rfcs/0002-rfc-process.html">0002-rfc-process - The Rust RFC Book</a></li>

</ul>
</details>

**社区讨论**: 社区成员强调，解耦是一个复杂的“开着火车换铁轨”式问题。一些人指出 Cargo 仍与 npm 和 PyPI 存在相似的供应链风险，强调需要更广泛的加固。另一些人赞赏 Packagist 等注册中心强制从源码仓库打包的功能。大家一致认为志愿者工作和资金是瓶颈。

**标签**: `#Rust`, `#crates.io`, `#supply-chain`, `#GitHub`, `#open-source`

---

<a id="item-9"></a>
## [业余操作系统借助 Wine 运行 Windows 游戏](https://astral-os.org/posts/2026/04/03/wine-on-astral.html) ⭐️ 8.0/10

Astral OS，一个业余操作系统，于 2026 年 4 月 3 日宣布通过集成 Wine 兼容层实现了运行 Windows 游戏的功能。 这一成就表明，业余操作系统可以通过利用 Wine 等现有兼容层实现日常实用，可能降低开发者创建可行的替代操作系统的门槛，并引发关于遗留接口必要性的讨论。 实现细节包括在 Astral OS 上实现 Linux 兼容接口（如 POSIX）以承载 Wine，社区关注其是否绕过了 X11 而使用原生渲染，从而降低复杂性。

hackernews · avaliosdev · 6月24日 14:38 · [社区讨论](https://news.ycombinator.com/item?id=48660671)

**背景**: Wine 是一个兼容层，允许 Windows 应用程序在类 Unix 操作系统上运行，通过将 Windows API 调用转换为 POSIX 兼容等效调用，而无需模拟完整的 Windows 环境。它并非模拟器，而是提供一套库，将 Windows 功能映射到宿主机操作系统。业余操作系统通常是个人项目，不旨在广泛使用，往往缺乏使操作系统具备生产力的大量应用生态。Astral OS 项目旨在使这样的业余操作系统成为日常使用的可行系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Wine_compatibility_layer">Wine compatibility layer</a></li>
<li><a href="https://www.winehq.org/">WineHQ - Run Windows applications on Linux, BSD, Solaris and macOS</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：有人对业余操作系统必须实现 POSIX、Win32 等遗留接口感到绝望，而另一些人则称赞通过多层兼容性运行 Windows 游戏的技术壮举。有用户询问 Wine 是否在不使用 X 服务器的情况下原生移植，显示出对集成技术细节的兴趣。

**标签**: `#hobby-os`, `#wine`, `#compatibility`, `#windows-games`, `#operating-systems`

---

<a id="item-10"></a>
## [为何前沿生态需向 Agent 云开放](https://www.latent.space/p/databricks) ⭐️ 8.0/10

Databricks 联合创始人 Matei Zaharia 和 Reynold Xin 在一次罕见的联合采访中主张，开放的前沿生态系统对于让每家公司都能构建基于 Agent 的云架构至关重要。 这一观点之所以重要，是因为随着 AI Agent 成为云工作负载的核心，开放生态系统能防止厂商锁定并促进互操作性，使企业能在 AI 基础设施上自由创新。 这次采访汇集了 Apache Spark 和 Databricks 背后的两位关键人物，提供了关于开源原则如何应用于 Agent 云架构的内部视角。可能讨论了多 Agent 编排和数据集成等具体技术挑战。

rss · Latent Space · 6月24日 18:53

**背景**: Agent 云是指由自主 AI Agent 通过规划和调用工具处理复杂任务的云原生系统。Google Cloud 的文档将 Agent 架构描述为包含协调器和专用子 Agent 的系统。Databricks 作为数据和 AI 平台，强调开放性以防止生态碎片化。开放的前沿生态系统允许多个供应商和开源工具互操作，类似 Linux 或 Apache Spark 的模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@philippeandrepage/ai-agent-clouds-c8cf588f7392">Autonomous Agent Clouds . A Conceptual Framework for... | Medium</a></li>
<li><a href="https://www.agentcloud.dev/">Homepage | Agent Cloud - Open source platform to talk to your data</a></li>
<li><a href="https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components">Choose your agentic AI architecture components | Cloud Architecture Center | Google Cloud Documentation</a></li>

</ul>
</details>

**标签**: `#agent clouds`, `#Databricks`, `#open source`, `#AI infrastructure`, `#ecosystem`

---