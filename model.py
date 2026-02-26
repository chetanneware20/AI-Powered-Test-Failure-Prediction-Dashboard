import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

def train_model(df):
    df = df.copy()

    # Convert Pass/Fail to binary
    df["last_run_status"] = df["last_run_status"].map({"Pass": 0, "Fail": 1})

    # Encode module
    le = LabelEncoder()
    df["module"] = le.fit_transform(df["module"])

    X = df[["module", "execution_time", "previous_failures", "build_number"]]
    y = df["last_run_status"]

    model = RandomForestClassifier()
    model.fit(X, y)

    return model, le
