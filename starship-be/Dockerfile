FROM python:3.7.3

COPY start.sh /
COPY requirements.txt /

RUN chmod +x ./start.sh

RUN pip install -r requirements.txt && \
    git clone https://github.com/jasonwer/starfleet.git

ENTRYPOINT ./start.sh
