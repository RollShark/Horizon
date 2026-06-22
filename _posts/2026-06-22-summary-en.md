---
layout: default
title: "Horizon Summary: 2026-06-22 (EN)"
date: 2026-06-22
lang: en
---

> From 23 items, 13 important content pieces were selected

---

1. [Codex logging bug may write TBs to local SSDs](#item-1) ⭐️ 8.0/10
2. [Did My Old Job Only Exist Because of Fraud?](#item-2) ⭐️ 8.0/10
3. [Logarithms Are Everywhere in Math and Science](#item-3) ⭐️ 8.0/10
4. [Deno Desktop Enables Desktop Apps with Shared Runtime](#item-4) ⭐️ 7.0/10
5. [Apertus: Open Foundation Model for Sovereign AI](#item-5) ⭐️ 7.0/10
6. [Minimal Downside to Switching to Open-Weight LLMs](#item-6) ⭐️ 7.0/10
7. [sqlite-utils 4.0rc1 adds migrations and nested transactions](#item-7) ⭐️ 7.0/10
8. [Cloudflare Launches Temporary Workers Deployments](#item-8) ⭐️ 7.0/10
9. [Update on Matrix Recurrent Units: Addressing Training Stability](#item-9) ⭐️ 7.0/10
10. [GLM 5.2 vs Opus: One-Shot Prompting Sparks Debate](#item-10) ⭐️ 6.0/10
11. [Fine-Tuning Qwen 0.6B for Question Categorization](#item-11) ⭐️ 6.0/10
12. [Best Methods for Fine-Tuning Whisper on Domain-Specific Spanish Vocabulary](#item-12) ⭐️ 6.0/10
13. [EMA on LoRA for Self-Distillation: Query](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Codex logging bug may write TBs to local SSDs](https://github.com/openai/codex/issues/28224) ⭐️ 8.0/10

A logging bug in OpenAI's Codex CLI causes excessive writes to a local SQLite database, potentially writing up to 640 TB per year and wearing out SSDs within months. Community members have shared a SQLite trigger workaround and noted that running VACUUM FULL can shrink the log file from 27 GB to 73 MB. This bug poses a serious hardware risk for developers using Codex, as excessive writes can permanently damage SSDs. It also highlights quality issues in widely-used AI coding tools, eroding user trust and prompting community-driven workarounds. The bug is tracked on GitHub as issue #17320 and remains open. The excessive writes stem from TRACE logs that ignore the RUST_LOG environment variable, causing all log entries to be written to a SQLite database. A temporary fix involves creating a SQLite trigger to block log inserts.

hackernews · vantareed · Jun 22, 07:30 · [Discussion](https://news.ycombinator.com/item?id=48626930)

**Background**: Codex is OpenAI's AI coding assistant that runs locally via CLI or desktop app. It uses SQLite for logging, and a misconfigured logging sink can write massive amounts of data. SSDs have limited write endurance, typically measured in total terabytes written (TBW); consumer drives often have a TBW of 150-600 TB.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/openai/codex/issues/17320">Excessive SQLite WAL writes during streaming due to TRACE logs ignoring RUST_LOG · Issue #17320 · openai/codex</a></li>
<li><a href="https://www.notebookcheck.net/OpenAI-Codex-has-a-bug-that-could-kill-your-SSD-in-under-a-year.1326191.0.html">OpenAI Codex has a bug that could kill your SSD in under a year - Notebookcheck News</a></li>
<li><a href="https://smartscope.blog/en/generative-ai/chatgpt/codex-cli-diagnostic-logs-deep-dive/">Codex CLI Logs: Location, Debug Flags & 401 Error Fix (2026) - SmartScope</a></li>

</ul>
</details>

**Discussion**: Community sentiment is largely critical of OpenAI, with users calling Codex 'slopware' and reporting high GPU usage even when idle. Some users appreciate the open-source nature of Codex, noting it can be patched, while others compare it unfavorably to Claude Code in terms of typing latency.

**Tags**: `#OpenAI`, `#Codex`, `#bug`, `#SSD`, `#logging`

---

<a id="item-2"></a>
## [Did My Old Job Only Exist Because of Fraud?](https://david.newgas.net/did-my-old-job-only-exist-because-of-fraud/) ⭐️ 8.0/10

A personal essay and community discussion explore how systemic fraud in billing, government contracts, and outsourcing may inflate tech job counts, with commenters sharing firsthand experiences of fraudulent billing and contractor schemes. This raises critical questions about the true health of the tech job market and the integrity of government spending, potentially affecting how workers, investors, and policymakers assess employment data and contract oversight. Commenters describe specific schemes: a manager editing billing entries to inflate hours on a government project, and a contractor being rehired through an outsourcing firm at a markup without changing the actual work.

hackernews · advisedwang · Jun 21, 21:40 · [Discussion](https://news.ycombinator.com/item?id=48622867)

**Background**: Government contract fraud includes overbilling, billing for work not performed, and kickback schemes. Outsourcing often involves third-party firms that add markup while supplying the same workers. Such practices can artificially inflate demand for tech labor and distort job market statistics.

<details><summary>References</summary>
<ul>
<li><a href="https://constantinecannon.com/practice/whistleblower/whistleblower-types/government-contract-fraud/">Government Contractor Fraud | Whistleblower Law Firm</a></li>
<li><a href="https://rm-firm.com/legal-blog/government-procurement-fraud/">10 Examples of Government Procurement Fraud | Reese Marketos LLP</a></li>
<li><a href="https://fedpractice.com/practice-areas/government-contracts/government-contract-procurement-fraud-false-claims-act/">Government Contract Procurement Fraud and False Claims Act</a></li>

</ul>
</details>

**Discussion**: The community strongly agrees that fraud is widespread, with multiple commenters sharing personal anecdotes of billing fraud, contractor markup schemes, and government funding being funneled to large companies instead of startups. Some express cynicism about the tech industry's reliance on such practices.

**Tags**: `#fraud`, `#government contracting`, `#tech industry`, `#outsourcing`, `#billing practices`

---

<a id="item-3"></a>
## [Logarithms Are Everywhere in Math and Science](https://alexkritchevsky.com/2026/05/25/everything-is-logarithms.html) ⭐️ 8.0/10

An essay titled 'Everything is logarithms' argues that logarithms are fundamental to understanding ratios, scales, and information across many domains, from mathematics to computer science. This perspective highlights the unifying role of logarithms in diverse fields, potentially changing how we teach and think about mathematical concepts and their applications. The essay explores logarithms in contexts such as information theory (bits, nats, digits), complex analysis, and historical calculation methods using log tables.

hackernews · E-Reverance · Jun 21, 21:10 · [Discussion](https://news.ycombinator.com/item?id=48622626)

**Background**: A logarithm is the inverse operation of exponentiation, answering how many times one number must be multiplied by itself to get another number. They are used to simplify multiplication into addition, and to represent ratios and scales in science and engineering.

**Discussion**: Commenters discuss the concept of torsors in relation to baseless logarithms, historical use of log tables, and the need for a type system to specify the base and domain of logarithms. Some recommend further reading on the lost art of logarithms and Lie theory.

**Tags**: `#mathematics`, `#logarithms`, `#computer science`, `#information theory`

---

<a id="item-4"></a>
## [Deno Desktop Enables Desktop Apps with Shared Runtime](https://docs.deno.com/runtime/desktop/) ⭐️ 7.0/10

Deno Desktop has been released, allowing developers to build desktop applications using Deno with backends such as CEF and Webview, and plans to reduce binary sizes through a shared runtime. This expands Deno's utility beyond server-side and CLI applications into desktop development, offering a lighter alternative to Electron by potentially reducing app sizes to a few megabytes per app. Deno Desktop supports CEF (Chromium Embedded Framework) and Webview backends, with a raw backend also available. The shared runtime feature is on the roadmap to avoid bundling a full browser engine per app.

hackernews · GeneralMaximus · Jun 22, 05:38 · [Discussion](https://news.ycombinator.com/item?id=48626137)

**Background**: CEF is an open-source framework for embedding Chromium-based browsers in applications, while Webview is a lightweight library that uses the operating system's native web engine (WebKit on macOS/Linux, Edge WebView2 on Windows). Deno is a JavaScript/TypeScript runtime built on V8, known for its security and modern features.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chromium_Embedded_Framework">Chromium Embedded Framework - Wikipedia</a></li>
<li><a href="https://github.com/webview/webview">GitHub - webview/webview: Tiny cross-platform webview library for C/C++. Uses WebKit (GTK/Cocoa) and Edge WebView2 (Windows). · GitHub</a></li>

</ul>
</details>

**Discussion**: Community sentiment is mixed: some users dislike JavaScript desktop apps, while others appreciate the shared runtime approach and Deno's permission system. There is interest in a 'launch in browser' option and questions about CEF versioning with shared runtimes.

**Tags**: `#deno`, `#desktop`, `#javascript`, `#cef`, `#webview`

---

<a id="item-5"></a>
## [Apertus: Open Foundation Model for Sovereign AI](https://apertvs.ai/) ⭐️ 7.0/10

Apertus is a fully open foundation model project designed for sovereign AI, aiming to comply with the EU AI Act by respecting opt-outs, removing PII, and preventing memorization. This project addresses the growing need for AI sovereignty outside the US, offering a transparent and compliant alternative for organizations that want to control their data and models. Apertus V1 performance was sub-par, and the team is currently working on V2. The instruct models are based on Llama 3.1 fine-tunes from last year, raising questions about competitiveness.

hackernews · T-A · Jun 21, 21:29 · [Discussion](https://news.ycombinator.com/item?id=48622778)

**Background**: Sovereign AI refers to a state's ability to design, host, operate, and regulate AI systems within its territory, including data storage and model training. Open foundation models like Apertus aim to provide transparency and control, contrasting with proprietary models from US tech giants.

<details><summary>References</summary>
<ul>
<li><a href="https://apertvs.ai/?trk=article-ssr-frontend-pulse_little-text-block">Fully Open Foundation Model for Sovereign AI</a></li>
<li><a href="https://news.ycombinator.com/item?id=48622778">Apertus – Open Foundation Model for Sovereign AI | Hacker News</a></li>
<li><a href="https://www.linkedin.com/pulse/sovereign-ai-new-geopolitical-fault-line-boards-cant-ignore-palande-mzy4c">Sovereign AI : The New Geopolitical Fault Line Boards Can’t Ignore</a></li>

</ul>
</details>

**Discussion**: Community feedback is mixed: some appreciate the sovereignty goal but criticize slow progress and sub-par performance, while others note that the team lacks experience compared to established LLM providers. Comparisons to other open models like OLMo and Nemotron highlight Apertus's current limitations.

**Tags**: `#open-source`, `#AI`, `#foundation model`, `#sovereign AI`, `#LLM`

---

<a id="item-6"></a>
## [Minimal Downside to Switching to Open-Weight LLMs](https://www.marble.onl/posts/cancel_claude.html) ⭐️ 7.0/10

A blog post argues that open-weight large language models (LLMs) are a viable alternative to proprietary models with minimal trade-offs, citing cost savings, privacy benefits, and near-parity in capability. This debate is significant because it challenges the prevailing assumption that proprietary models like GPT-4 and Claude are necessary for high-quality AI applications, potentially accelerating adoption of open models in privacy-sensitive and cost-conscious environments. The post acknowledges that open-weight models may be a few months behind proprietary ones, but argues that for many use cases, this lag is acceptable. It also notes that open models can be run locally or via third-party services, though privacy concerns vary by provider.

hackernews · amarble · Jun 21, 20:56 · [Discussion](https://news.ycombinator.com/item?id=48622518)

**Background**: Open-weight LLMs make their pre-trained weights publicly available, allowing anyone to use, fine-tune, or deploy them. This contrasts with proprietary models like GPT-4 and Claude, which are only accessible via API and whose weights remain secret. The open-source vs. proprietary AI debate has intensified as open models have improved rapidly, narrowing the capability gap.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/open-weights-llms-in-depth-analysis-adoption-usage-performance-jha-kymhc">Open - Weights LLMs: In-Depth Analysis of Adoption, Usage, and...</a></li>
<li><a href="https://newsletter.himanshuramchandani.co/p/proprietary-vs-open-source-ai-trap-that-s-bankrupting-startups">Proprietary vs Open - Source AI Trap That's Bankrupting Startups</a></li>
<li><a href="https://www.sunqi.org/open-source-vs-proprietary-2025.html">Open Source vs Proprietary : How to Think About the Trade -off in 2025</a></li>

</ul>
</details>

**Discussion**: Commenters raised nuanced points: some questioned the true openness of open-weight models, noting that users cannot modify the underlying matrices. Others highlighted that privacy depends on the service provider, with some recommending eurouter.ai for better data protection. A few argued that the capability lag is negligible for many tasks, especially those that were using older proprietary models.

**Tags**: `#open source`, `#LLM`, `#AI`, `#privacy`, `#machine learning`

---

<a id="item-7"></a>
## [sqlite-utils 4.0rc1 adds migrations and nested transactions](https://simonwillison.net/2026/Jun/21/sqlite-utils-40rc1/#atom-everything) ⭐️ 7.0/10

sqlite-utils 4.0rc1 introduces built-in database migrations and nested transaction support via db.atomic(). This major update simplifies database schema management for Python developers and enables safer, more flexible transaction handling in SQLite. Migrations are defined as Python functions using the @migrations() decorator and can be applied via CLI or Python API. Nested transactions are implemented using SQLite savepoints.

rss · Simon Willison · Jun 21, 23:35

**Background**: sqlite-utils is a Python library and CLI tool that provides high-level operations on SQLite databases. Previously, schema changes had to be managed manually or with external tools like sqlite-migrate, which is now integrated into the core library.

<details><summary>References</summary>
<ul>
<li><a href="https://sqlite-utils.datasette.io/en/latest/migrations.html">Database migrations - sqlite - utils</a></li>
<li><a href="https://simonwillison.net/2026/Jun/21/sqlite-utils-40rc1/">sqlite - utils 4.0rc1 adds migrations and nested transactions</a></li>

</ul>
</details>

**Tags**: `#sqlite`, `#python`, `#database`, `#migrations`, `#open-source`

---

<a id="item-8"></a>
## [Cloudflare Launches Temporary Workers Deployments](https://simonwillison.net/2026/Jun/21/temporary-cloudflare-accounts/#atom-everything) ⭐️ 7.0/10

Cloudflare now allows users to deploy a Workers project for 60 minutes without creating an account, using the command `npx wrangler deploy --temporary`. This lowers the barrier to trying Cloudflare Workers, making serverless deployment accessible to anyone with a terminal, including AI agents and casual developers. The temporary deployment is ephemeral and lasts exactly 60 minutes, after which it is automatically removed. Users can claim the project via a provided URL to extend its lifetime.

rss · Simon Willison · Jun 21, 22:01

**Background**: Cloudflare Workers is a serverless edge computing platform that runs JavaScript on Cloudflare's global CDN. Wrangler is the official CLI tool for managing Workers projects. Previously, deploying a Worker required creating a Cloudflare account and configuring a project.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.cloudflare.com/workers/wrangler/commands/">Commands - Wrangler · Cloudflare Workers docs</a></li>
<li><a href="https://www.npmjs.com/package/wrangler">wrangler - npm</a></li>

</ul>
</details>

**Tags**: `#Cloudflare`, `#serverless`, `#deployment`, `#developer tools`

---

<a id="item-9"></a>
## [Update on Matrix Recurrent Units: Addressing Training Stability](https://www.reddit.com/r/MachineLearning/comments/1ubz5o8/an_update_on_matrix_recurrent_units_an_attention/) ⭐️ 7.0/10

The author reports progress on Matrix Recurrent Units (MRU), a linear-time attention alternative, by experimenting with new input state matrix methods (skew-symmetric, LDU, QR) to bound matrix states and stabilize training on larger datasets. This work addresses a key limitation of MRUs—training instability—potentially making them more viable for efficient sequence modeling, which is critical for scaling transformers and exploring alternatives to attention. The author found that orthogonal input state matrices (via Cayley map or matrix exponential) performed poorly, suggesting shear transformations are critical, while LDU factorization gave the best results. On the TinyStories dataset, MRU underperformed a baseline GPT-2.

reddit · r/MachineLearning · /u/mikayahlevi · Jun 21, 19:39

**Background**: Matrix Recurrent Units (MRUs) are a linear-time sequence architecture that replaces attention with cumulative matrix multiplication across the sequence. They use a parallel associative scan for efficiency on modern hardware. Training instability on larger datasets has been a known issue, which the author attempts to fix by constraining the input state matrices.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@sparklerussell/gated-recurrent-units-explained-with-matrices-part-2-training-and-loss-function-7e7147b7f2ae">Gated Recurrent Units explained with matrices : Part... | Medium</a></li>
<li><a href="https://vitalab.github.io/article/2018/09/27/kronecker-recurrent-units.html">Kronecker Recurrent Units</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#sequence modeling`, `#attention alternative`, `#recurrent neural networks`, `#linear-time architecture`

---

<a id="item-10"></a>
## [GLM 5.2 vs Opus: One-Shot Prompting Sparks Debate](https://techstackups.com/comparisons/glm-5.2-vs-opus/) ⭐️ 6.0/10

A comparison article pitted GLM 5.2 against Claude Opus 4.8 using a single one-shot prompt to build a 3D platformer in raw WebGL, sparking community criticism for unrealistic methodology. The debate highlights the need for more realistic benchmarks that reflect collaborative, multi-step AI usage rather than simplistic one-shot prompts. The one-shot prompt asked the models to build a 3D platformer from scratch without any game engine or library, which critics argue does not represent real-world software development workflows.

hackernews · ritzaco · Jun 22, 07:22 · [Discussion](https://news.ycombinator.com/item?id=48626866)

**Background**: GLM 5.2 is a large language model by Zhipu AI with a 1-million-token context window, while Claude Opus is Anthropic's high-capability tier. One-shot prompting uses a single input to generate a complete output, which is often insufficient for complex tasks like game development.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.z.ai/guides/llm/glm-5.2">GLM - 5 . 2 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://felloai.com/glm-5-2/">What Is GLM 5 . 2 ? Zhipu's 1M-Context Open Model | Fello AI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude ( AI ) - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters criticized the one-shot approach as unrealistic, with one noting that real agent usage is collaborative and requires reliability and steerability. Another suggested using Opus to plan and GLM to execute for a best-of-both-worlds approach.

**Tags**: `#AI`, `#LLM`, `#benchmark`, `#coding`

---

<a id="item-11"></a>
## [Fine-Tuning Qwen 0.6B for Question Categorization](https://www.teachmecoolstuff.com/viewarticle/fine-tuning-a-local-llm-to-categorize-questions) ⭐️ 6.0/10

A practical guide demonstrates fine-tuning the small language model Qwen 3:0.6B to categorize user questions, achieving effective classification with a local, lightweight model. This approach enables on-device text classification without relying on large cloud APIs, making it suitable for privacy-sensitive or offline applications. It also highlights the growing trend of using small, specialized models for specific tasks. The fine-tuning process uses Qwen 3:0.6B, a 0.6-billion-parameter model, and the article provides hands-on steps for training it on a custom question categorization dataset. Community comments suggest that simpler classifiers like scikit-learn's SGDClassifier may achieve comparable results with far less resource overhead.

hackernews · dev-experiments · Jun 21, 22:55 · [Discussion](https://news.ycombinator.com/item?id=48623434)

**Background**: Fine-tuning adapts a pre-trained language model to a specific task by training it on a small, task-specific dataset. Small language models (SLMs) like Qwen 0.6B are designed to run on edge devices, offering a balance between performance and efficiency. Text classification is a common NLP task where models assign predefined categories to text inputs.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3-0.6B">Qwen / Qwen 3 - 0 . 6 B · Hugging Face</a></li>
<li><a href="https://openlaboratory.ai/models/qwen3-0_6b">Qwen 3 0 . 6 B | Open Laboratory</a></li>
<li><a href="https://medium.com/@liana.napalkova/fine-tuning-small-language-models-practical-recommendations-68f32b0535ca">Fine - Tuning Small Language Models : Practical... | Medium</a></li>

</ul>
</details>

**Discussion**: Commenters debate the necessity of fine-tuning an LLM for simple classification, with some advocating for traditional ML classifiers like scikit-learn's SGDClassifier or ModernBERT plus a classifier. Others suggest exploring zero-shot encoders, GRPO training, or using embedding models with a separate classifier. The discussion reflects a healthy skepticism about over-engineering simple tasks.

**Tags**: `#fine-tuning`, `#small language models`, `#text classification`, `#practical ML`

---

<a id="item-12"></a>
## [Best Methods for Fine-Tuning Whisper on Domain-Specific Spanish Vocabulary](https://www.reddit.com/r/MachineLearning/comments/1ubvmdx/best_current_methods_for_finetuning_whisper_on/) ⭐️ 6.0/10

A Reddit user asked the community for the best current methods and data requirements for fine-tuning OpenAI's Whisper model on domain-specific Spanish vocabulary, mentioning techniques like LoRA, QLoRA, and Spectrum. Domain-specific fine-tuning of Whisper is crucial for applications like medical or legal transcription where accuracy on specialized terms is essential. The discussion helps practitioners identify efficient methods and estimate data needs. The user specifically works with Spanish technical terms and asks about newer methods beyond LoRA, QLoRA, and Spectrum. They also inquire about the amount of labeled audio hours needed for convergence.

reddit · r/MachineLearning · /u/gothenjoyer_ · Jun 21, 17:18

**Background**: Whisper is a general-purpose speech recognition model from OpenAI that performs well on many languages but may struggle with domain-specific vocabulary. Fine-tuning adapts the model to specialized domains using labeled audio. LoRA and QLoRA are parameter-efficient fine-tuning techniques that reduce memory and compute requirements, while Spectrum is another adaptation method.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@chris.xg.wang/a-guide-to-fine-tune-whisper-model-with-hyper-parameter-tuning-c13645ba2dba">Whisper Precision: A Comprehensive Guide to Fine - Tuning ... | Medium</a></li>
<li><a href="https://huggingface.co/blog/fine-tune-whisper">Fine - Tune Whisper For Multilingual ASR with Transformers</a></li>
<li><a href="https://github.com/Vaibhavs10/fast-whisper-finetuning">GitHub - Vaibhavs10/fast- whisper - finetuning · GitHub</a></li>

</ul>
</details>

**Tags**: `#Whisper`, `#fine-tuning`, `#domain adaptation`, `#speech recognition`, `#Spanish`

---

<a id="item-13"></a>
## [EMA on LoRA for Self-Distillation: Query](https://www.reddit.com/r/MachineLearning/comments/1ubv0f5/ema_on_lora_r/) ⭐️ 6.0/10

A Reddit user asks if there are papers that successfully apply Exponential Moving Average (EMA) on LoRA adapters for self-distillation, where the EMA adapter acts as a self-teacher generating soft labels for the trainable adapter. This question highlights a gap in parameter-efficient fine-tuning research: combining EMA-based self-distillation with LoRA could improve performance without full fine-tuning, benefiting resource-constrained practitioners. The user references the paper 'On-Policy Self-Distillation' (arXiv:2601.19897) which uses EMA for the teacher but with full fine-tuning, and seeks empirical results specifically for LoRA or left models.

reddit · r/MachineLearning · /u/South-Conference-395 · Jun 21, 16:54

**Background**: LoRA (Low-Rank Adaptation) is a parameter-efficient fine-tuning method that adds small trainable matrices to a frozen pre-trained model, reducing memory and storage costs. EMA is a technique that maintains a moving average of model parameters, often used to stabilize training or as a teacher in self-distillation. Self-distillation uses a teacher model (often an EMA of the student) to generate soft labels for the student to learn from.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/low-rank-adaptation-lora-adapters">LoRA Adapters : Efficient Fine-Tuning</a></li>
<li><a href="https://www.ibm.com/think/topics/lora">What is LoRA (Low-Rank Adaption)? | IBM</a></li>

</ul>
</details>

**Tags**: `#LoRA`, `#EMA`, `#self-distillation`, `#fine-tuning`, `#parameter-efficient`

---