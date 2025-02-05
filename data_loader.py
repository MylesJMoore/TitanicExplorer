import pandas as pd

# Load the dataset
def load_data():
    df = pd.read_csv("data/titanic.csv")
    return df

# Perform basic analysis
def analyze_data(df):
    summary = df.describe()  # Summary statistics
    survival_rate = df["Survived"].mean() * 100  # Survival percentage
    return summary, survival_rate

if __name__ == "__main__":
    df = load_data()
    summary, survival_rate = analyze_data(df)

    print("Dataset Summary:")
    print(summary)
    print(f"\nSurvival Rate: {survival_rate:.2f}%")