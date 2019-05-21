FROM python:3

COPY llen.py ./
COPY queue.json ./

RUN pip install prometheus_client
RUN pip install redis

EXPOSE 8000

ENTRYPOINT ["python", "./llen.py"]
