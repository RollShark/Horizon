---
layout: default
title: "Horizon Summary: 2026-08-13 (ZH)"
date: 2026-08-13
lang: zh
---

> 从 89 条内容中筛选出 10 条重要资讯。

---

1. [Qwen 发布 2.4T 参数 MoE 模型，95B 活跃参数](#item-1) ⭐️ 9.0/10
2. [在 NVIDIA GB300 NVL72 上运行 Qwen3.8-2.4T-A95B（2.4T 参数）并配置推理](#item-2) ⭐️ 9.0/10
3. [DeepSeek V4 Pro 0813 模型在 OpenRouter 上线](#item-3) ⭐️ 8.0/10
4. [xAI 发布 Grok 4.6，专注长时运行智能体与视觉工作](#item-4) ⭐️ 8.0/10
5. [AI 正在移除软件工程的中产阶级](#item-5) ⭐️ 8.0/10
6. [蒂莫西·高尔斯：大语言模型擅长哪些数学？](#item-6) ⭐️ 8.0/10
7. [DeepMind 推出 SL2T，Pixel 11 支持手语转文字](#item-7) ⭐️ 8.0/10
8. [GitHub 推出 Agent Plugins 1.0，一次构建跨多端使用](#item-8) ⭐️ 8.0/10
9. [OneAdvanced 在英国主权 AWS 上部署 50 多个 AI 智能体](#item-9) ⭐️ 8.0/10
10. [研究人员现在能以近乎完美的准确率从输出文本逆向还原 LLM 提示词](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Qwen 发布 2.4T 参数 MoE 模型，95B 活跃参数](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) ⭐️ 9.0/10

Qwen 发布了 Qwen3.8-2.4T-A95B，这是一个开放权重的 MoE 语言模型，总参数 2.4 万亿，活跃参数 950 亿，提供 BF16 和 FP8 格式。该模型定位为 Kimi K3 的竞争对手，性能接近 Opus 4.5/Fable 水平。 这一发布将前沿性能带入开放权重模型，使研究者和企业能够在许可和硬件条件允许的情况下运行与闭源模型竞争的系统。它加剧了 Qwen、月之暗面和 DeepSeek 等开放 MoE 模型之间的竞争。 模型卡在 Hugging Face 上提供 BF16 和 FP8 检查点；初始版本缺少低于 FP8 的 QAT 量化版本，也不具备官方 Qwen3.8-Max 中的视觉输入或 100 万上下文长度支持。社区估计 1 比特量化可将模型体积降至约 397GB，活跃参数仍为 95B，使高端消费级硬件上的本地服务成为可能。

hackernews · Philpax · 8月12日 15:01 · [社区讨论](https://news.ycombinator.com/item?id=49273478)

**背景**: MoE 模型的总参数分布在多个专家中，但每个 token 只激活一部分专家，因此推理成本主要由活跃参数而非总参数决定。然而，所有参数通常仍需要加载到内存或存储中，这使得大型 MoE 模型的服务硬件要求很高。Qwen 是阿里巴巴的开放权重模型系列；Kimi K3 是月之暗面公司的开放 MoE 模型，Opus 4.5/Fable 是作为性能基准的前沿闭源模型。量化会降低数值精度，例如从 BF16 降至 FP8 或更低，以牺牲一定质量来减少内存占用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained - Hugging Face</a></li>
<li><a href="https://medium.com/@csburakkilic/understanding-moe-architectures-the-difference-between-total-and-active-parameters-ad1d161fccaa">Understanding MoE Architectures: The Difference Between Total and Active Parameters | by Burak Kılıç | Medium</a></li>
<li><a href="https://www.inferless.com/learn/the-ultimate-guide-to-qwen-model">Qwen Models : Alibaba’s Next-Generation AI Family for Text, Vision...</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，由于发布时只有 BF16 和 FP8 版本，该模型比 Kimi K3 更难服务，合适的 4 比特量化需要大量校准资源。一些人强调 Unsloth 提供的约 397GB 的 1 比特量化版本可以在普通人能购买的机器上达到 Opus 4.5 级别的性能，而另一些人指出开放权重版本缺少 Qwen3.8-Max 的视觉和 100 万上下文特性。还有人对在普通硬件上运行如此大的模型表示怀疑和幽默，并提到 DeepSeek V4-Pro-0813 的基准测试分数。

**标签**: `#LLM`, `#Qwen`, `#MoE`, `#Hugging Face`, `#model release`

---

<a id="item-2"></a>
## [在 NVIDIA GB300 NVL72 上运行 Qwen3.8-2.4T-A95B（2.4T 参数）并配置推理](https://developer.nvidia.com/blog/serve-qwen3-8-2-4t-a95b-a-2-4t-parameter-model-with-configurable-reasoning-on-nvidia-gb300-nvl72/) ⭐️ 9.0/10

阿里巴巴发布了 Qwen3.8-2.4T-A95B（Qwen3.8-Max）的开源权重，这是一个拥有 2.4 万亿总参数、95B 活跃参数的稀疏混合专家模型；英伟达随后发布了在 GB300 NVL72 系统上部署该模型并启用可配置推理的指南。 这是目前最大的开源权重模型之一，将接近前沿的能力带给了开放生态；英伟达的部署指南降低了企业在高端基础设施上运行如此大规模模型的门槛，并凸显了可配置推理作为实际部署特性的重要性。 该模型为稀疏 MoE 架构，总参数 2.4 万亿，但每个 token 仅激活 95B 参数；Qwen3.8-Max 还增加了视觉输入、非思考模式和 1M 上下文等功能，GB300 NVL72 是英伟达的机架级系统，配备 72 个互联的 Blackwell Ultra GPU，面向大规模 AI 工作负载。

rss · NVIDIA AI Blog · 8月12日 18:23

**背景**: 混合专家（MoE）模型将每个输入仅路由到一部分专家参数，与同等总参数量的稠密模型相比，大幅降低了推理成本。开源权重使组织可以自行托管和微调模型，而无需依赖 API。英伟达 GB300 NVL72 通过 NVLink 将 72 个 GPU 连接在单一内存一致性域中，这对于服务万亿参数级别的模型至关重要。可配置推理允许操作员调整模型每个请求的思考量，在速度和答案质量之间做出权衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B">Qwen/ Qwen 3 . 8 - 2 . 4 T - A 95 B · Hugging Face</a></li>
<li><a href="https://openrouter.ai/qwen/qwen3.8-2.4t-a95b">Qwen 3 . 8 2 . 4 T A 95 B - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://theshiftmaker.in/featured/2026-07-21-nvidia-gb300-nvl72-sets-world-record-for-moe-pre-training-with-deepseek-v3-671b/">NVIDIA GB 300 NVL 72 Sets World Record for MoE... — The ShiftMaker</a></li>

</ul>
</details>

**标签**: `#open-weight model`, `#large language model`, `#model serving`, `#NVIDIA GB300`, `#configurable reasoning`

---

<a id="item-3"></a>
## [DeepSeek V4 Pro 0813 模型在 OpenRouter 上线](https://openrouter.ai/deepseek/deepseek-v4-pro-0813) ⭐️ 8.0/10

DeepSeek 发布了其旗舰模型 V4 Pro 的生产版本（版本号 0813），并在 OpenRouter 上线，结束了近四个月的预览期，基准测试成绩有所提升，API 定价也更具竞争力。 该模型提供 100 万 token 的上下文窗口，且 API 价格极具竞争力（输入每百万 token 0.435 美元，输出每百万 token 0.87 美元），可大幅降低开发成本，加剧 AI 实验室之间的竞争。 DeepSeek V4 Pro 0813 是一个混合专家模型，总参数 1.6 万亿，激活参数 490 亿。相比 4 月的预览版，它在 Terminal Bench 上提升了 15.8%，并以约 57 分之 1 的成本达到 Fable 5 性能；最大输出为 384,000 token。

hackernews · explosion-s · 8月12日 16:04 · [社区讨论](https://news.ycombinator.com/item?id=49274600)

**背景**: DeepSeek 是一家中国 AI 实验室，以低成本发布高性能开放权重模型而闻名。OpenRouter 是一个统一 API 平台，开发者可以通过单一接口访问多家提供商的大语言模型。混合专家（MoE）架构每次只激活部分参数，从而在保持质量的同时降低推理成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-pro-0813">DeepSeek V4 Pro 0813 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://www.unite.ai/deepseek-ships-v4-pro-as-its-flagship-model-leaves-preview/">DeepSeek Ships V4 Pro as Its Flagship Model Leaves ...</a></li>
<li><a href="https://wccftech.com/deepseek-prices-its-new-v4-pro-0813-model-at-0-87-per-1-million-output-tokens-as-the-high-flying-chinese-ai-lab-wows-with-its-soaring-token-consumption/">DeepSeek Prices Its New V4-Pro-0813 Model At $0.87 Per 1 ...</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体积极，多位用户称赞其在编程和繁重开发任务中的表现，有人报告在交通模拟器中获得显著性能提升。但也有用户批评 OpenRouter 页面缺少有用的基准测试信息、图表没有标注，并建议改链接到 DeepSeek 官方 API 文档和基准测试图片。

**标签**: `#deepseek`, `#ai-model`, `#llm`, `#openrouter`, `#ai-coding`

---

<a id="item-4"></a>
## [xAI 发布 Grok 4.6，专注长时运行智能体与视觉工作](https://x.ai/news/grok-4-6) ⭐️ 8.0/10

xAI 发布了 Grok 4.6，该模型基于 Grok 4.5 构建，尤其关注长时间运行的智能体以及更具雄心的交互和视觉任务。 作为主要 AI 实验室发布的新前沿模型，Grok 4.6 加剧了大语言模型领域的竞争，并可能影响智能体和视觉应用的价格与能力。 据官方公告，Grok 4.6 基于 Grok 4.5 构建，专注于长时间运行的智能体以及更具雄心的交互和视觉工作；但一些用户反映默认系统提示导致模型拒绝讨论系统提示。

hackernews · iLuddite · 8月12日 15:32 · [社区讨论](https://news.ycombinator.com/item?id=49274027)

**背景**: Grok 是 xAI 推出的生成式 AI 大语言模型系列，于 2023 年 11 月首次发布。该系列从 Grok-1 发展到 Grok 4，其中 Grok 4.5 此前已发布并与 Cursor 联合开发。这些模型逐步增加了图像生成、网络搜索、'Think'推理模式以及通过 Grok Build 进行智能体编程等能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://x.ai/news/grok-4-6">Introducing Grok 4.6 | SpaceXAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Grok_4">Grok 4</a></li>

</ul>
</details>

**社区讨论**: 社区评论总体上对 Grok 的竞争力持乐观态度，用户称赞其简洁、快速和高性价比；但也有人担忧基准测试被操纵以及不同实验室快速出现类似能力。另有用户报告一个技术问题：默认系统提示导致模型拒绝讨论系统提示。

**标签**: `#AI`, `#LLM`, `#Grok`, `#xAI`, `#Model Release`

---

<a id="item-5"></a>
## [AI 正在移除软件工程的中产阶级](https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html) ⭐️ 8.0/10

Florian Herrengt 的博客文章认为，AI 通过自动化常规编码任务正在消除软件工程的“中产阶级”。这篇文章在 Hacker News 上引发了高分讨论，获得了 675 分和 600 条评论。 这很重要，因为 AI 可能同时放大好的和坏的工程实践，改变软件团队分配工作的方式，并引发关于行业就业安全和代码质量的疑问。 社区评论指出，“坏”工程师现在可以在整个组织内放大糟糕的工程质量，而且 AI 自动化了传统上“Stack Overflow 工程师”的角色。但也有评论者指出，目前还没有确凿证据表明 LLM 编码智能体导致软件工程岗位流失。

hackernews · florianherrengt · 8月12日 13:20 · [社区讨论](https://news.ycombinator.com/item?id=49271994)

**背景**: 大型语言模型（LLM）是经过海量文本训练、能够理解和生成语言（包括代码）的 AI 模型。它们为编码助手提供支持，可以根据自然语言提示编写、补全和解释代码。现代 LLM 通常采用 Transformer 架构，并经过指令微调，使其能够协助完成以前由初级或中级工程师承担的软件开发任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model</a></li>
<li><a href="https://www.ibm.com/think/topics/large-language-models">What Are Large Language Models (LLMs)? | IBM</a></li>

</ul>
</details>

**社区讨论**: 整体情绪喜忧参半：许多人认为 AI 可以自动化常规编码，同时放大好的和坏的工程实践，也有人警告不要外包批判性思维和积累技术债务。还有人质疑是否有真实的工作岗位流失证据，或指出技术数十年来一直在使经济分化。

**标签**: `#AI`, `#software engineering`, `#job market`, `#automation`, `#LLMs`

---

<a id="item-6"></a>
## [蒂莫西·高尔斯：大语言模型擅长哪些数学？](https://gowers.wordpress.com/2026/08/12/what-sort-of-maths-are-llms-good-at/) ⭐️ 8.0/10

2026 年 8 月 12 日，数学家蒂莫西·高尔斯发表博客，分析大语言模型真正擅长的数学任务，认为其优势在于采样、模式匹配和反例搜索，而非人类式的创造性定理证明。 高尔斯是知名数学家，他的判断对人工智能和数学界具有重要影响，有助于调整对大语言模型数学能力的预期，并将研究方向从基准测试热转向真正的证明能力。 关键区别在于，测试时扩展（采样大量候选解并筛选或投票）支撑了 AlphaCode 在 2022 年编程竞赛中的表现，但高尔斯认为这不同于发现全新、事后看来优美自然的数学方法。

hackernews · ColinWright · 8月12日 10:04 · [社区讨论](https://news.ycombinator.com/item?id=49270022)

**背景**: 大语言模型通过从概率分布中采样选择下一个词元来生成文本；测试时扩展在推理阶段分配额外计算资源，可生成多个候选答案并通过投票或验证筛选。数学基准旨在评估推理能力，但可能过度奖励模式匹配而非真正的证明。这些概念是高尔斯区分当前优势与人类式创造数学的核心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.04001">Test-Time Scaling in Reasoning LLMs: Inference Regimes ...</a></li>
<li><a href="https://medium.com/@shashankag14/understanding-sampling-techniques-in-large-language-models-llms-dfc28b93f518">Sampling Techniques in Large Language Models (LLMs) | by Shashank Agarwal | Medium</a></li>

</ul>
</details>

**社区讨论**: 评论区总体认同高尔斯，认为其观点实质是测试时扩展：有人指出 AlphaCode 在 2022 年通过大规模采样和筛选就已超过普通程序员。也有人赞同人类级证明应产生新奇、事后看来自然且不易偶然发现的方法；还有人分享 AI 数学成果列表，并对 AI 在时序逻辑等领域未经检验的能力提出疑问。

**标签**: `#LLMs`, `#mathematics`, `#AI reasoning`, `#test-time scaling`, `#benchmarks`

---

<a id="item-7"></a>
## [DeepMind 推出 SL2T，Pixel 11 支持手语转文字](https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/) ⭐️ 8.0/10

谷歌 DeepMind 推出了 SL2T 手语转文字模型，并在 Pixel 11 上首次亮相；最初支持美国手语转英语，用户可以在 Gboard 和 Live Transcribe 中直接通过手语输入，而不必打字。 这能显著改善聋人和听障用户的数字无障碍体验，让他们用更自然的方式交流，减少对打字的依赖；也可能推动移动平台上手语识别技术的更广泛应用。 SL2T 被描述为一个多语言翻译模型，但首发仅支持美国手语到英语，且只在 Pixel 11 机型上的 Gboard 和 Live Transcribe 中提供。

rss · Google DeepMind Blog · 8月12日 14:01

**背景**: Live Transcribe 是谷歌为 Android 开发的无障碍应用，可将语音和环境声音实时转换成文字字幕，下载量已超过 5 亿次。Gboard 是谷歌的虚拟键盘。美国手语（ASL）是许多美国聋人使用的视觉语言；手语识别通过计算机视觉解读手形和动作。SL2T 让用户面对摄像头打手语来生成文字，而无需手动打字。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://siliconangle.com/2026/08/12/google-debuts-sl2t-ai-model-thats-designed-understand-sign-language/">Google debuts SL2T, an AI model that's designed to understand sign language - SiliconANGLE</a></li>
<li><a href="https://techmymoney.com/2026/08/12/deepmind-sl2t-brings-asl-input-to-pixel-11-phones/">DeepMind SL2T Brings ASL Input to Pixel 11 Phones</a></li>
<li><a href="https://en.wikipedia.org/wiki/Live_Transcribe">Live Transcribe</a></li>

</ul>
</details>

**标签**: `#AI`, `#sign language recognition`, `#accessibility`, `#DeepMind`, `#computer vision`

---

<a id="item-8"></a>
## [GitHub 推出 Agent Plugins 1.0，一次构建跨多端使用](https://github.blog/changelog/2026-08-12-agent-plugins-1-0-in-vs-code-copilot-cli-and-the-copilot-app) ⭐️ 8.0/10

8 月 6 日，GitHub 与 AWS、Anysphere、Microsoft、OpenAI 和 Vercel 联合发布 Agent Plugins 1.0，开发者只需构建一次插件，即可在 VS Code、Copilot CLI 和 Copilot 应用等兼容的 AI 智能体客户端中使用。 这为 AI 智能体确立了供应商中立、跨客户端的插件标准，减少碎片化，使可复用的 agent 技能和 MCP 服务器能覆盖更广泛生态。开发者只需面向一种插件格式，无需为每个客户端单独集成，有望加速 AI 工具生态发展。 Agent Plugins 1.0 是一个开放、中立的标准，将 Agent Skills 和 MCP 服务器打包为可移植插件，包含插件清单（plugin manifest）和 MCP 配置 schema。该发布公告本身未提供深层技术细节，但规范要求每个版本发布时两个 schema 与规范版本保持一致。

rss · GitHub Changelog · 8月12日 18:39

**背景**: Agent Plugins 是一种新兴的开放标准，用于将可复用的 AI 智能体组件（如任务专用技能和 MCP 服务器）打包为可分发插件。GitHub Copilot CLI 是基于终端的 Copilot 客户端，可运行 agent 并使用自定义技能；VS Code 和 Copilot 应用则是其他常见的 Copilot 界面。所列合作伙伴包括主要 AI 编程和开发者工具厂商，其中 Anysphere 是 Cursor 背后的公司。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agent-plugins.org/">Agent Plugins</a></li>
<li><a href="https://grokipedia.com/page/GitHub_Copilot_CLI">GitHub Copilot CLI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Anysphere">Anysphere</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#developer tools`, `#GitHub Copilot`, `#plugins`, `#VS Code`

---

<a id="item-9"></a>
## [OneAdvanced 在英国主权 AWS 上部署 50 多个 AI 智能体](https://aws.amazon.com/blogs/machine-learning/how-oneadvanced-deployed-over-50-ai-agents-on-uk-sovereign-aws/) ⭐️ 8.0/10

OneAdvanced 通过在 Amazon SageMaker AI 上自行托管 Llama 4 Maverick 和 Llama Guard 4，使用 pgvector 进行检索增强生成（RAG），并在 Amazon ECS 上采用 Strands Agents SDK，构建了一个英国主权 AI 平台，部署了 50 多个 AI 智能体。 该案例为需要数据主权和监管合规的企业提供了实用蓝图，展示了如何在主权云基础设施上组合开放权重模型、安全护栏和智能体框架。这对面临 AI 和数据驻留规则日益严格的英国及欧洲组织尤其具有参考价值。 该部署在 Amazon SageMaker AI 上使用 Llama 4 Maverick（170 亿活跃参数，128 个专家的 MoE 模型）和 Llama Guard 4（120 亿参数安全分类器），并采用 pgvector 进行 RAG，在 Amazon ECS 上运行 Strands Agents SDK。摘要未提供具体的智能体用例、评估指标或性能细节。

rss · AWS Machine Learning Blog · 8月12日 13:46

**背景**: Llama 4 Maverick 是 Meta 推出的开放权重多模态模型，拥有 170 亿活跃参数和 128 个专家；Llama Guard 4 是一个 120 亿参数的安全分类器，用于检测有害提示和回复。Amazon SageMaker AI 是用于训练和托管模型的托管机器学习服务，Amazon ECS 是容器编排服务。pgvector 是 PostgreSQL 的扩展，用于存储和搜索向量嵌入，常用于检索增强生成（RAG）。Strands Agents SDK 是 AWS 开源的智能体框架，能以少量代码构建 AI 智能体；英国主权 AWS 部署将数据和负载保持在英国管辖范围内。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/">Introducing Strands Agents , an Open Source AI Agents SDK</a></li>
<li><a href="https://huggingface.co/meta-llama/Llama-Guard-4-12B">meta-llama/Llama-Guard-4-12B · Hugging Face</a></li>
<li><a href="https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct">meta-llama/Llama-4-Maverick-17B-128E-Instruct · Hugging Face</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#sovereign AI`, `#AWS`, `#Llama`, `#RAG`

---

<a id="item-10"></a>
## [研究人员现在能以近乎完美的准确率从输出文本逆向还原 LLM 提示词](https://the-decoder.com/researchers-can-now-reverse-engineer-llm-prompts-from-output-text-with-near-perfect-accuracy/) ⭐️ 8.0/10

印度理工学院孟买分校和 Adobe Research 的研究人员开发了一种名为“Previous-Token Prediction”的逆向语言模型，它无需获取模型权重，即可从 LLM 的输出中以近乎完美的准确率重建原始提示词，并且该方法可在不同模型间工作。 这对依赖专有系统提示词的企业构成严重安全风险，可能导致精心设计的提示词和相关知识产权泄露，进而影响更广泛的 LLM 应用生态。 PTP 并非微调预训练序列到序列模型，而是完全从头训练一个基于解码器的逆向 LLM，其训练数据由目标模型自身生成的合成数据构成，不需要访问 logits、梯度、嵌入或原始训练数据；它通过给定未来上下文预测前一个 token 来镜像前向模型的训练目标。

rss · The Decoder · 8月12日 17:32

**背景**: 大语言模型通常通过“下一个 token 预测”进行训练，模型根据已有文本预测后续 token；模型逆向攻击则试图从模型输出推断输入或训练数据，是利用模型统计信息的隐私攻击方式。此前的研究已表明可以从语言模型的输出中恢复前缀文本或提示词，而这项工作进一步实现了近乎精确的提示词重建。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.29378">PTP: Previous-Token Prediction based LLM InversionforNear-Exact Prompt Reconstruction</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_inversion_attack">Model inversion attack</a></li>
<li><a href="https://openreview.net/forum?id=t9dWHpGkPj">Language Model Inversion | OpenReview</a></li>

</ul>
</details>

**标签**: `#LLM`, `#prompt engineering`, `#AI security`, `#model inversion`, `#research`

---