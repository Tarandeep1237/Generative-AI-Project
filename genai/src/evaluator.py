import os
import json
from openai import OpenAI
from typing import Dict, Any

EVALUATOR_PROMPT = """You are an expert evaluator. I will provide you with a question, the expected correct answer, and an AI model's output.
Your task is to evaluate the model's output based on three criteria:
1. Accuracy: Does the model's final answer correctly match the meaning of the expected answer? (1 for Yes, 0 for No).
2. Reasoning Quality: Rate the logical reasoning on a scale of 1-5 (1 = no reasoning/hallucination, 5 = perfect logical steps). Standard prompts with no reasoning should get a 1.
3. Hallucination: Did the model hallucinate false facts during its thought process or final answer? (True for Yes, False for No).

Provide your evaluation strictly as a JSON object with keys "accuracy" (int), "reasoning_quality" (int), and "hallucination_present" (boolean).
Do not output anything other than the JSON object.

Question: {question}
Expected Answer: {expected_answer}
Model Output: {model_output}
"""

class Evaluator:
    def __init__(self, model_name: str = "gpt-4o"):
        api_key = os.getenv("OPENAI_API_KEY")
        self.mock_mode = False
        if not api_key or api_key.startswith("sk-proj-..."):
            print("[Warning] No valid OpenAI key found. Running Evaluator in MOCK mode.")
            self.mock_mode = True
        else:
            self.client = OpenAI(api_key=api_key)
        self.model_name = model_name

    def evaluate(self, question: str, expected_answer: str, model_output: str) -> Dict[str, Any]:
        """Evaluates the model output against the expected answer using an LLM as a judge."""
        if getattr(self, "mock_mode", False):
            import random
            is_correct = expected_answer.lower() in model_output.lower()
            return {
                "accuracy": 1 if is_correct else 0,
                "reasoning_quality": random.randint(4, 5) if is_correct else random.randint(1, 2),
                "hallucination_present": not is_correct
            }

        prompt = EVALUATOR_PROMPT.format(
            question=question,
            expected_answer=expected_answer,
            model_output=model_output
        )

        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0,
                response_format={ "type": "json_object" }
            )
            result_str = response.choices[0].message.content.strip()
            result_json = json.loads(result_str)
            return {
                "accuracy": int(result_json.get("accuracy", 0)),
                "reasoning_quality": int(result_json.get("reasoning_quality", 1)),
                "hallucination_present": bool(result_json.get("hallucination_present", False))
            }
        except Exception as e:
            print(f"Error evaluating: {e}")
            return {
                "accuracy": 0,
                "reasoning_quality": 1,
                "hallucination_present": True
            }
