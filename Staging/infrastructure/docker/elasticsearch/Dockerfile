FROM ubuntu:16.04
MAINTAINER katoaoi<hmthmtgrnl@gmail.com>

RUN apt-get update && apt-get install -y openjdk-8-jdk
RUN apt-get install -y wget
RUN apt-get install -y openssh-server apache2 supervisor

RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/run/sshd /var/log/supervisor

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add -
RUN echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | tee -a /etc/apt/sources.list.d/elastic-6.x.list
RUN apt-get install -y elasticsearch
RUN echo "network.host: 0.0.0.0" | tee -a /etc/elasticsearch/elasticsearch.yml

EXPOSE 22 80
CMD ["/usr/bin/supervisord"]