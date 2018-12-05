FROM centos:7


RUN yum -y update \
  && yum -y install vim curl wget git jq ipmitool 

RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm -y 

RUN yum -y install python36u python36u-pip python36u-devel openssl-devel openssl

WORKDIR /var/env/innkeeper2

RUN pip3.6 install flask==1.0.2 configparser==3.5.0 pymysql==0.8.1 gunicorn==19.8.1 flask_restplus==0.11.0

EXPOSE 5000

ENTRYPOINT ["gunicorn", "--config", "gunicorn.conf", "--log-config", "logging.conf", "-b", ":5000", "server:flaskapp"]
