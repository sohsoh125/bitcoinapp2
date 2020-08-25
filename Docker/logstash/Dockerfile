FROM ubuntu:16.04
MAINTAINER katoso<hmthmtgrnl@gmail.com>

# Installing supervisor and necessarious software
RUN apt-get update && apt-get install -y openjdk-8-jdk
RUN apt-get install -y wget
RUN apt-get install -y supervisor

# Making directory for kitting supervisor
RUN mkdir -p /var/log/supervisor

# Copying configurator for supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Installing logstash
RUN apt-get install -y apt-transport-https
RUN wget https://artifacts.elastic.co/downloads/logstash/logstash-5.4.0.deb
RUN dpkg -i logstash-5.4.0.deb

# Releasing ports
EXPOSE 5044

# Supervisor's binary file execute
CMD ["/usr/bin/supervisord"]