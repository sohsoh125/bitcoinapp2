FROM ubuntu:16.04
MAINTAINER katoso<hmthmtgrnl@gmail.com>

# Installing supervisor and necessarious software
RUN apt-get update && apt-get install -y openjdk-8-jdk
RUN apt-get install -y wget
RUN apt-get install -y openssh-server apache2 supervisor

# Making four directories for kitting supervisor
RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/run/sshd /var/log/supervisor

# Copying configurator for supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Installing elasticsearch
RUN wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add -
RUN echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | tee -a /etc/apt/sources.list.d/elastic-6.x.list
RUN apt-get install -y elasticsearch
RUN echo "network.host: 0.0.0.0" | tee -a /etc/elasticsearch/elasticsearch.yml

# Releasing ports
EXPOSE 22 80 9200 9300

# Supervisor's binary file execute
CMD ["/usr/bin/supervisord"]