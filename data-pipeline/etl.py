# === data-pipeline/etl.py ===
import pandas as pd
import os

def run():
    url = "https://raw.githubusercontent.com/numenta/NAB/master/data/realKnownCause/ambient_temperature_system_failure.csv"
    df = pd.read_csv(url)

    output_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, "time_series.csv")
    df.to_csv(output_file, index=False)

    print(f"✅ ETL complete: {output_file}")

if __name__ == "__main__":
    run()
