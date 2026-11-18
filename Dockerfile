FROM python:3.11.10-slim
WORKDIR /app
COPY books.py app.py books.json.example ./
ENV APP_PORT=8102
CMD ["python", "books.py", "--help"]
