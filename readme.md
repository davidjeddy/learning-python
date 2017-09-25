# Learning Python

# Requirements

[Docker](https://www.docker.com/)

# Setup

    docker build --tag dje/learnpython:latest ./
    docker run -i -t -v `pwd`:/learn-python dje/learnpython:latest /bin/bash

To run a python script

    pything ./{path to script}/{file name}.py

Collect [Bacon](https://en.wikipedia.org/wiki/Bacon)
