FROM python:3.11-alpine

WORKDIR /app

RUN apk add nginx bash
COPY requirements.txt requirements.txt
RUN pip install gunicorn
RUN pip install -r requirements.txt

COPY nginx/default.conf /etc/nginx/http.d/default.conf
COPY entrypoint.sh .
COPY app.py .

EXPOSE 8000

ENTRYPOINT /app/entrypoint.sh
