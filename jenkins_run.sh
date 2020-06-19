#! /bin/bash

docker container run -d \
    -p 2020:8080 \
    -v /home/robot/data_factory/jenkins_home:/var/jenkins_home \
    --name jenkins-local \
    jenkins/jenkins:lts