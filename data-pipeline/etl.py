# === data-pipeline/etl.py ===
import pandas as pd

def run():
    df = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")
    df.to_csv("/data/iris.csv", index=False)
    print("ETL complete: /data/iris.csv")

if __name__ == "__main__":
    run()