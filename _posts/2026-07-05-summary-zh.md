---
layout: default
title: "Horizon Summary: 2026-07-05 (ZH)"
date: 2026-07-05
lang: zh
---

> 从 47 条内容中筛选出 10 条重要资讯。

---

1. [Anthropic 发布 Claude Science Beta 多智能体科学工作台](#item-1) ⭐️ 9.0/10
2. [YouTube Studio 提示注入漏洞泄露私密视频标题](#item-2) ⭐️ 8.0/10
3. [2.6 万学生研究揭示 AI 辅助作业导致两年后考试成绩下降 24%](#item-3) ⭐️ 8.0/10
4. [NVIDIA HORIZON：AI 代理实现 100% RTL 基准测试完成率](#item-4) ⭐️ 8.0/10
5. [Claude Code 会话泄露报告：幻觉还是漏洞？](#item-5) ⭐️ 7.0/10
6. [新版 Claude 模型工具调用模式遵循能力退步](#item-6) ⭐️ 7.0/10
7. [Midjourney 请愿好莱坞制片厂披露 AI 使用细节](#item-7) ⭐️ 7.0/10
8. [Anthropic 开发者分享针对 Fable 5 的盲点发现提示技巧](#item-8) ⭐️ 7.0/10
9. [OpenAI 联合创始人预测“几乎无界面”的未来](#item-9) ⭐️ 7.0/10
10. [Anthropic 启动 AI 新药研发，针对被药企忽视的疾病](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Anthropic 发布 Claude Science Beta 多智能体科学工作台](https://www.marktechpost.com/2026/07/04/anthropic-launches-claude-science-beta/) ⭐️ 9.0/10

Anthropic 于 2026 年 6 月 30 日发布了 Claude Science 测试版，这是一个多智能体 AI 工作台，可协调领域专家、审核智能体，并确保每个图表都包含用于重现的准确代码、环境和完整消息历史。 它通过自动化环境跟踪和引用检查，应对基因组学、蛋白质组学和化学信息学流程中的可重复性挑战，可能加速 AI 驱动的研究并提高结果可信度。 该工作台可管理本地机器、通过 SSH 连接的 HPC 和 Modal 无服务器计算；连接 60 多个数据库及 NVIDIA BioNeMo 技能；并具有一个审核智能体，用于标记和纠正引用和数字。

rss · MarkTechPost · 7月4日 16:21

**背景**: Claude 是 Anthropic 的大型语言模型系列。多智能体系统涉及多个专门 AI 智能体协作完成任务。可重复性意味着科学结果可以可靠地重复，通常需要准确的代码和环境记录。NVIDIA BioNeMo 是一个用于 AI 驱动生物学和药物发现的平台。Modal 为 AI 工作负载提供无服务器云计算。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/industries/healthcare-life-sciences/">NVIDIA AI Platforms for Healthcare and Life Sciences</a></li>
<li><a href="https://modal.com/">Modal : High-performance AI infrastructure</a></li>

</ul>
</details>

**标签**: `#AI`, `#science`, `#agents`, `#reproducibility`, `#Anthropic`

---

<a id="item-2"></a>
## [YouTube Studio 提示注入漏洞泄露私密视频标题](https://javoriuski.com/post/youtube) ⭐️ 8.0/10

在 YouTube Studio 的 AI 生成回复功能中发现了一个提示注入漏洞。攻击者通过精心构造的恶意评论，可以诱使 AI 泄露创作者私密视频的标题。 该漏洞突显了在没有适当输入清理的情况下将 LLM 集成到面向用户的应用程序中的风险。它可能导致隐私泄露，并证明了提示注入攻击在现实世界中的可利用性。 该攻击需要创作者对恶意评论点击 AI 建议的回复。泄露仅限于视频标题而非完整内容，且 YouTube 最初未将其归类为安全漏洞。

hackernews · javxfps · 7月4日 16:45 · [社区讨论](https://news.ycombinator.com/item?id=48786781)

**背景**: 提示注入是一种网络安全攻击，恶意输入会改变 AI 模型的行为。在此案例中，YouTube Studio 的 AI 功能处理评论并建议回复；如果评论中包含覆盖 AI 原始指令的命令，则可能导致泄露私人信息等意外操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection</a></li>
<li><a href="https://www.ibm.com/think/topics/prompt-injection">What Is a Prompt Injection Attack? | IBM</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：一些用户担心隐私问题，而另一些人则质疑该漏洞的实用性。一位前 Google 工程师解释了为什么该漏洞可能未得到优先处理，一些测试者报告无法复现此问题，暗示可能已被修复。

**标签**: `#prompt-injection`, `#security`, `#vulnerability`, `#YouTube`, `#AI`

---

<a id="item-3"></a>
## [2.6 万学生研究揭示 AI 辅助作业导致两年后考试成绩下降 24%](https://the-decoder.com/a-26000-student-study-shows-ais-hidden-learning-cost-takes-two-full-years-to-surface/) ⭐️ 8.0/10

一项针对超过 2.6 万名中国学生的研究发现，使用 AI 完成作业虽能短期提高成绩，但两年后考试成绩平均下降 24%，揭示出 AI 对学习效果的长期负面影响。 这表明在教育中不加限制地使用 AI 可能会损害学生的深层学习能力，影响知识体系的构建，对教育政策和实践具有重要警示意义。 研究显示，AI 的负面影响在两年后才完全显现，短期研究无法发现这种延迟效应；研究样本为中国学生，可能受文化因素影响。

rss · The Decoder · 7月4日 09:08

**背景**: 近年来，随着 ChatGPT 等 AI 工具的普及，学生越来越多地借助 AI 完成作业。人们一直担忧 AI 可能只提供答案而非促进真正的理解和记忆，这项研究为这种担忧提供了实证证据。

**标签**: `#AI in education`, `#study`, `#learning outcomes`, `#negative impact`, `#large-scale`

---

<a id="item-4"></a>
## [NVIDIA HORIZON：AI 代理实现 100% RTL 基准测试完成率](https://www.marktechpost.com/2026/07/04/nvidia-horizon-a-hands-free-agent-that-evolves-git-worktrees-and-hits-100-rtl-benchmark-completion/) ⭐️ 8.0/10

NVIDIA 推出了 HORIZON，这是一个无需人工干预的 AI 代理框架，能自主演化 Git worktree 来解决寄存器传输级（RTL）设计问题，并在各项基准测试中达到 100% 的完成率。 这一突破通过自动化复杂的 RTL 任务，可大幅加速硬件设计，显著减少芯片设计人员的开发时间和工作量，标志着向完全自主的 EDA 工具迈出了重要一步。 该框架使用带有 worktree 的版本化 Git 仓库来管理每个问题，但未提供有关底层模型、训练数据或局限性的更多技术细节。

rss · MarkTechPost · 7月4日 16:04

**背景**: RTL（寄存器传输级）是一种在硬件描述语言（如 Verilog 和 VHDL）中用于建模数字电路的设计抽象。Git worktree 允许开发者从单个仓库拥有多个工作目录，从而无需切换上下文即可并行处理不同分支。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.synopsys.com/glossary/what-is-register-transfer-level-design.html">What is Register-Transfer-Level (RTL) Design? | Synopsys</a></li>
<li><a href="https://git-scm.com/docs/git-worktree">Git - git-worktree Documentation</a></li>

</ul>
</details>

**标签**: `#AI agent`, `#RTL design`, `#NVIDIA`, `#benchmark`, `#automation`

---

<a id="item-5"></a>
## [Claude Code 会话泄露报告：幻觉还是漏洞？](https://github.com/anthropics/claude-code/issues/74066) ⭐️ 7.0/10

GitHub 上的一项 issue 报告称，Claude Code 在一次会话中意外引用了来自其他会话的 Minecraft 相关内容，表明可能存在跨会话数据泄露。Anthropic 团队正在调查，但怀疑这是 AI 幻觉。 如果确认为会话泄露，这可能表明代理式编程工具存在严重安全缺陷，或许会在用户或会话间暴露敏感数据。这凸显了人们对 AI 驱动开发工具中数据隔离和可靠性的日益担忧。 报告来自一个经过企业级 ZDR 认证的工作区；代理突然询问关于 Minecraft 砖块的问题。Anthropic 团队怀疑这是幻觉，可能受大上下文窗口或工具调用结果影响。另一位用户注意到 Google Gemini 中的类似行为，暗示可能存在缓存冲突。

hackernews · chatmasta · 7月4日 14:03 · [社区讨论](https://news.ycombinator.com/item?id=48785485)

**背景**: Claude Code 是 Anthropic 的一款代理式编程工具，能自主编辑文件和运行命令。AI 幻觉是指大语言模型生成看似合理但内容错误的输出。会话泄露指一个用户的数据意外暴露给另一个用户，这是基于云的 AI 服务中一个严重的安全漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/anthropics/claude-code/issues/74066">[Bug] Potential session/cache leakage between workspace ... - GitHub</a></li>
<li><a href="https://www.anthropic.com/product/claude-code">Claude Code | Anthropic's agentic coding system \ Anthropic</a></li>
<li><a href="https://letsdatascience.com/news/anthropic-claude-code-reports-potential-session-leakage-4919e15c">Anthropic Claude Code reports potential session leakage</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：一些人认为这是典型的幻觉，尤其是在大上下文环境下；其他人分享了来自不同供应商的类似跨会话事件，指出可能存在基础设施缺陷。Anthropic 团队成员确认正在调查，并认为这是幻觉。有人幽默地建议添加提示词以避免 Minecraft 话题。

**标签**: `#AI coding tools`, `#Claude`, `#hallucination`, `#session leakage`, `#security`

---

<a id="item-6"></a>
## [新版 Claude 模型工具调用模式遵循能力退步](https://simonwillison.net/2026/Jul/4/better-models-worse-tools/#atom-everything) ⭐️ 7.0/10

Armin Ronacher 报告称，较新的 Anthropic Claude 模型（特别是 Opus 4.8 和 Sonnet 5）在调用 Pi 的编辑工具时，有时会虚构额外字段，违反既定模式，而旧模型并未出现此问题。 SOTA 模型在工具调用合规性上的倒退对开发者而言违反直觉，可能影响依赖结构化工具交互的应用稳健性，暗示模型针对特定工具进行了过度优化。 问题出现在嵌套的'edits[]'数组中，模型会虚构不存在的键；Armin 推测，新版 Claude 模型因针对 Claude Code 自带的编辑工具（基于查找替换）进行了微调，导致对其他编辑工具模式的错误理解。

rss · Simon Willison · 7月4日 22:53

**背景**: LLM 的工具调用允许模型按照定义的 JSON 模式传递结构化参数来调用外部函数，模式遵循对可靠集成至关重要。SOTA 模型通常在基准测试中得分更高，但此例显示在特定实战能力上出现倒退。强化学习微调能让模型精通特定工具格式，有时会降低泛化能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ucafs.com/structured-output-benchmark-which-llms-are-best-at-json-tool-calls-and-schema-adherence">Structured Output Benchmark for LLMs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI models`, `#tool use`, `#Claude`, `#model reliability`, `#software development`

---

<a id="item-7"></a>
## [Midjourney 请愿好莱坞制片厂披露 AI 使用细节](https://techcrunch.com/2026/07/04/midjourney-wants-hollywood-studios-to-reveal-the-details-of-their-ai-usage/) ⭐️ 7.0/10

作为正在进行的版权诉讼的一部分，Midjourney 已提出法律动议，要求三家好莱坞制片厂披露其内部使用 AI 的细节。 这一举措可能迫使大型制片厂对其自身的 AI 实践保持透明，可能在 AI 版权争论中树立先例，并影响整个行业的披露规范。 具体涉及哪些制片厂和法律论点尚未公开，但该动议凸显了 Midjourney 通过质疑制片厂自身对 AI 的依赖来挑战其版权主张的策略。

rss · TechCrunch AI · 7月4日 18:00

**背景**: Midjourney 是一款从文本提示生成图像的生成式 AI 工具。它目前正与三家好莱坞制片厂进行版权诉讼，后者可能指控其模型在未经许可的情况下使用了受版权保护的材料进行训练。通过寻求揭示制片厂的 AI 使用，Midjourney 可能旨在削弱对方的诉讼立场或主张 AI 使用已广泛存在并被接受。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Midjourney">Midjourney</a></li>

</ul>
</details>

**标签**: `#AI`, `#copyright`, `#legal`, `#Hollywood`, `#Midjourney`

---

<a id="item-8"></a>
## [Anthropic 开发者分享针对 Fable 5 的盲点发现提示技巧](https://the-decoder.com/anthropic-developer-shares-prompting-tips-for-fable-5-that-focus-on-finding-your-own-blind-spots-first/) ⭐️ 7.0/10

Anthropic 开发者 Thariq Shihipar 推出了“盲点扫描”和“结构化访谈”等提示技巧，帮助程序员在借助 Claude 的 Fable 5 模型实施之前发现自身的无意识知识盲区。 在 Fable 5 这一强大模型面前，主要瓶颈已不再是 AI 的能力，而是用户的盲点；这些技巧将重点转向人的准备，有望提升代码质量和开发效率。 其中一个关键方法是“盲点扫描”，即请求 Claude 在不熟悉的代码库中找出未知的未知；另一种是结构化访谈，系统性地在编码前揭示盲区。

rss · The Decoder · 7月4日 12:37

**背景**: Claude Fable 5 是 Anthropic 最新的通用安全模型，基于 Mythos 级架构，已在 Claude 平台上线。所谓“盲点”指的是开发者没有意识到自己缺乏的知识或假设，这可能导致对 AI 的次优使用。这些技巧源于一个理念：与 AI 高效协作首先要理解自身的局限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/redeploying-fable-5">Redeploying Claude Fable 5 \ Anthropic</a></li>
<li><a href="https://the-decoder.com/anthropic-developer-shares-prompting-tips-for-fable-5-that-focus-on-finding-your-own-blind-spots-first/">Anthropic developer shares prompting tips for Fable 5 that focus on finding your own blind spots first</a></li>
<li><a href="https://thariqs.github.io/html-effectiveness/unknowns/01-blindspot-pass.html">Blindspot pass — Know your unknowns</a></li>

</ul>
</details>

**标签**: `#prompt engineering`, `#Claude`, `#Anthropic`, `#developer tips`, `#LLM`

---

<a id="item-9"></a>
## [OpenAI 联合创始人预测“几乎无界面”的未来](https://the-decoder.com/openai-cofounder-envisions-almost-no-interface-future-where-nobody-learns-software-anymore/) ⭐️ 7.0/10

格雷格·布罗克曼承认 ChatGPT 插件失败是因为模型尚未成熟，并设想未来由上下文感知的 AI 代理取代传统软件界面，使人们无需学习软件。 这一愿景标志着从以应用为中心向以代理为中心的计算模式转变，可能简化用户交互并加速 AI 融入日常任务，但也引发了对控制、隐私和软件开发者角色的问题。 布罗克曼表示，OpenAI 自家的编码 AI 代理 Codex 距离实现这一愿景还很遥远，而此前插件的失败凸显了当前模型在可靠工具使用方面的局限性。

rss · The Decoder · 7月4日 09:53

**背景**: ChatGPT 插件于 2023 年推出，是允许模型与外部服务交互的扩展，但时常产生不可靠的结果。OpenAI Codex 最初是基于 GPT-3 的 AI 系统，能将自然语言翻译成代码，后演变为能自动化软件任务的 AI 代理。设想的“几乎无界面”未来中，AI 代理可预测需求并无需明确指令即可行动，取代手动操作软件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(language_model)">OpenAI Codex (language model) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex">OpenAI Codex - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#user interface`, `#future of AI`, `#OpenAI`, `#Greg Brockman`

---

<a id="item-10"></a>
## [Anthropic 启动 AI 新药研发，针对被药企忽视的疾病](https://the-decoder.com/anthropic-launches-its-own-drug-discovery-programs-to-tackle-diseases-big-pharma-considers-unprofitable/) ⭐️ 7.0/10

Anthropic 启动了内部 AI 药物研发项目，旨在攻克因盈利能力不足而被制药企业忽视的疾病。诺华 CEO Vas Narasimhan 预计，AI 可将药物研发时间从十二年缩短至七到八年，并将成功率从 8%提高到 16%。 这标志着主流 AI 实验室直接介入药物研发的重大举措，关注未被满足的医疗需求而非利润。此举可能加速被忽视疾病的治疗，并为非商业性 AI 生物医学研究树立先例。 该项目将利用 Anthropic 的 Claude AI 模型进行药物设计与候选物筛选。目标是那些因患者数量少或利润率低而难以吸引投资的疾病。

rss · The Decoder · 7月4日 08:11

**背景**: 制药公司通常优先考虑患者市场庞大的疾病以最大化投资回报，导致罕见病或热带病等被忽视。AI 通过预测分子相互作用和优化临床试验，有望降低药物发现成本并缩短时间。

**标签**: `#Anthropic`, `#drug discovery`, `#AI for health`, `#neglected diseases`, `#pharma`

---