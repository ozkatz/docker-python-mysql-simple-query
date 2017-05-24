FROM python:2.7

RUN apt-get update && apt-get install -y python-dev libmysqlclient-dev
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY simple-query.py .

CMD /usr/local/bin/python simple-query.py
