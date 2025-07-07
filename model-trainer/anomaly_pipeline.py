# === model-trainer/anomaly_pipeline.py ===

import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
from sklearn.ensemble import IsolationForest
from sklearn.svm import OneClassSVM
from sklearn.preprocessing import StandardScaler
import joblib


class BaseAnomalyDetector:
    def __init__(self, model_name):
        self.model_name = model_name
        self.model = None
        self.scaler = StandardScaler()

    def preprocess(self, df):
        df['rolling_mean'] = df['value'].rolling(window=10).mean().fillna(method='bfill')
        df['rolling_std'] = df['value'].rolling(window=10).std().fillna(method='bfill')
        X = df[['value', 'rolling_mean', 'rolling_std']].values
        return self.scaler.fit_transform(X)

    def predict(self, X_scaled):
        preds = self.model.predict(X_scaled)
        return np.where(preds == -1, 1, 0)

    def fit_and_log(self, df):
        X_scaled = self.preprocess(df)

        with mlflow.start_run(run_name=self.model_name):
            self.model.fit(X_scaled)
            preds = self.predict(X_scaled)
            n_anomalies = int(np.sum(preds))

            mlflow.log_param("algorithm", self.model_name)
            mlflow.log_metric("n_anomalies", n_anomalies)
            mlflow.sklearn.log_model(self.model, artifact_path="model")

            if self.model_name == "IsolationForest":
                joblib.dump(self.model, "model.pkl")

            print(f"{self.model_name}: {n_anomalies} anomalies detected.")
            return preds


class IFDetector(BaseAnomalyDetector):
    def __init__(self):
        super().__init__("IsolationForest")
        self.model = IsolationForest(contamination=0.01, random_state=42)


class SVMDetector(BaseAnomalyDetector):
    def __init__(self):
        super().__init__("OneClassSVM")
        self.model = OneClassSVM(nu=0.01, kernel="rbf", gamma="scale")


class AnomalyDetectionPipeline:
    def __init__(self):
        self.detectors = [IFDetector(), SVMDetector()]

    def run(self, df):
        mlflow.set_experiment("Anomaly-Detection")
        for detector in self.detectors:
            detector.fit_and_log(df)
