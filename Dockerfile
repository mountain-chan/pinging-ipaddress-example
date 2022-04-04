FROM python:3.7
WORKDIR /pinging-ipaddress-example
ADD . /pinging-ipaddress-example
RUN pip install -r requirements.txt
# CMD python main.py