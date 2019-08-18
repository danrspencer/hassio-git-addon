ARG BUILD_FROM
FROM $BUILD_FROM

RUN apk add --no-cache git openssh-client gcc python3 python3-dev libc-dev libffi-dev openssl-dev
RUN pip3 install --upgrade pip pyyaml pyjson

COPY run.py /opt
RUN chmod a+x /opt/run.py

RUN mkdir ~/.ssh
COPY ./ssh/config ~/.ssh/config


WORKDIR /opt

CMD /opt/run.py