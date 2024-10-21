FROM python:3.9-alpine

WORKDIR /srv
#复制代码到镜像环境中
COPY . /srv   
#更换软件源成国内的
RUN sed -i "s#dl-cdn.alpinelinux.org#mirrors.aliyun.com#g"  /etc/apk/repositories
#下载make工具环境
RUN apk add --no-cache make
