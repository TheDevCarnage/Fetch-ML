FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

WORKDIR /app/api

EXPOSE 8000

CMD ["uvicorn", "main:app", "--reload" ]
