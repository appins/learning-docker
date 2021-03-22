FROM python:3.6-alpine

COPY ./requirements.txt /var/www/requirements.txt
RUN pip3 install -r /var/www/requirements.txt

WORKDIR /usr/src/app
COPY . .

CMD python ./main.py
