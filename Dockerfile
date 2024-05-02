FROM python:3.11

WORKDIR /myapp

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY  mysite .

#EXPOSE 8000


CMD ["python3", "manage.py", "runserver"]


