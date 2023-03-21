FROM python:3.9

ENV FALCO_VERSION=0.34.1

RUN curl -L -o falco.tar.gz \
    https://download.falco.org/packages/bin/x86_64/falco-${FALCO_VERSION}-x86_64.tar.gz && \
    tar -xvf falco.tar.gz && \
    rm -f falco.tar.gz && \
    mv falco-${FALCO_VERSION}-x86_64 falco && \
    rm -rf /falco/usr/src/falco-* /falco/usr/bin/falco-driver-loader

ADD validate_sysdig_rules.py requirements.txt /

RUN pip3 install -r requirements.txt

RUN useradd -m app

WORKDIR /home/app

USER app

ENTRYPOINT ["python3", "/validate_sysdig_rules.py"]