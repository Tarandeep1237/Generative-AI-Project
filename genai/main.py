import os
import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from src.data_loader import load_questions
from src.llm_handler import LLMHandler
from src.evaluator import Evaluator

def main():
    print("Loading data...")
    questions = load_questions("data/sample_questions.json")
    
    if not questions:
        print("No questions loaded. Exiting.")
        return

    gen_model = os.getenv("MODEL_GENERATOR", "gpt-4o-mini")
    eval_model = os.getenv("MODEL_EVALUATOR", "gpt-4o")
    
    try:
        handler = LLMHandler(model_name=gen_model)
        evaluator = Evaluator(model_name=eval_model)
    except Exception as e:
        print(f"Initialization error: {e}")
        print("Please configure your .env file with a valid OPENAI_API_KEY.")
        return

    results = []
    
    print(f"Starting evaluations on {len(questions)} questions...")
    for q_idx, q in enumerate(questions):
        print(f"Processing Q{q_idx+1}: {q['id']}")
        
        # 1. Standard Prompting
        print("  Running Standard Prompting...")
        std_result = handler.run_standard(q['question'])
        std_eval = evaluator.evaluate(q['question'], q['expected_answer'], std_result['final_answer'])
        
        results.append({
            "id": q["id"],
            "question": q["question"],
            "technique": "Standard",
            "iterations": std_result["iterations"],
            "total_tokens": std_result["total_tokens"],
            "latency_sec": std_result["latency_sec"],
            "final_answer": std_result["final_answer"],
            "raw_output": std_result["raw_output"],
            "accuracy": std_eval["accuracy"],
            "reasoning_quality": std_eval["reasoning_quality"],
            "hallucination_present": std_eval["hallucination_present"]
        })
        
        # 2. ReAct Prompting
        print("  Running ReAct Prompting...")
        react_result = handler.run_react(q['question'])
        react_eval = evaluator.evaluate(q['question'], q['expected_answer'], react_result['raw_output'])
        
        results.append({
            "id": q["id"],
            "question": q["question"],
            "technique": "ReAct",
            "iterations": react_result["iterations"],
            "total_tokens": react_result["total_tokens"],
            "latency_sec": react_result["latency_sec"],
            "final_answer": react_result["final_answer"],
            "raw_output": react_result["raw_output"],
            "accuracy": react_eval["accuracy"],
            "reasoning_quality": react_eval["reasoning_quality"],
            "hallucination_present": react_eval["hallucination_present"]
        })

    # Save Results
    os.makedirs("results", exist_ok=True)
    df = pd.DataFrame(results)
    
    csv_path = "results/experiment_log.csv"
    df.to_csv(csv_path, index=False)
    print(f"\nEvaluation Complete. Saved results to {csv_path}")

    print("\n--- EXPERIMENT SUMMARY ---")
    # Display the essential columns so it can be viewed then and there
    print(df[['id', 'technique', 'accuracy', 'reasoning_quality', 'latency_sec']].to_string(index=False))
    print("\n")

if __name__ == "__main__":
    main()
