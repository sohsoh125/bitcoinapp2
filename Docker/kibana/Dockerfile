FROM ubuntu:16.04
MAINTAINER katoso<hmthmtgrnl@gmail.com>

# Installing supervisor and necessarious software
RUN apt-get update && apt-get install -y openjdk-8-jdk
RUN apt-get install -y wget
RUN apt-get install -y supervisor

# Making four directories for kitting supervisor
RUN mkdir -p /var/log/supervisor

# Copying configurator for supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Installing kibana
RUN apt-get install -y apt-transport-https
RUN wget https://artifacts.elastic.co/downloads/kibana/kibana-5.4.0-amd64.deb
RUN sha1sum kibana-5.4.0-amd64.deb 
RUN dpkg -i kibana-5.4.0-amd64.deb
RUN echo "server.host: 0.0.0.0" | tee -a /etc/kibana/kibana.yml

# Releasing ports
EXPOSE 5601

# Supervisor's binary file execute
CMD ["/usr/bin/supervisord"]