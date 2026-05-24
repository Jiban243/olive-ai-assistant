import json
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def generate_infographic():
    # 1. Load data from the evaluation run
    results_path = "evaluation/results.json"
    if not os.path.exists(results_path):
        print(f"❌ Error: {results_path} not found. Run evaluate.py first!")
        return

    with open(results_path, "r") as f:
        data = json.load(f)

    # 2. Parse the scores into a flat format for processing
    parsed_scores = []
    for item in data:
        category = item["category"]
        parsed_scores.append({
            "Category": category,
            "Model": "Frontier Model (Groq)",
            "Score": item["frontier"]["score"]
        })
        parsed_scores.append({
            "Category": category,
            "Model": "Open Source (HF)",
            "Score": item["open_source"]["score"]
        })

    df = pd.DataFrame(parsed_scores)
    
    # Calculate average scores per category for quick numerical summary
    avg_scores = df.groupby(["Category", "Model"])["Score"].mean().unstack()
    print("\n📈 Calculated Average Metrics (Scale 1-5):")
    print(avg_scores)

    # 3. Initialize the Plot
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))

    # Set custom colors: Olive Green for Olive branding and Deep Grey for comparison
    colors = {"Frontier Model (Groq)": "#4A5D4E", "Open Source (HF)": "#8F9E8B"}

    ax = sns.barplot(
        x="Category", 
        y="Score", 
        hue="Model", 
        data=df, 
        palette=colors,
        errorbar=None,
        edgecolor="black"
    )

    # Styling and formatting adjustments
    plt.title("Olive Assistant Benchmark Evaluation: Frontier vs. Open Source", fontsize=14, fontweight="bold", pad=20)
    plt.xlabel("Evaluation Metric Categories", fontsize=12, fontweight="bold", labelpad=10)
    plt.ylabel("Judge Evaluation Score (1 - 5)", fontsize=12, fontweight="bold", labelpad=10)
    plt.ylim(0, 5.5)
    plt.legend(loc="upper right", frameon=True, facecolor="white", edgecolor="none")

    # Add score value labels on top of the bars
    for p in ax.patches:
        if p.get_height() > 0:
            ax.annotate(f"{p.get_height():.1f}", 
                        (p.get_x() + p.get_width() / 2., p.get_height() + 0.1), 
                        ha='center', va='center', 
                        fontsize=10, fontweight="bold", 
                        color='black', xytext=(0, 5), 
                        textcoords='offset points')

    plt.tight_layout()
    
    # Save chart image cleanly to our evaluation folder
    output_image = "evaluation/model_comparison_infographic.png"
    plt.savefig(output_image, dpi=300)
    print(f"\n🎨 Infographic saved successfully as an image asset at: {output_image}")

if __name__ == "__main__":
    generate_infographic()