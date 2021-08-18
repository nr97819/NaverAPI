FROM python:3

WORKDIR /app

ADD . /app

RUN python -m pip install --upgrade pip 
RUN pip install flask
RUN pip install flask-restx
RUN pip install googletrans==4.0.0-rc1
RUN pip install uwsgi


CMD ["uwsgi","uwsgi.ini"]