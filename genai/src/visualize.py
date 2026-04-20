import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def visualize_results(csv_path: str = "results/experiment_log.csv"):
    if not os.path.exists(csv_path):
        print(f"File {csv_path} not found. Please run main.py first.")
        return

    df = pd.read_csv(csv_path)

    # Set up styling
    sns.set_theme(style="whitegrid")
    
    # 1. Bar Chart: Average Accuracy by Technique
    plt.figure(figsize=(8, 6))
    # We use hue to suppress the seaborn warning and palette to style.
    ax = sns.barplot(x="technique", y="accuracy", data=df, hue="technique", errorbar=None, palette="viridis", legend=False)
    plt.title("Average Accuracy: Standard vs ReAct Prompting", fontsize=14)
    plt.ylabel("Accuracy (0 or 1)", fontsize=12)
    plt.xlabel("Prompting Technique", fontsize=12)
    plt.ylim(0, 1.1)
    
    # Add values on top of bars
    for i in ax.containers:
        ax.bar_label(i, padding=3, fmt='%.2f')
        
    plt.tight_layout()
    plt.savefig("results/accuracy_comparison.png")
    print("Saved: results/accuracy_comparison.png")
    plt.show()

    # 2. Scatter Plot: Latency vs Reasoning Quality
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        data=df, 
        x="latency_sec", 
        y="reasoning_quality", 
        hue="technique", 
        style="technique",
        s=150, 
        alpha=0.8,
        palette="viridis"
    )
    
    plt.title("Latency vs. Reasoning Quality", fontsize=14)
    plt.xlabel("Latency (Seconds)", fontsize=12)
    plt.ylabel("Reasoning Quality (1-5)", fontsize=12)
    
    # Ensure y-axis covers 1 to 5
    plt.yticks(range(1, 6))
    
    plt.tight_layout()
    plt.savefig("results/latency_vs_reasoning.png")
    print("Saved: results/latency_vs_reasoning.png")
    plt.show()

if __name__ == "__main__":
    visualize_results()
