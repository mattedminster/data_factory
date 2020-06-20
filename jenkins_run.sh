#! /bin/bash

docker run -d \
    -p 2020:8080 \
    -v /home/robot/data_factory/jenkins_home:/var/jenkins_home \
    -v /usr/bin/docker:/usr/bin/docker \
    -v /var/run/docker.sock:/var/run/docker.sock:rw \
    --privileged \
    jenkins/jenkins:lts