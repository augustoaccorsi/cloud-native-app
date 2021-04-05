[![Build Status](https://travis-ci.com/augustoaccorsi/cloud-native-app.svg?branch=main)](https://travis-ci.com/augustoaccorsi/cloud-native-app)

# Cloud Native Application

Cloud Native Application Sample for the class of Software Architecture Unisinos

## How to run locally
  1. Install [Docker Desktop](https://docs.docker.com/get-docker/)
  2. Run the command ```docker-compose up --build``` to build the Docker images
  3. Run the Docker Container
  4. The service will be available on ```localholst:80```

## How to run on EB locally
  1. Install [EB cli](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install-advanced.html) with command ```pip install awsebcli --upgrade --user```
  2. Run the command ```eb local run```, the image will be available on Docker
  3. Run the Docker Container
  4. The service will be available on ```localholst:80```

## How to use
  1. Path ```localhost:5000``` students names
  1. Path ```localhost:5000/professor``` professor's name


