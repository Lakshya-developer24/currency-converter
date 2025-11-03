FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV API_KEY=$API_KEY
EXPOSE 5000

CMD ["python", "app.py"]
