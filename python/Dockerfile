FROM python:3.9-alpine

WORKDIR /srv
# 将source code拷贝至容器
COPY . /srv   
# 更新source mirror
RUN sed -i "s#dl-cdn.alpinelinux.org#mirrors.aliyun.com#g"  /etc/apk/repositories
# 更新make
RUN apk add --no-cache make
# 更新容器环境时间为本地时间
ENV TZ=Asia/Shanghai
