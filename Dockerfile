FROM python:3.5-alpine

RUN pip install prometheus_client requests

ENV BIND_PORT 9189

ADD src /app
WORKDIR /app

CMD ["python", "gandi_exporter.py"]
