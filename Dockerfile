FROM python:3.8-alpine

ENV HTTP_PORT=8080
ENV HOSTS=jvb

WORKDIR /usr/local/src/app/

ADD run.py /usr/local/src/app/
RUN chmod +x /usr/local/src/app/run.py

ADD requirements.txt /usr/local/src/app/
RUN pip install -r /usr/local/src/app/requirements.txt

EXPOSE ${HTTP_PORT}
CMD /usr/local/src/app/run.py