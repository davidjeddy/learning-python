FROM python:latest

RUN apt-get update -y
RUN apt-get install -y htop nano vim
RUN python --version

# Change back to root of FS
WORKDIR /learn-python

# exec container
CMD ["tail", "-f", "/dev/null"]