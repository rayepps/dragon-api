FROM python:3

WORKDIR /usr/src/dragon-api


ADD ./src/requirements.txt ./src/requirements.txt
RUN pip3 install -r src/requirements.txt

ADD ./test/requirements.txt ./test/requirements.txt
RUN pip3 install -r test/requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/usr/src/dragon-api"

ADD . .

CMD [ "python", "/usr/src/dragon-api/src/api.py" ]
