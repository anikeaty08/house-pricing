FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

COPY service.py .
COPY bentofile.yaml .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN bentoml build

EXPOSE 3000

CMD ["bentoml", "serve", "service:HousingPriceService", "--host", "0.0.0.0", "--port", "3000"]
