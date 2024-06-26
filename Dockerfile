FROM python:3.8.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV PORT=8000

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
