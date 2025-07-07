# === data-pipeline/etl.py ===
import pandas as pd
import os

def run():
    url = "https://raw.githubusercontent.com/numenta/NAB/master/data/realKnownCause/ambient_temperature_system_failure.csv"
    df = pd.read_csv(url)

    os.makedirs("/data", exist_ok=True)
    df.to_csv("/data/time_series.csv", index=False)
    print("✅ ETL complete: /data/time_series.csv")

if __name__ == "__main__":
    run()
