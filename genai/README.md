# Standard vs. ReAct Prompting Framework

This framework compares Standard Prompting against the ReAct (Reasoning and Acting) prompting pattern using multi-hop reasoning questions. It measures accuracy, reasoning quality, hallucination likelihood, and calculates latency and token usage.

## Architecture

* `data_loader.py` - Ingests the JSON dataset containing multi-hop questions.
* `mock_tools.py` - Provides a deterministic Wikipedia mock integration to simulate an external ReAct tool safely.
* `prompts.py` - Contains system instructions for the LLM agents (Standard and ReAct configurations).
* `llm_handler.py` - Routes API calls and orchestrates the ReAct loop (with a hard cap of `max_iterations=3` to prevent infinite token loops).
* `evaluator.py` - Employs the "LLM-as-a-judge" pattern to score AI outputs blindly.
* `main.py` - Dispatches questions to both methodologies, evaluates the outputs, and logs execution to a pandas DataFrame.
* `visualize.py` - Consumes the runtime telemetry to create visualizations comparing Standard vs ReAct performance metrics.

## Setup Instructions

1. **Install dependencies**
   Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API Keys**
   We use the OpenAI SDK. Create your `.env` file by copying the template:
   ```bash
   cp .env.example .env
   ```
   Open the `.env` file and replace the placeholder with your actual `OPENAI_API_KEY`.

3. **Run the Experiment**
   Execute the framework via `main.py`:
   ```bash
   python main.py
   ```
   The framework will loop over all questions in `data/sample_questions.json`, execute standard queries, and execute the ReAct reasoning loops. All telemetry will be saved to `results/experiment_log.csv`.

4. **Visualize Results**
   Once the experiment is complete, generate visual reports metrics:
   ```bash
   python src/visualize.py
   ```
   * Expect outputs like `accuracy_comparison.png` and `latency_vs_reasoning.png` populated in the `results/` folder.
