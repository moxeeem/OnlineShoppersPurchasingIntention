FROM python:3.10-slim-buster

RUN pip install explainerdashboard
RUN pip install dill

COPY dashboard.py ./
COPY app.py ./

RUN python dashboard.py

EXPOSE 5678
CMD ["python", "./app.py"]
