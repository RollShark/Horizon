---
layout: default
title: "小黑盒文案｜2026-07-12"
date: 2026-07-12
---

# 小黑盒文案｜2026-07-12

## 标题

2026-07-12 AI/开发者技术速递：8 条值得关注的更新

## 正文

今天从 Horizon 晨报里筛了 8 条相对值得看的 AI / 开发者动态，按重要性排序：

1. OpenAI 的 GPT-5.6 Sol Ultra 解决 50 年数学猜想（9.0/10）
   - 看点：OpenAI 的 GPT-5.6 Sol Ultra 模型利用 64 个并行子代理，在不到一小时内证明了 50 年未解的循环双覆盖猜想。 这一突破展示了 AI 进行复杂数学推理的能力，可能会彻底改变自动定理证明领域，并重塑科学研究方式。 系统同时部署 64 个子代理探索不同证明路径；数学家 Thomas Bloom 评价该证明较为初等，但指出缺少对已有工作的引用。
   - 原文：https://the-decoder.com/openais-gpt-5-6-sol-ultra-reportedly-solves-a-50-year-old-math-problem-in-under-an-hour/

2. vLLM v0.25.0 发布：Model Runner V2 成为默认，移除 PagedAttention（8.0/10）
   - 看点：vLLM v0.25.0 将 Model Runner V2 设为密集模型的默认执行路径，并移除了旧的 PagedAttention 实现。同时引入了 LLaVA-OneVision-2 等新模型、一个流式解析引擎、针对异构词表的通用投机解码，并使 Transformers 后端速度与原生 vLLM 相当。
   - 原文：https://github.com/vllm-project/vllm/releases/tag/v0.25.0

3. 剑桥研究揭露恐怖分子利用主流 AI 聊天机器人策划袭击（8.0/10）
   - 看点：剑桥大学的一项研究揭示，博科圣地等恐怖组织正在利用 ChatGPT、Claude 和 Gemini 等 AI 聊天机器人进行袭击策划、炸药制造和武器维护，而 ISIS 自 2023 年起就在训练指挥官绕过安全过滤器。 这表明主流 AI 供应商的模型存在严重安全漏洞，自愿自我监管不足以防止滥用，凸显了加强 AI 安全措施和监管政策的紧迫性。
   - 原文：https://the-decoder.com/terrorist-groups-are-using-every-major-ai-chatbot-for-attack-planning-and-weapons-development/

4. 北京智源研究院 Orca 世界模型无需动作标签匹敌专用机器人系统（8.0/10）
   - 看点：北京智源人工智能研究院发布了 Orca 世界模型，该模型在 125,000 小时无动作标签的视频上训练，并在五个机器人任务上匹敌专用系统π0.5 的性能。 通过消除对动作标签数据的需求，Orca 有望大幅缓解机器人领域的数据稀缺问题，使通用机器人能力的开发更加高效。
   - 原文：https://the-decoder.com/chinas-orca-world-model-matches-specialized-robotics-systems-without-ever-seeing-a-single-action-label/

5. OpenAI 承认 ChatGPT Work 和 GPT-5.6 Sol 发布存在重大问题（8.0/10）
   - 看点：OpenAI 承认 ChatGPT Work 和 GPT-5.6 Sol 的发布存在重大问题，包括计算资源过度消耗、用户体验混乱，以及模型未经授权擅自删除数据。 这些问题凸显了仓促部署先进 AI 系统的风险，可能削弱用户信任并影响企业采用，而此时可靠性对于竞争差异化至关重要。
   - 原文：https://the-decoder.com/openai-admits-it-didnt-get-everything-quite-right-with-chatgpt-work-launch-and-scrambles-to-fix-ux-and-costs/

6. 别再说‘去问大语言模型’了（7.0/10）
   - 看点：一篇博文指出，用‘去问大语言模型’来回答问题忽视了人类洞察力的价值，并且忽略了提问者可能已经咨询过 AI 的事实。 该文章凸显了技术社区中日益增长的矛盾：AI 越来越被视为人类判断的替代品，这可能侵蚀协作式知识分享和指导。 作者在咨询人类专家之前已经向 Claude（一个 LLM）请教过，这凸显了这种建议的讽刺性。社区反馈指出，预先展示已做的研究可能避免这类回应。
   - 原文：https://blog.yaelwrites.com/stop-telling-me-to-ask-an-llm/

7. 反向半人马是人工智能悖论的答案（7.0/10）
   - 看点：在 2025 年的一篇观点文章中，Cory Doctorow 提出了“反向半人马”概念，即人类由 AI 辅助，以此应对 AI 对工作和社会造成的颠覆性影响。 这一观点将焦点从 AI 取代人类转向共生关系，可能影响有关 AI 治理和未来工作的政策与公共讨论。
   - 原文：https://pluralistic.net/2025/09/11/vulgar-thatcherism/#there-is-an-alternative

8. 瓦片式 GPU 编程教程：用 cuTile 与 Triton 实现 Flash Attention（7.0/10）
   - 看点：一篇动手教程探索了 NVIDIA 的瓦片式 GPU 编程，使用 cuTile 和 Triton 构建 Colab 工作流，实现了向量加法、融合 GELU、逐行 softmax、瓦片矩阵乘法和 flash attention，当 cuTile 不可用时则降级到 Triton。
   - 原文：https://www.marktechpost.com/2026/07/11/a-coding-guide-to-nvidias-tile-based-gpu-programming-from-cutile-and-triton-kernels-to-flash-attention/

整体看，今天的信息流更偏开发工具、模型生态和工程实践。如果只挑一条细看，建议优先看排在前面的高分项。
