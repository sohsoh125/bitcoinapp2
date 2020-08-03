FROM ubuntu:16.04

RUN apt-get update && apt-get install -y openjdk-8-jdk wget
RUN wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add -
RUN echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | tee -a /etc/apt/sources.list.d/elastic-6.x.list
RUN apt-get install -y elasticsearch
RUN echo "network.host: 0.0.0.0" | tee -a /etc/elasticsearch/elasticsearch.yml
RUN systemctl start elasticsearch
RUN systemctl enable elasticsearch