# ReAct Prompting vs Standard Prompting: An Experimental Study for Knowledge-Intensive Tasks

## 📌 Overview

This repository contains the experimental framework, datasets, prompts, and evaluation results for a comparative study between **ReAct Prompting** (Reasoning + Acting) and **Standard Prompting** (few-shot or zero-shot) in the context of **knowledge-intensive tasks** using Large Language Models (LLMs).

The goal of this project is to systematically evaluate whether prompting a model to *reason step-by-step* and *interact with external tools* (ReAct) yields better factual accuracy, logical coherence, and task completion compared to standard prompting methods, especially when the required knowledge is not fully contained in the model’s parametric memory.

## 🧠 Background

### Standard Prompting
- Relies on the LLM’s internal knowledge.
- May produce hallucinations or incomplete answers for knowledge-intensive queries.
- Examples: zero-shot, few-shot, chain-of-thought (CoT) without tool use.

### ReAct Prompting
- Interleaves **Reasoning** (thought traces) and **Acting** (tool use like search, calculator, or API calls).
- Enables the model to retrieve external knowledge dynamically.
- Reduces hallucinations and improves verifiability.

## 🎯 Research Questions

1. Does ReAct prompting improve answer accuracy over standard prompting for knowledge-intensive tasks?
2. How does the reasoning trace quality differ between ReAct and standard CoT?
3. What is the trade-off between inference cost (tokens/time) and performance gain?
4. In which task categories (e.g., multi-hop QA, fact verification, temporal reasoning) does ReAct excel or fail?

## 🧪 Experimental Setup

### Tasks (Knowledge-Intensive)
| Task | Description | Example |
|------|-------------|---------|
| Multi-hop QA | Requires combining facts from multiple sources | “Who was the president when the Berlin Wall fell?” |
| Fact Verification | Check claim against known knowledge | “Einstein won a Nobel Prize in Chemistry.” |
| Temporal Reasoning | Events across time | “Was the Model T invented before the first iPhone?” |
| Counterfactual QA | Contradicts common knowledge | “If water boiled at 50°C, what would happen?” |

### Models Tested
- GPT-3.5 / GPT-4 (OpenAI)
- Llama 3 (70B)
- Claude 3 Haiku / Sonnet
- (Optional) Mistral 7B

### Prompting Strategies
- **Standard Zero-shot**  
  `Q: ... A:`
- **Standard Few-shot (3-shot)**  
  Examples provided
- **Chain-of-Thought (CoT)**  
  `Let’s think step by step.`
- **ReAct (Reasoning + Acting)**  
  Interleaved `Thought → Action → Observation` loops

### Tools for ReAct
- Wikipedia search API
- Web search (DuckDuckGo)
- Calculator
- Datetime lookup

## 📊 Evaluation Metrics

| Metric | Description |
|--------|-------------|
| **Exact Match (EM)** | For QA tasks |
| **Factual Accuracy** | Human or LLM-as-judge evaluation |
| **Reasoning Plausibility** | Logical consistency of thought trace |
| **Tool Call Efficiency** | Number of unnecessary tool calls |
| **Token Cost** | Input + output tokens |
| **Latency** | Time to final answer |
