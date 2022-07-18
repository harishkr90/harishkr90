FROM python:3.8.9

ENV MONGO_DB_USERNAME=admin \
    MONGO_DB_PWD=password

RUN mkdir -p /home/myfirstapp/src

WORKDIR /home/myfirstapp/src

# destination -> ./ if WORKDIR is set (else full path ex: /home/myfirstapp/src )
COPY requirements.txt .
COPY app.py ./

RUN pip3 install -r requirements.txt

CMD [ "python3", "app.py" ]
