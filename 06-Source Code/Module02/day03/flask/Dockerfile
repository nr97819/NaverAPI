FROM python:3.8

WORKDIR /app

ADD . /app

RUN pip install flask
RUN pip install googletrans==4.0.0-rc1
RUN pip install uwsgi


CMD ["uwsgi","uwsgi.ini"]