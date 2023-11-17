FROM python:alpine

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python3","-m","flask", "--app=app","run","--host=0.0.0.0"]