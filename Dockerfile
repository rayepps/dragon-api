FROM python:3

WORKDIR /usr/src/dragon

ADD . .

RUN pip3 install -r src/requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/usr/src/dragon"

CMD [ "python", "dragon/api.py" ]
