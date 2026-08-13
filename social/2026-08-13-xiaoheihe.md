---
layout: default
title: "小黑盒文案｜2026-08-13"
date: 2026-08-13
---

# 小黑盒文案｜2026-08-13

## 标题

2026-08-13 AI/开发者技术速递：8 条值得关注的更新

## 正文

今天从 Horizon 晨报里筛了 8 条相对值得看的 AI / 开发者动态，按重要性排序：

1. Qwen 发布 2.4T 参数 MoE 模型，95B 活跃参数（9.0/10）
   - 看点：Qwen 发布了 Qwen3.8-2.4T-A95B，这是一个开放权重的 MoE 语言模型，总参数 2.4 万亿，活跃参数 950 亿，提供 BF16 和 FP8 格式。该模型定位为 Kimi K3 的竞争对手，性能接近 Opus 4.5/Fable 水平。 这一发布将前沿性能带入开放权重模型，使研究者和企业能够在许可和硬件条件允许的情况下运行与闭源模型竞争的系统。
   - 原文：https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B

2. 在 NVIDIA GB300 NVL72 上运行 Qwen3.8-2.4T-A95B（2.4T 参数）并配置推理（9.0/10）
   - 看点：阿里巴巴发布了 Qwen3.8-2.4T-A95B（Qwen3.8-Max）的开源权重，这是一个拥有 2.4 万亿总参数、95B 活跃参数的稀疏混合专家模型；英伟达随后发布了在 GB300 NVL72 系统上部署该模型并启用可配置推理的指南。
   - 原文：https://developer.nvidia.com/blog/serve-qwen3-8-2-4t-a95b-a-2-4t-parameter-model-with-configurable-reasoning-on-nvidia-gb300-nvl72/

3. DeepSeek V4 Pro 0813 模型在 OpenRouter 上线（8.0/10）
   - 看点：DeepSeek 发布了其旗舰模型 V4 Pro 的生产版本（版本号 0813），并在 OpenRouter 上线，结束了近四个月的预览期，基准测试成绩有所提升，API 定价也更具竞争力。
   - 原文：https://openrouter.ai/deepseek/deepseek-v4-pro-0813

4. xAI 发布 Grok 4.6，专注长时运行智能体与视觉工作（8.0/10）
   - 看点：xAI 发布了 Grok 4.6，该模型基于 Grok 4.5 构建，尤其关注长时间运行的智能体以及更具雄心的交互和视觉任务。 作为主要 AI 实验室发布的新前沿模型，Grok 4.6 加剧了大语言模型领域的竞争，并可能影响智能体和视觉应用的价格与能力。
   - 原文：https://x.ai/news/grok-4-6

5. AI 正在移除软件工程的中产阶级（8.0/10）
   - 看点：Florian Herrengt 的博客文章认为，AI 通过自动化常规编码任务正在消除软件工程的“中产阶级”。这篇文章在 Hacker News 上引发了高分讨论，获得了 675 分和 600 条评论。 这很重要，因为 AI 可能同时放大好的和坏的工程实践，改变软件团队分配工作的方式，并引发关于行业就业安全和代码质量的疑问。
   - 原文：https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html

6. 蒂莫西·高尔斯：大语言模型擅长哪些数学？（8.0/10）
   - 看点：2026 年 8 月 12 日，数学家蒂莫西·高尔斯发表博客，分析大语言模型真正擅长的数学任务，认为其优势在于采样、模式匹配和反例搜索，而非人类式的创造性定理证明。 高尔斯是知名数学家，他的判断对人工智能和数学界具有重要影响，有助于调整对大语言模型数学能力的预期，并将研究方向从基准测试热转向真正的证明能力。
   - 原文：https://gowers.wordpress.com/2026/08/12/what-sort-of-maths-are-llms-good-at/

7. DeepMind 推出 SL2T，Pixel 11 支持手语转文字（8.0/10）
   - 看点：谷歌 DeepMind 推出了 SL2T 手语转文字模型，并在 Pixel 11 上首次亮相；最初支持美国手语转英语，用户可以在 Gboard 和 Live Transcribe 中直接通过手语输入，而不必打字。 这能显著改善聋人和听障用户的数字无障碍体验，让他们用更自然的方式交流，减少对打字的依赖；也可能推动移动平台上手语识别技术的更广泛应用。
   - 原文：https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/

8. GitHub 推出 Agent Plugins 1.0，一次构建跨多端使用（8.0/10）
   - 看点：8 月 6 日，GitHub 与 AWS、Anysphere、Microsoft、OpenAI 和 Vercel 联合发布 Agent Plugins 1.0，开发者只需构建一次插件，即可在 VS Code、Copilot CLI 和 Copilot 应用等兼容的 AI 智能体客户端中使用。
   - 原文：https://github.blog/changelog/2026-08-12-agent-plugins-1-0-in-vs-code-copilot-cli-and-the-copilot-app

整体看，今天的信息流更偏开发工具、模型生态和工程实践。如果只挑一条细看，建议优先看排在前面的高分项。
