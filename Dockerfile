FROM python:3.11-slim-buster

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--workers", "2", "--host", "0.0.0.0", "--port" ,"${PORT:-5000}"]
