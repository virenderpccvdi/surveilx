FROM python:3.12-alpine

WORKDIR /app
COPY . /app

RUN pip install fastapi uvicorn python-telegram-bot smtplib

EXPOSE 9000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9000"]
