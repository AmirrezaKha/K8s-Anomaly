# === model-trainer/main.py ===
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_pipeline import etl
from anomaly_pipeline import AnomalyDetectionPipeline

if __name__ == "__main__":
    etl.run()
    df = pd.read_csv("/data/time_series.csv")

    if 'value' not in df.columns:
        raise ValueError("Expected 'value' column in dataset.")
    df = df[['value']]

    pipeline = AnomalyDetectionPipeline()
    pipeline.run(df)
