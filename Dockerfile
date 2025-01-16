FROM python:3.12-slim
RUN apt-get update && apt-get install -y postgresql-client && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN mkdir /library_patres
WORKDIR /library_patres
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN chmod a+x /library_patres/docker/*.sh
