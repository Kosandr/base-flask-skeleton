FROM ubuntu:16.04
MAINTAINER Konstantin Kowalski <kostelkow@gmail.com>
RUN apt update; apt -y install wget; wget https://raw.githubusercontent.com/rpasta42-personal/myconfigs/master/install.sh; chmod u+x install.sh; sudo ./install.sh
RUN cd ~/orgs/Kosandr/base-flask/skeleton/setup; ./deps.py
