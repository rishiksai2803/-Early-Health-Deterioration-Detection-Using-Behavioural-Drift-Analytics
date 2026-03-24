import matplotlib.pyplot as plt
import seaborn as sns

def perform_eda(df):
    print("\n--- EDA SUMMARY ---\n")
    print(df.describe())

    # Correlation heatmap
    plt.figure(figsize=(6,4))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.show()

    # Distribution plots
    df.hist(figsize=(8,6))
    plt.suptitle("Feature Distributions")
    plt.show()