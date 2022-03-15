
FROM python:3.8

ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["python3", "manage.py runserver"]
