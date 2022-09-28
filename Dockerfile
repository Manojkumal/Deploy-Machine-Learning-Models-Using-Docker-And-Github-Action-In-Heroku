FROM ubuntu:20.04
FROM python:3.9
COPY . /app
WORKDIR /app
RUN apt-get update -y && \
    apt-get install -y python3-pip
RUN pip install -r requirements.txt
EXPOSE 8501 8501
CMD ["python3","api.py"]