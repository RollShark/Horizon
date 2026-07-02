---
layout: default
title: "Horizon Summary: 2026-07-02 (ZH)"
date: 2026-07-02
lang: zh
---

> 从 84 条内容中筛选出 10 条重要资讯。

---

1. [日本最高法院裁定 AI 不能列为专利发明人](#item-1) ⭐️ 8.0/10
2. [Copilot Vision 现已正式推出](#item-2) ⭐️ 8.0/10
3. [微软成立 AI 部署公司，投入 25 亿美元](#item-3) ⭐️ 8.0/10
4. [Cloudflare 设 9 月 15 日为 AI 爬虫分离最后期限](#item-4) ⭐️ 8.0/10
5. [从微分几何视角看哈密顿神经网络](#item-5) ⭐️ 8.0/10
6. [Kimi K2.7 Code 已正式登陆 GitHub Copilot](#item-6) ⭐️ 7.0/10
7. [Senior SWE-Bench：面向高级软件工程任务的基准测试](#item-7) ⭐️ 7.0/10
8. [技能工程与一次性 AI 设计：智能体循环中的人类判断力](#item-8) ⭐️ 7.0/10
9. [AIEWF 辩论：全自动研究 vs. 人类能动性](#item-9) ⭐️ 7.0/10
10. [Introspection 联合创始人谈自动研究与自改进代理](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [日本最高法院裁定 AI 不能列为专利发明人](https://japannews.yomiuri.co.jp/science-nature/technology/20260306-314930/) ⭐️ 8.0/10

日本最高法院裁定，人工智能不能被列为专利申请的发明人，这与美国和欧洲的类似裁决一致。 该裁决为 AI 在创新中的角色和知识产权归属设置了重要的法律先例，确保人类发明人承担最终责任，可能影响全球 AI 政策讨论。 该裁决明确指出，只有自然人可以成为发明人，但并不排除 AI 辅助发明的可专利性，只要人类被列为发明人。

hackernews · mushstory · 7月2日 13:43 · [社区讨论](https://news.ycombinator.com/item?id=48761536)

**背景**: 全球专利法通常要求发明人为自然人。近年来，诸如 DABUS 项目等测试案例试图将 AI 列为发明人，但多个司法辖区的法院均裁定 AI 不具备发明人的法律人格。

**社区讨论**: 评论者大多支持该裁决，认为 AI 缺乏责任能力，不应拥有权利。部分人质疑专利制度的整体价值，也有人认为随着 AI 能力的增强，社会可能被迫重新考虑 AI 的人格地位。少数人指出，发明人只需自己署名即可轻松规避此规定。

**标签**: `#AI law`, `#patent`, `#Japan`, `#IP`, `#AI ethics`

---

<a id="item-2"></a>
## [Copilot Vision 现已正式推出](https://github.blog/changelog/2026-07-01-copilot-vision-is-generally-available) ⭐️ 8.0/10

GitHub Copilot 现在支持视觉输入，用户可以将图片和 PDF 附加到聊天提示中，让 AI 结合代码进行分析。 该功能使开发者能够就图表、截图和文档等视觉内容获取 AI 辅助，从而简化工作流程，减少上下文切换。 该功能支持附加图像和 PDF 文件；有关文件类型和限制的更多详细信息，请参阅官方文档。

rss · GitHub Changelog · 7月1日 18:39

**背景**: GitHub Copilot 是一款集成到 IDE 中的 AI 编码助手，此前仅接受文本提示。视觉功能的加入使其能够处理视觉信息，类似于多模态 AI 模型，从而增强了其在涉及 UI 设计、错误截图或文档等任务中的实用性。

**标签**: `#copilot`, `#vision`, `#github`, `#ai-assistant`, `#development-tools`

---

<a id="item-3"></a>
## [微软成立 AI 部署公司，投入 25 亿美元](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/) ⭐️ 8.0/10

微软成立了一家新的 AI 部署公司，承诺投入 25 亿美元，以加速 AI 服务交付。此举紧随亚马逊、OpenAI 和 Anthropic 的类似举措。 这表明科技巨头在 AI 基础设施投资上的竞争加剧，致力于提供企业级 AI 部署。这可能会重塑云 AI 服务，并影响企业大规模采用 AI 的方式。 该新集团可能专注于 Azure AI 服务，与 Amazon Bedrock 和 OpenAI 企业产品直接竞争。25 亿美元的金额反映了训练和运行大规模 AI 模型所需的巨额资本。

rss · TechCrunch AI · 7月2日 13:53

**背景**: AI 部署公司专注于帮助企业将 AI 模型集成到生产环境中并实现规模化。亚马逊推出了 Bedrock 用于托管基础模型部署，OpenAI 提供了企业级 API 访问，Anthropic 则强调安全可控的部署。微软此举利用其 Azure 云平台，提供全面的 AI 部署套件。

**标签**: `#Microsoft`, `#AI deployment`, `#industry`, `#investment`, `#Azure AI`

---

<a id="item-4"></a>
## [Cloudflare 设 9 月 15 日为 AI 爬虫分离最后期限](https://techcrunch.com/2026/07/01/cloudflares-new-policy-pushes-ai-companies-to-pay-for-publishers-content/) ⭐️ 8.0/10

Cloudflare 宣布新政策，要求 AI 公司在 9 月 15 日前将用于 AI 训练和 AI 代理的网络爬虫与用于搜索索引的爬虫分离开来，否则可能会在采用其服务的发布者网站上被默认拦截。 此举直击 AI 公司未经许可抓取发布者内容的争议问题，可能迫使其为数据访问谈判并付费。它可能重塑数据收集实践，并在 AI 时代强化发布者权益。 该政策可能利用 Cloudflare 作为 CDN 和 DNS 提供商的角色在基础设施层面进行拦截。AI 爬虫可能需要使用不同的用户代理字符串来区分用途，但确切的执行细节尚不明确。

rss · TechCrunch AI · 7月1日 17:48

**背景**: 网络爬虫是自动浏览网页的机器人，传统上被搜索引擎用于索引内容。近来，AI 公司使用爬虫收集模型训练数据并为与网站交互的 AI 代理提供动力。Cloudflare 作为主要的内容分发网络，保护和加速众多网站，使其有能力广泛执行此类政策。robots.txt 协议允许网站请求爬虫不要抓取，但遵守是自愿的且常被忽视。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Web_crawler">Web crawler</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent</a></li>
<li><a href="https://grokipedia.com/page/Web_Rendering_for_AI_Crawlers">Web Rendering for AI Crawlers</a></li>

</ul>
</details>

**标签**: `#AI`, `#web scraping`, `#Cloudflare`, `#data governance`, `#publishers`

---

<a id="item-5"></a>
## [从微分几何视角看哈密顿神经网络](https://www.reddit.com/r/MachineLearning/comments/1ukzdnj/hamiltonian_neural_networks_from_a_differential/) ⭐️ 8.0/10

一篇新博文从微分几何的视角解释哈密顿神经网络（HNN），强调了诺特定理在将对称性与模型架构中的守恒律联系起来方面的作用。 该视角提供了对 HNN 的更深层次理论理解，通过将物理对称性直接嵌入神经网络设计，可能提高泛化能力和效率。 该博文数学性较强，但包含交互式视觉内容以帮助说明概念。它基于 Greydanus 等人（2019 年）的原始 HNN 工作，并重点关注在物理信息神经网络文献中常被忽视的诺特定理。

reddit · r/MachineLearning · /u/FlameOfIgnis · 7月1日 21:55

**背景**: 哈密顿神经网络（HNN）是一类物理信息神经网络，通过使用哈密顿力学对系统进行建模，学习遵守守恒律，从而保证能量守恒。微分几何提供了描述相空间和对称性几何结构的数学框架。诺特定理确立了连续对称性与守恒量之间的对应关系，这是 HNN 可以利用以提高泛化能力的基础原理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/1906.01563">[1906.01563] Hamiltonian Neural Networks - arXiv.org</a></li>
<li><a href="https://en.wikipedia.org/wiki/Noether's_theorem">Noether's theorem</a></li>

</ul>
</details>

**标签**: `#Hamiltonian Neural Networks`, `#differential geometry`, `#physics-informed neural networks`, `#Noether's theorem`, `#machine learning`

---

<a id="item-6"></a>
## [Kimi K2.7 Code 已正式登陆 GitHub Copilot](https://github.blog/changelog/2026-07-01-kimi-k2-7-is-now-available-in-github-copilot/) ⭐️ 7.0/10

来自月之暗面的开源智能编程模型 Kimi K2.7 Code 现已作为模型选项正式在 GitHub Copilot 中推出。 此次集成扩展了开发者在 Copilot 内的模型选择，但正值 Copilot 近期价格调整引发用户不满、导致许多人转向 Claude Code 等替代品之际。 Kimi K2.7 Code 具备智能体能力，思维令牌使用量比前代减少 30%，并提供高速版本，输出速度可达 260 Tokens/s。其在 Copilot 中的定价与月之暗面官方一致：每百万输入令牌 0.95 美元，缓存命中令牌 0.19 美元，输出令牌 4.00 美元。

hackernews · GitHub Changelog · 7月2日 04:32 · [社区讨论](https://news.ycombinator.com/item?id=48756602)

**背景**: Kimi K2.7 Code 是月之暗面推出的一款以编程为核心的 AI 模型，以其长程推理和工具调用能力著称。GitHub Copilot 是一款广泛使用的 AI 编程助手，现已支持多种模型，用户可从不同提供商中选择。加入 Kimi K2.7 Code 反映了 AI 编程工具集成多样化专用模型以满足不同需求的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kimi.com/resources/kimi-k2-7-code">Kimi K2.7 Code: Open-Source Agentic Coding Model</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k2-7-code-quickstart">Kimi K2.7 Code - Kimi API Platform</a></li>

</ul>
</details>

**社区讨论**: 社区情绪复杂：许多用户对 Copilot 六月的定价调整表示不满，促使他们转向 Claude Code 或本地模型；但也有用户欢迎 Kimi K2.7 Code 作为有竞争力的选择，尤其适合希望使用非西方模型的企业，不过成本担忧依然存在。

**标签**: `#AI`, `#coding assistant`, `#GitHub Copilot`, `#model integration`, `#developer tools`

---

<a id="item-7"></a>
## [Senior SWE-Bench：面向高级软件工程任务的基准测试](https://senior-swe-bench.snorkel.ai/) ⭐️ 7.0/10

Senior SWE-Bench 是 Snorkel AI 发布的一个开源基准测试，采用接近现实的、不完整的自然语言指令，评估 AI 智能体处理需要高级软件工程技能的任务的能力。 该基准填补了评估 AI 智能体处理高级工程师面临的复杂、模糊任务的空白，超越了简单的指令遵循测试，将影响 AI 编程助手的衡量和改进方向。 Senior SWE-Bench 目前最高解决率是 Opus 4.8 的 24%，任务具有不完整的需求描述，逼真模拟了高级工程难题。该基准开源并设有公开排行榜。

hackernews · matt_d · 7月2日 02:55 · [社区讨论](https://news.ycombinator.com/item?id=48755928)

**背景**: SWE-Bench 是一个流行的基准测试，用于评估语言模型解决真实 GitHub 问题的能力。基准测试是用来比较 AI 模型能力的标准化测试。Senior SWE-Bench 扩展了这一概念，专注于需要高级工程判断的任务，其需求通常不明确，需要创造性地解决问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://senior-swe-bench.snorkel.ai/">Senior SWE-Bench</a></li>
<li><a href="https://news.ycombinator.com/item?id=48755928">open-source benchmark that assesses agents as senior engineers</a></li>
<li><a href="https://www.reddit.com/r/LocalLLaMA/comments/1ukzavr/senior_swe_bench_a_new_benchmark_focussed_on/">Senior SWE Bench: a new benchmark focussed on realistically ... - Reddit</a></li>

</ul>
</details>

**社区讨论**: 评论者幽默地指出，一个具备高级工程师水平的 LLM 可能会质疑整个项目，另一些人则提出设计动态对抗性基准。有人称赞 Opus 4.8 处理模糊需求的能力，但也质疑该基准的长期新颖性，并好奇人类合格分数应是多少。

**标签**: `#AI`, `#benchmark`, `#LLM`, `#agents`, `#software engineering`

---

<a id="item-8"></a>
## [技能工程与一次性 AI 设计：智能体循环中的人类判断力](https://www.latent.space/p/skill-engineering-design) ⭐️ 7.0/10

Paul Bakaus 讨论了在 AI 智能体工作流中需要人类判断力，批评一次性 AI 设计，并倡导将“技能工程”作为更可靠的方法。 这一观点挑战了全自主智能体的趋势，强调在复杂现实任务中，人类监督对于可靠性和控制力至关重要。 技能工程将 AI 工作流打包为明确的指令、示例和成功标准，使智能体能更可靠地执行任务；而一次性设计缺乏迭代的人类反馈，常会导致失败。

rss · Latent Space · 7月2日 14:36

**背景**: “技能工程”概念将 AI 智能体的能力形式化，类似于软件库，便于复用与组合。“一次性 AI 设计”指在单次生成中产生完整输出，无需人类干预。在“循环最大化”时代，开发者越来越依赖人机协同模式，通过迭代反馈改进 AI 输出。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.articsledge.com/post/skill-engineering">What Is Skill Engineering? The Complete 2026 Guide</a></li>

</ul>
</details>

**标签**: `#agents`, `#human-in-the-loop`, `#AI design`, `#skill engineering`, `#interview`

---

<a id="item-9"></a>
## [AIEWF 辩论：全自动研究 vs. 人类能动性](https://www.latent.space/p/aiewf-daily-dispatch-agency) ⭐️ 7.0/10

在 AIEWF 大会上，演讲者反对完全自动化的“软件工厂”愿景——即用 AI 驱动软件和研究，并捍卫人类理解与监督的重要性。 这场辩论凸显了 AI 工程的关键转折点：是追求完全自主系统，还是保持有意义的人类控制，这将影响开发实践、安全性和研究的未来。 反对声音出现在一个聚焦 AI 工程进展的会议上，关注点可能包括安全性、可解释性，以及人类直觉在解决复杂问题中不可替代的作用。

rss · Latent Space · 7月2日 06:13

**背景**: AI Engineer World's Fair (AIEWF) 是面向 AI 从业者、实验室和企业的大型行业会议。“软件工厂”愿景指通过 AI 驱动的流水线自动化开发，减少人类参与。“全自动研究”（autoresearch）由 Andrej Karpathy 推广，设想 AI 代理独立进行研究，取代传统以人类为主导的科研。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aiewf.shebecoding.com/">Explore AI Engineering Conference speakers and sessions</a></li>
<li><a href="https://github.com/karpathy/autoresearch">GitHub - karpathy/autoresearch: AI agents running research on single ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#automation`, `#human agency`, `#software development`, `#research`

---

<a id="item-10"></a>
## [Introspection 联合创始人谈自动研究与自改进代理](https://www.latent.space/p/autoresearch-introspection) ⭐️ 7.0/10

Introspection 联合创始人 Roland Gavrilescu 解释了自动研究（autoresearch）的概念，即 AI 代理通过自我改进循环自主进行研究和提升，并强调人类在软件工厂中仍不可或缺。 自动研究和自改进代理的概念可能显著加速 AI 发展，但明确人类角色可确保这些系统增强而非取代人类专长，从而影响软件开发方式。 采访详细介绍了用于构建自主工作流的代理配方，以及包含人类审批步骤的自改进循环，这些循环基于如 Karpathy’s autoresearch 等框架，用于 ML 实验。

rss · Latent Space · 7月1日 23:52

**背景**: 自动研究（autoresearch）由 Andrej Karpathy 推广，允许 AI 代理在单 GPU 上自主进行机器学习实验，超越了传统的超参数调优。代理配方（agent recipes）是构建基于 LLM 的代理的预定义模板，类似于 Anthropic 分享的通用模式。自改进代理循环则指代理根据反馈迭代改进代码或输出，通常需要人类审批以确保质量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openapps.pro/apps/autoresearch">autoresearch : Autonomous AI Research on a Single GPU</a></li>
<li><a href="https://addyosmani.com/blog/self-improving-agents/">AddyOsmani.com - Self-Improving Coding Agents</a></li>
<li><a href="https://agent-recipes-peach.vercel.app/">Agent Recipes</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#self-improving systems`, `#feedback loops`, `#autoresearch`, `#AI development`

---