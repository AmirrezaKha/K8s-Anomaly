FROM python:3.10
WORKDIR /app
COPY train.py .
RUN pip install pandas scikit-learn
CMD ["python", "train.py"]
