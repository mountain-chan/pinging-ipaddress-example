FROM python:3.7
WORKDIR /pinging_ipaddress
ADD . /pinging_ipaddress
#RUN pip install -r requirements.txt
# CMD python main.py