#!/bin/sh
if [ "${TRAVIS_BRANCH}" == "master" ]
then
    docker tag matoba/dncindocker:ci matoba/dncindocker:latest
    docker login -u="${DOCKER_USERNAME}" -p="${DOCKER_PASSWORD}"
    docker push matoba/dncindocker:latest
    wget https://hyper-install.s3.amazonaws.com/hyper-linux-x86_64.tar.gz
    tar xzf hyper-linux-x86_64.tar.gz
    mv -f docker-compose.hyper.yml docker-compose.yml
    cat docker-compose.yml
    ./hyper config --accesskey ${HYPER_ACCESS} --secretkey ${HYPER_KEY}
    ./hyper compose down -p cdcc
    ./hyper compose up -d -p cdcc
fi