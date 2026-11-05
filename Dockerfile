
FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

RUN useradd --create-home appuser

USER appuser

EXPOSE 5000

ENV APP_VERSION=v1.0.0

CMD ["python", "app.py"]
