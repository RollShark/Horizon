---
layout: default
title: "Horizon Summary: 2026-06-22 (ZH)"
date: 2026-06-22
lang: zh
---

> 从 23 条内容中筛选出 13 条重要资讯。

---

1. [Codex 日志漏洞可能导致 SSD 写入数 TB 数据](#item-1) ⭐️ 8.0/10
2. [我的旧工作只是因为欺诈而存在吗？](#item-2) ⭐️ 8.0/10
3. [文章探讨对数在自然与数学中的普遍性](#item-3) ⭐️ 8.0/10
4. [Cloudflare 推出临时 60 分钟账户](#item-4) ⭐️ 8.0/10
5. [Deno Desktop 支持多后端构建桌面应用](#item-5) ⭐️ 7.0/10
6. [Apertus：欧洲主权 AI 开放基础模型](#item-6) ⭐️ 7.0/10
7. [转向开放模型几乎没有缺点](#item-7) ⭐️ 7.0/10
8. [sqlite-utils 4.0rc1 新增迁移和嵌套事务](#item-8) ⭐️ 7.0/10
9. [矩阵循环单元更新：稳定性修复与并行扫描](#item-9) ⭐️ 7.0/10
10. [微调 Qwen 0.6B 模型进行问题分类](#item-10) ⭐️ 6.0/10
11. [ECCV 2026 论文决定申诉讨论](#item-11) ⭐️ 6.0/10
12. [微调 Whisper 以适应领域特定词汇的最佳方法](#item-12) ⭐️ 6.0/10
13. [探索在 LoRA 上使用 EMA 进行自蒸馏](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Codex 日志漏洞可能导致 SSD 写入数 TB 数据](https://github.com/openai/codex/issues/28224) ⭐️ 8.0/10

OpenAI Codex 存在一个日志漏洞，可能向本地 SSD 写入数 TB 数据，同时一个旋转动画会导致 GPU 使用率达到 100%。社区成员提供了变通方案，例如使用 SQLite 触发器阻止日志插入。 该漏洞可能显著缩短 SSD 寿命并降低用户体验，尤其对于依赖 Codex 进行 AI 辅助编码的开发者。这也引发了对广泛使用的 AI 工具软件质量的担忧。 该漏洞在 GitHub 上跟踪，已开放近六个月。一位用户报告称，对 SQLite 日志文件执行 VACUUM FULL 后，文件从 27GB 缩小到 73MB，表明日志严重膨胀。

hackernews · vantareed · 6月22日 07:30 · [社区讨论](https://news.ycombinator.com/item?id=48626930)

**背景**: OpenAI Codex 是一款本地运行的 AI 编码助手，会将交互记录到 SQLite 数据库中。配置错误的日志接收器可能导致过度写入，可能超过典型 SSD 的寿命（例如每年 640 TB）。旋转动画漏洞是另一个独立问题，在等待模型响应时导致 GPU 高使用率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.notebookcheck.net/OpenAI-Codex-has-a-bug-that-could-kill-your-SSD-in-under-a-year.1326191.0.html">OpenAI Codex has a bug that could kill your... - Notebookcheck News</a></li>
<li><a href="https://news.ycombinator.com/item?id=48626930">Codex logging bug may write TBs to local SSDs | Hacker News</a></li>
<li><a href="https://github.com/openai/codex/issues/16857">High GPU usage while the app is “thinking” due to tiny ...</a></li>

</ul>
</details>

**社区讨论**: 社区情绪普遍批评，用户称 Codex 为“垃圾软件”，并对长期存在的漏洞表示沮丧。一些用户赞赏 Codex 是开源的且可以修补，而另一些用户则指出 Claude Code 等竞争工具性能更好。

**标签**: `#OpenAI`, `#Codex`, `#bug`, `#performance`, `#AI tools`

---

<a id="item-2"></a>
## [我的旧工作只是因为欺诈而存在吗？](https://david.newgas.net/did-my-old-job-only-exist-because-of-fraud/) ⭐️ 8.0/10

一篇个人文章及 Hacker News 上的社区讨论探讨了许多技术岗位可能并非源于真实业务需求，而是由欺诈性账单、政府拨款滥用和承包商计划所维持。 这一发现挑战了技术就业的合法性认知，并引发了对纳税人资金被用于虚假岗位的道德担忧，可能影响行业信任和政策监管。 作者描述了自己之前的一份工作几乎无实际任务，却通过虚增合同和政府拨款获得资金。社区评论提供了具体案例，例如承包商通过外包公司以更高费率重新入职，以及经理在政府项目中篡改工时记录。

hackernews · advisedwang · 6月21日 21:40 · [社区讨论](https://news.ycombinator.com/item?id=48622867)

**背景**: 政府合同和拨款通常授予大型科技公司，这些公司可能通过分包方式虚增成本。欺诈性账单，如虚报工时或为未完成的工作收费，是政府采购中的已知问题。科技行业还严重依赖承包商和外包，为创造无实际价值的岗位提供了机会。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://oig.hhs.gov/fraud/contract-fraud/">Contract Fraud | Office of Inspector General | Government Oversight | U.S. Department of Health and Human Services</a></li>
<li><a href="https://fedpractice.com/practice-areas/government-contracts/government-contract-procurement-fraud-false-claims-act/">Government Contract Procurement Fraud and False Claims Act</a></li>
<li><a href="https://rm-firm.com/legal-blog/government-procurement-fraud/">10 Examples of Government Procurement Fraud | Reese Marketos LLP</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了技术岗位中的欺诈经历，包括加拿大政府拨款滥用、英国银行的承包商重新雇佣计划以及政府项目中的工时欺诈。普遍观点认为此类做法广泛存在且常不受惩罚，一些人指出欺诈可能是系统性的而非孤立的。

**标签**: `#fraud`, `#tech industry`, `#government contracts`, `#software engineering`, `#ethics`

---

<a id="item-3"></a>
## [文章探讨对数在自然与数学中的普遍性](https://alexkritchevsky.com/2026/05/25/everything-is-logarithms.html) ⭐️ 8.0/10

一篇题为《一切都是对数》的文章认为，对数是许多自然和数学现象背后的基本结构，从信息论到测量单位。 这一视角为理解不同领域提供了统一的框架，可能影响数学教学和测量系统的设计。 文章讨论了“无底对数”，并将其与 torsor（主齐性空间）这一数学概念联系起来，其中值在任意缩放或平移下定义。

hackernews · E-Reverance · 6月21日 21:10 · [社区讨论](https://news.ycombinator.com/item?id=48622626)

**背景**: 对数将乘法转化为加法，简化复杂计算。它们出现在信息论（比特、奈特）、物理学（分贝）等许多领域。Torsor 是一个像群一样运作但没有特定单位元的集合，常用于描述位置或货币等量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Principal_homogeneous_space">Principal homogeneous space - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Logarithm">Logarithm - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调了对数的 torsor 视角、对数表的历史使用，并批评文章缺乏类型系统来明确对数的对象和参照。一些评论者推荐进一步阅读李群理论和失传的对数艺术。

**标签**: `#mathematics`, `#logarithms`, `#information theory`, `#measurement`, `#essay`

---

<a id="item-4"></a>
## [Cloudflare 推出临时 60 分钟账户](https://simonwillison.net/2026/Jun/21/temporary-cloudflare-accounts/#atom-everything) ⭐️ 8.0/10

Cloudflare 现在允许任何人通过命令 `npx wrangler deploy --temporary` 在不注册的情况下部署 Workers 项目，部署持续 60 分钟。该部署是临时的，之后可以认领以获取永久所有权。 此功能大幅降低了开发者和 AI 代理测试和部署无服务器代码的门槛，使 Cloudflare Workers 更易上手。同时，它还为实验和自动化提供了临时环境。 临时账户持续 60 分钟，之后部署将被删除。用户可通过生成的 URL 认领项目以永久保留，该功能适用于任何使用 Wrangler CLI 的 Workers 项目。

rss · Simon Willison · 6月21日 22:01

**背景**: Cloudflare Workers 是一个在边缘运行代码的无服务器计算平台。Wrangler 是管理 Workers 项目的官方 CLI。此前，部署 Worker 需要创建 Cloudflare 账户并登录，这给快速测试或自动化工作流增加了障碍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.cloudflare.com/workers/wrangler/commands/">Commands - Wrangler · Cloudflare Workers docs</a></li>
<li><a href="https://developers.cloudflare.com/workers/platform/claim-deployments/">Claim deployments (temporary accounts) · Cloudflare Workers docs</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（文章中有链接）普遍称赞该功能简单实用，对 AI 代理和人类开发者都很有用。一些评论者指出 60 分钟的限制对于临时测试来说很宽松，而另一些人则讨论了潜在的滥用场景。

**标签**: `#Cloudflare`, `#serverless`, `#deployment`, `#AI agents`, `#developer tools`

---

<a id="item-5"></a>
## [Deno Desktop 支持多后端构建桌面应用](https://docs.deno.com/runtime/desktop/) ⭐️ 7.0/10

Deno Desktop 是一项新功能，允许开发者使用 Deno 构建原生桌面应用，支持 CEF、Webview 和 Raw 后端。它可将 Deno 项目编译为自包含的二进制文件，捆绑代码、Deno 运行时和渲染引擎。 该功能解决了桌面应用开发中的关键痛点，如捆绑大型浏览器引擎和管理权限。它通过提供共享运行时选项并利用 Deno 内置的权限系统，成为 Electron 的轻量级替代方案。 该功能支持三个后端：CEF（Chromium 嵌入式框架）、Webview（系统 Webview）和 Raw（无渲染）。跨应用的共享 CEF 运行时已在路线图中，这将使每个应用的二进制文件大小降至几兆字节。

hackernews · GeneralMaximus · 6月22日 05:38 · [社区讨论](https://news.ycombinator.com/item?id=48626137)

**背景**: Deno 是一个基于 V8、Rust 和 Tokio 的 JavaScript/TypeScript 运行时，以其安全优先的权限系统而闻名。传统的桌面应用开发需要捆绑整个浏览器引擎（如 Electron 捆绑 Chromium），导致二进制文件体积庞大。Deno Desktop 旨在通过提供多个后端和潜在的共享运行时来解决这个问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.deno.com/runtime/desktop/">Desktop apps | Deno Docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Chromium_Embedded_Framework">Chromium Embedded Framework - Wikipedia</a></li>
<li><a href="https://docs.deno.com/runtime/reference/cli/desktop/">deno desktop | Deno Docs</a></li>

</ul>
</details>

**社区讨论**: 社区总体持积极态度，用户称赞 Deno 的持续创新和共享运行时的潜力。一些用户请求增加“在浏览器中启动”选项，并对编译后二进制文件的权限透明度表示担忧。

**标签**: `#Deno`, `#Desktop`, `#CEF`, `#Webview`, `#Runtime`

---

<a id="item-6"></a>
## [Apertus：欧洲主权 AI 开放基础模型](https://apertvs.ai/) ⭐️ 7.0/10

由苏黎世联邦理工学院及其合作伙伴开发的 Apertus，作为一个完全开放、透明且多语言的基础模型，已作为欧洲主权 AI 倡议的一部分发布。 Apertus 是少数达到规模且完全开放的 LLM 之一，也是首个将多语言、透明性和合规性作为核心设计原则的模型，为欧洲部署提供了美国主导模型的法律上干净的替代方案。 该模型的 V1 版本性能不佳，团队正在开发 V2。社区反馈指出其多语言可靠性存在问题，例如幻觉生成不存在的词汇。

hackernews · T-A · 6月21日 21:29 · [社区讨论](https://news.ycombinator.com/item?id=48622778)

**背景**: 主权 AI 指国家或地区独立开发和部署 AI 的能力，以减少对外国供应商的依赖。Apertus 旨在提供一个完全开放的模型，可在欧洲基础设施上运行，无需依赖美国公司或政策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=48622778">Apertus – Open Foundation Model for Sovereign AI | Hacker News</a></li>
<li><a href="https://ethz.ch/en/news-and-events/eth-news/news/2025/09/press-release-apertus-a-fully-open-transparent-multilingual-language-model.html">Apertus: a fully open, transparent, multilingual language model | ETH Zurich</a></li>
<li><a href="https://www.aimadetools.com/blog/what-is-apertus-swiss-sovereign-ai-model/">What Is Apertus? Europe's Open Sovereign AI Model Explained</a></li>

</ul>
</details>

**社区讨论**: 社区情绪复杂：有人称赞该项目的主权雄心，但许多人批评其进展缓慢，且与 OLMo、K2 Think V2 和 Nemotron 等其他开放模型相比缺乏竞争力。用户报告多语言性能不可靠，并指出该团队与成熟的 LLM 提供商相比经验不足。

**标签**: `#open-source`, `#AI`, `#foundation model`, `#sovereignty`, `#LLM`

---

<a id="item-7"></a>
## [转向开放模型几乎没有缺点](https://www.marble.onl/posts/cancel_claude.html) ⭐️ 7.0/10

一篇博客文章认为，开放权重 LLM 是专有模型的可行替代方案，几乎没有缺点，引发了关于隐私、延迟和开源哲学的讨论。 这一讨论突显了开放模型与专有模型之间差距的缩小，可能推动企业转向更透明、更具成本效益的 AI 解决方案。 开放权重模型与真正的开源不同，它们保留训练数据和代码的秘密，但可以自托管以获得更好的隐私和更低的延迟。性能差距已从 20-30%缩小到某些基准测试中的接近持平。

hackernews · amarble · 6月21日 20:56 · [社区讨论](https://news.ycombinator.com/item?id=48622518)

**背景**: 开放权重 LLM 仅发布模型权重，而不发布训练数据或代码，这使得它们比专有 API 更透明，但不如真正的开源开放。FOSS 哲学强调用户研究、修改和共享软件的自由，这在开放权重模型中部分受到损害。最近的进展使开放权重模型与较旧的专有模型具有竞争力，从而减少了切换的缺点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.solarwinds.com/blog/open-source-llms-vs-open-weight-llms-vs-proprietary-llms">Open Source LLMs vs Open Weight LLMs vs Proprietary LLMs - SolarWinds Blog</a></li>
<li><a href="https://callsphere.ai/blog/open-weight-models-vs-proprietary-2026-enterprise-comparison">Open-Weight Models vs Proprietary: A 2026 Comparison ...</a></li>
<li><a href="https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models">The Best Open-Source LLMs in 2026</a></li>

</ul>
</details>

**社区讨论**: 评论者就第三方 API 提供商的隐私问题进行了辩论，有人建议对敏感数据使用路由规则。其他人指出，如果开放模型与较旧的专有版本匹配，则几乎没有理由不切换，而一些人批评开放权重模型缺乏真正的 FOSS 原则。

**标签**: `#open-source`, `#LLM`, `#AI`, `#privacy`, `#FOSS`

---

<a id="item-8"></a>
## [sqlite-utils 4.0rc1 新增迁移和嵌套事务](https://simonwillison.net/2026/Jun/21/sqlite-utils-40rc1/#atom-everything) ⭐️ 7.0/10

Simon Willison 发布了 sqlite-utils 4.0rc1，这是 4.0 版本的第一个候选发布版，引入了内置的数据库迁移功能和通过 db.atomic() 实现的嵌套事务支持。 此次更新显著增强了 sqlite-utils（一个广泛使用的 SQLite Python 库和命令行工具），通过添加关键的数据库管理功能，简化了开发者的模式演化和事务处理。 迁移功能移植自 sqlite-migrate 包，不支持反向迁移；嵌套事务通过 SQLite 保存点实现，允许在事务内部分回滚。

rss · Simon Willison · 6月21日 23:35

**背景**: sqlite-utils 是一个 Python 库和命令行工具，在 Python 内置的 sqlite3 模块之上提供更高级的操作。它支持复杂的表转换、从 JSON 自动创建表等功能。4.0 版本是一个主版本，包含一些不向后兼容的更改。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/21/sqlite-utils-40rc1/">sqlite-utils 4.0rc1 adds migrations and nested transactions</a></li>
<li><a href="https://github.com/simonw/sqlite-migrate">GitHub - simonw/sqlite-migrate: A simple database migration system for SQLite, based on sqlite-utils · GitHub</a></li>
<li><a href="https://pypi.org/project/sqlite-migrate/">sqlite-migrate · PyPI</a></li>

</ul>
</details>

**标签**: `#python`, `#sqlite`, `#database`, `#open source`, `#release`

---

<a id="item-9"></a>
## [矩阵循环单元更新：稳定性修复与并行扫描](https://www.reddit.com/r/MachineLearning/comments/1ubz5o8/an_update_on_matrix_recurrent_units_an_attention/) ⭐️ 7.0/10

作者更新了矩阵循环单元（MRU），这是一种线性时间的注意力替代方案，通过实现新的输入状态矩阵创建方法（如斜对称、LDU、QR）来解决训练不稳定性，并引入了并行扫描以实现高效的 GPU 计算。 这项工作探索了一种新颖的线性时间架构，可能降低 Transformer 的二次复杂度，从而实现高效的长序列建模。然而，在 TinyStories 等较大数据集上的初步结果显示，MRU 的性能不如 Transformer，凸显了扩展此类替代方案的挑战。 作者测试了四种矩阵构造方法：斜对称结合矩阵指数/Cayley 映射、LDU 分解加行列式约束、QR 分解以及标量因子除法。LDU 方法表现最佳，而强制正交矩阵（通过 Cayley 映射）反而阻碍了学习，表明剪切变换至关重要。

reddit · r/MachineLearning · /u/mikayahlevi · 6月21日 19:39

**背景**: Transformer 依赖的注意力机制随序列长度呈二次方扩展，导致长序列效率低下。Mamba 和线性注意力等线性时间替代方案旨在解决这一问题。矩阵循环单元（MRU）是一种循环架构，通过累积矩阵乘法实现线性复杂度，但早期版本存在训练不稳定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/mikayahlevi/mru-lm">GitHub - mikayahlevi/mru-lm: An LM forked from my transformer ...</a></li>
<li><a href="https://arxiv.org/abs/2312.00752">Mamba: Linear - Time Sequence Modeling with Selective State Spaces</a></li>
<li><a href="https://en.wikipedia.org/wiki/Prefix_sum">Prefix sum - Wikipedia</a></li>

</ul>
</details>

**标签**: `#attention alternative`, `#recurrent neural networks`, `#linear-time architecture`, `#deep learning`, `#sequence modeling`

---

<a id="item-10"></a>
## [微调 Qwen 0.6B 模型进行问题分类](https://www.teachmecoolstuff.com/viewarticle/fine-tuning-a-local-llm-to-categorize-questions) ⭐️ 6.0/10

一篇教程展示了如何微调 Qwen 3:0.6B 小型语言模型来对用户问题进行分类，使用自定义数据集和 LLaMA-Factory 工具。该方法旨在通过将问题映射到预定义类别后再查询数据库，从而提升检索效果。 这份实用指南降低了将小型 LLM 应用于文本分类任务的门槛，这些模型可在普通硬件上本地运行。它引发了关于微调小型 LLM 是否比使用更简单、更轻量的方法（如 sklearn 分类器）更值得投入的讨论。 该教程使用了 Qwen 3:0.6B（一个 6 亿参数的因果语言模型），并通过 LLaMA-Factory 进行微调。作者将问题映射到如“pool”等类别后再进行索引，但社区评论质疑对如此简单的任务进行微调的必要性。

hackernews · dev-experiments · 6月21日 22:55 · [社区讨论](https://news.ycombinator.com/item?id=48623434)

**背景**: 微调是指使用小型标注数据集将预训练 LLM 适配到特定任务。像 Qwen 0.6B 这样的小型模型对于设备端或成本敏感的应用很有吸引力。替代方法包括使用嵌入模型配合简单分类器（如 SVM），或使用零样本方法如 GliNER。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3-0.6B">Qwen / Qwen 3 - 0 . 6 B · Hugging Face</a></li>
<li><a href="https://blogs.novita.ai/qwen-3-0-6-why-small-models-still-matter-today/">Qwen 3 0 . 6 : Why Small Models Still Matter Today - Novita</a></li>
<li><a href="https://ai.learnmodernpython.com/fine-tune-small-open-models-for-custom-text-classification/">Fine - Tune Small Open Models For Custom Text Classification</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，对于简单的文本分类任务，传统机器学习方法（如基于 n-gram 的 sklearn SGDClassifier）效率更高，生成的模型不到 1MB，训练时间不到一分钟。其他人提出了项目思路，如使用零样本编码器、GRPO 训练或基于嵌入的分类器。一位用户询问分类如何改善检索，质疑其实际收益。

**标签**: `#fine-tuning`, `#LLM`, `#text classification`, `#small models`, `#practical ML`

---

<a id="item-11"></a>
## [ECCV 2026 论文决定申诉讨论](https://www.reddit.com/r/MachineLearning/comments/1uc0m1e/eccv_2026_paper_decision_appeals_discussion_d/) ⭐️ 6.0/10

ECCV 2026 已开放 Google 表单，允许作者基于政策错误、文书错误或明显的重大误解对论文决定提出申诉。一位 Reddit 用户报告称，尽管审稿人同意其贡献类型，且根据 ECCV 政策该类型不应受到惩罚，但其论文仍被拒绝。 此次讨论凸显了顶级计算机视觉会议的程序公正性，影响作者对审稿过程的信任。其结果可能影响未来会议如何处理申诉以及执行贡献类型指南。 申诉理由包括政策错误（例如应用不存在或不适用的政策）、文书错误（例如本意接收但被拒绝）以及明显的重大误解（历史上极为罕见）。该用户的论文得分为 6/4/3，且领域主席未推翻声明的贡献类型，但论文仍被拒绝。

reddit · r/MachineLearning · /u/Muted-Ad4511 · 6月21日 20:39

**背景**: ECCV（欧洲计算机视觉会议）是顶级的双年度会议。作者必须选择贡献类型（例如算法/通用、理论/基础）以对齐审稿人期望。评审标准的解释因类型而异，政策规定，除非领域主席明确反对，否则论文不应因其声明类型之外的方面受到惩罚。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eccv.ecva.net/Conferences/2026/SubmissionPolicies">ECCV 2026 Submission Policies</a></li>
<li><a href="https://eccv.ecva.net/Conferences/2026/AuthorContributionTypes">ECCV 2026 Author Contribution Types</a></li>
<li><a href="https://eccv.ecva.net/Conferences/2026/ACGuidance">Guidance to Area Chairs on Contribution Types - eccv.ecva.net</a></li>

</ul>
</details>

**社区讨论**: Reddit 帖子中的情绪不一：一些用户表示同情并考虑申诉，而另一些则指出申诉很少成功。少数评论者认为，某一标准上的低分（3）可能足以证明拒绝合理，无论贡献类型如何。

**标签**: `#ECCV`, `#conference`, `#paper appeal`, `#machine learning`

---

<a id="item-12"></a>
## [微调 Whisper 以适应领域特定词汇的最佳方法](https://www.reddit.com/r/MachineLearning/comments/1ubvmdx/best_current_methods_for_finetuning_whisper_on/) ⭐️ 6.0/10

一位 Reddit 用户询问针对领域特定西班牙语词汇微调 OpenAI 的 Whisper 语音识别模型的最佳当前方法和数据需求，并提到 LoRA、QLoRA 和 Spectrum 等已知技术。 这个问题对许多需要将 Whisper 适配到医疗或技术等专业领域的从业者很有意义，在这些领域准确识别特定术语至关重要。 该用户正在做一个需要可靠检测西班牙语特定单词和技术术语的项目，并希望了解除 LoRA、QLoRA 和 Spectrum 之外更新的或更好的适配方法。

reddit · r/MachineLearning · /u/gothenjoyer_ · 6月21日 17:18

**背景**: Whisper 是 OpenAI 开发的通用自动语音识别（ASR）模型，在多种音频上表现良好，但可能难以处理领域特定词汇。微调通过使用标注音频数据使模型适应专业领域。LoRA 和 QLoRA 等参数高效方法通过仅更新一小部分权重来降低计算成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/fine-tune-whisper">Fine - Tune Whisper For Multilingual ASR with Transformers</a></li>
<li><a href="https://github.com/Vaibhavs10/fast-whisper-finetuning">GitHub - Vaibhavs10/fast- whisper - finetuning · GitHub</a></li>
<li><a href="https://github.com/kartikmunjal/whisper-domain-adaptation">GitHub - kartikmunjal/ whisper - domain - adaptation · GitHub</a></li>

</ul>
</details>

**标签**: `#Whisper`, `#fine-tuning`, `#speech recognition`, `#domain adaptation`

---

<a id="item-13"></a>
## [探索在 LoRA 上使用 EMA 进行自蒸馏](https://www.reddit.com/r/MachineLearning/comments/1ubv0f5/ema_on_lora_r/) ⭐️ 6.0/10

一位 Reddit 用户正在寻找关于在 LoRA 适配器上使用指数移动平均（EMA）作为自教师进行在线自蒸馏的论文或实证结果，并引用了一篇最近使用 EMA 进行全参数微调的论文。 如果成功，在 LoRA 上应用 EMA 可以实现高效的自蒸馏微调大型模型，降低计算成本同时保持性能，这对资源受限的场景非常有价值。 引用的论文（arXiv:2601.19897）使用 EMA 进行在线自蒸馏，但采用的是全参数微调，而非 LoRA。用户特别询问 EMA 适配器为可训练适配器生成软标签的情况。

reddit · r/MachineLearning · /u/South-Conference-395 · 6月21日 16:54

**背景**: LoRA（低秩适配）是一种参数高效的微调方法，向冻结的预训练模型添加小型可训练矩阵。EMA（指数移动平均）维护模型权重的移动平均，常用于稳定训练或作为自蒸馏中的教师模型。自蒸馏利用模型自身生成软标签进行训练，以提升泛化能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://colab.research.google.com/github/codelion/ellora/blob/main/Ellora_Recipe_1_Self_Distillation_For_Quantization_Recovery.ipynb">Ellora_Recipe_1_Self_Distillation_For_Quantization_Recovery ...</a></li>
<li><a href="https://arxiv.org/abs/2605.29726">SLAD : Shared LoRA Adapters for Task Specific Distillation</a></li>

</ul>
</details>

**标签**: `#LoRA`, `#EMA`, `#self-distillation`, `#fine-tuning`, `#machine learning`

---