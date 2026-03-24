import pandas as pd

def preprocess_data():
    df = pd.read_csv("data/sample_data.csv")

    # Handle missing values
    df.fillna(method='ffill', inplace=True)

    # Convert data types
    df["Sleep"] = df["Sleep"].astype(float)
    df["ScreenTime"] = df["ScreenTime"].astype(float)
    df["Hydration"] = df["Hydration"].astype(float)
    df["PhysicalActivity"] = df["PhysicalActivity"].astype(float)

    return df