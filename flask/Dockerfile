FROM python:3.9-slim

WORKDIR /app
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    rm -rf /var/lib/apt/lists/*
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# uwsgi.ini を利用してuWSGIを起動
CMD ["uwsgi", "--ini", "uwsgi.ini"]