FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-compile -r requirements.txt

COPY app ./app
EXPOSE 5000
CMD ["gunicorn", "--bind=0.0.0.0:5000", "app:app", "--chdir", "app", "--workers=2"]
