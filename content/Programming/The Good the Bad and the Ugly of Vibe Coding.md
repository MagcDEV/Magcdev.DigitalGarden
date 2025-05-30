---
title: The Good the Bad and the Ugly
draft: false
tags: []
---
"Vibe coding" is definitely having a moment. Everyone seems to be talking about it, and as usual, when everyone's talking, a lot of them don't *really* know what they're talking about. That's why I decided to dive in and try this AI-assisted coding approach myself. Here's what I learned navigating the hype.

### 1. One-Shot Wonders? Not for Big Projects (Yet)

My first attempt involved using Copilot in agent mode to build an entire Angular front-end from a single prompt. Let's just say it failed... spectacularly. The AI kept getting tangled up in the routing and file structure. To be fair, this wasn't a trivial "Hello World" app; it was a complex beast with numerous components and services. Plus, Angular itself is a robust framework designed for larger applications, which likely added to the challenge. The dream of generating a full app in one go remains, for now, mostly a dream for substantial projects.

### 2. AI Shines with Bite-Sized Code Generation

Okay, so the grand, one-prompt plan flopped. I shifted gears and started generating the app piece by piece – component by component, service by service. The results? *Much* better. The AI was impressively consistent and helpful when generating smaller, well-defined code blocks. However, this approach requires patience. You have to guide the AI step-by-step, constantly verifying that it's sticking to the rules and requirements you've set. Which brings me to my next point...

### 3. Context Isn't Just King, It's Everything

To get quality results from coding AI, providing clear, unambiguous context is crucial. You can stuff context into every single prompt, but that gets tedious and inefficient fast. A much better approach is to provide persistent context. For GitHub Copilot, you can use the `.github/copilot-instructions.md` file ([GitHub Docs](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot)). This file lets you add short, self-contained statements that guide Copilot's behavior for your repository.

For instance, I created a mini style guide for my Angular project in this file, specifying preferences like using modern Angular features (version 17+) and other coding conventions. You can see my example [here](https://github.com/MagcDEV/BreakManager/blob/master/.github/copilot-instructions.md). This is similar to using system or contextual prompting techniques discussed in prompt engineering. Providing examples (few-shot prompting) can also significantly steer the AI toward your desired output style and structure.

### Final Thoughts

Overall, my "vibe coding" journey has been pretty incredible. While I wouldn't call myself an Angular expert (especially given my stronger background in C#/.NET, as you mentioned before), these AI tools, specifically Gemini 1.5 Pro in my recent work, have made tackling this complex front-end project feel achievable. It's not magic, and it requires a different way of working, but the potential to accelerate development, especially in less familiar territory, is undeniable. It's less about vibes and more about smart, contextual prompting.