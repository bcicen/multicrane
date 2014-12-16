#multicrane dockerfile
FROM python:2.7.8-onbuild

MAINTAINER Bradley Cicenas <bradley.cicenas@gmail.com>

ENV CRANEURL https://github.com/michaelsauter/crane/releases/download/v1.0.0/crane_linux_amd64

#install docker from latest
RUN apt-get -yqq update && apt-get -yq install apt-transport-https && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9 && \
    echo "deb https://get.docker.com/ubuntu docker main" > /etc/apt/sources.list.d/docker.list && \
    apt-get -yqq update && \
    apt-get -yq install lxc-docker && \
    apt-get clean

#install crane
RUN curl -sL $CRANEURL > /usr/local/bin/crane && \
    chmod +x /usr/local/bin/crane

#install multicrane
RUN chmod +x /usr/src/app/run.sh && \
    cd /usr/src/app && \
    python setup.py install 

ENTRYPOINT [ "/usr/src/app/run.sh" ]
