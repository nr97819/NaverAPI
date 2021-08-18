FROM python:3.8

WORKDIR /app

ADD . /app

RUN pip install flask
RUN pip install uwsgi

RUN pip install googletrans==4.0.0-rc1

RUN pip install matplotlib
RUN pip install numpy
RUN pip install ruptures

RUN pip install wordcloud
RUN pip install pillow

RUN pip install datetime

RUN pip install requests
RUN pip install beautifulsoup4
RUN pip install pandas
RUN pip install openpyxl

CMD ["uwsgi","uwsgi.ini"]