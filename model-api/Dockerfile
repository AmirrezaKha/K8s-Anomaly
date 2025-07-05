FROM python:3.10
WORKDIR /app
COPY app.py .
COPY ../model-trainer/model.pkl ./
RUN pip install flask pandas scikit-learn
CMD ["python", "app.py"]