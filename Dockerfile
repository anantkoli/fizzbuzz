# base image
FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install software-properties-common -y
RUN apt-get install -y curl vim telnet libssl-dev wget libffi-dev
RUN apt-get --assume-yes install libsqlite3-dev python3-dev build-essential zlib1g-dev

RUN wget https://www.python.org/ftp/python/3.10.12/Python-3.10.12.tar.xz
RUN tar xvf Python-3.10.12.tar.xz
RUN ./Python-3.10.12/configure --enable-optimizations
RUN make altinstall

RUN pip3.10 install --upgrade pip==23.0.1
RUN pip3.10 install wheel setuptools

RUN rm -rf /var/www/fizzbuzz
COPY requirements.txt /var/www/fizzbuzz/
RUN pip3.10 install -r /var/www/fizzbuzz/requirements.txt
ADD . /var/www/fizzbuzz
WORKDIR /var/www/fizzbuzz
ENV PYTHONPATH $PYTHONPATH:/var/www/fizzbuzz
