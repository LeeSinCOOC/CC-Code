## Docker 使用笔记
###中文手册：
https://docker_practice.gitee.io/zh-cn/install/ubuntu.html

### 删除镜像：
```shell
docker image ls
docker image rm [] # 需要注意是否有容器在占用镜像，如果有无法删除
```

### 删除容器：
```shell
docker ps -a
docker rm []
```

### 修改Docker本地镜像与容器的存储位置的方法
1.软连接
```shell
mv /var/lib/docker /root/data/docker
ln -s /root/data/docker /var/lib/docker
```  
2.配置文件
Ubuntu 中的位置是：`/etc/default/docker`如果是 Ubuntu 则添加下面这行（因为 Ubuntu 默认没开启 selinux）：
```
OPTIONS=--graph="/root/data/docker" -H fd://
# 或者
DOCKER_OPTS="-g /root/data/docker"
```

### 停容器：
```shell
docker stop [name]
```

### 容器部署：
```shell
docker-compose up -d
```

### 新建容器：
```shell
docker run -it -p 6000:6000 --shm-size 4G -v [宿主机绝对路径]:[容器路径] --privileged=true --gpus all --name [容器名] [镜像名] /bin/bash
-u root 增加容器内权限
nvidia-docker run -it -p 6000:6000 --shm-size 4G -v  [宿主机绝对路径]:[容器路径] --name [容器名] [镜像名] /bin/bash
```

### 启动容器：
```shell
docker start containername
```

### 进入容器：
```shell
docker exec -it containername /bin/bash
```

### 修改 Docker 的默认存储路径：
`vi /etc/docker/daemon.json`
```
{
  "registry-mirrors": ["http://hub-mirror.c.163.com"],
  "data-root": "/www/docker"
}
```

### Docker改镜像位置：
1. 停服务
```shell
service docker stop
service docker restart
```
2. 改位置
```shell
mv /var/lib/docker /root/data/docker
ln -s /root/data/docker /var/lib/docker
```
3. 重加载
```shell
systemctl daemon-reload
systemctl start docker
```
4.检查位置
```shell
docker info
```

### 容器换源：
```shell
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
echo deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse >> /etc/apt/sources.list
```

### 保存镜像：
```shell
docker commit a589933536b1[容器ID] cmii-bodypose-0913[镜像名称]
docker save -o mynetcore.tar mynetcore:v1
docker load < rocketmq.tar
```

### 查看日志：
```shell
docker logs [OPTIONS] CONTAINER
  -f : 跟踪日志输出
  --since :显示某个开始时间的所有日志
  -t : 显示时间戳
  --tail :仅列出最新N条容器日志
```

### 查看映射docker容器的路径：
```shell
docker inspect code | grep Mount -A 20
```
### 改源
```
{
  "registry-mirrors": [
    "https://dockerhub.icu",
    "https://docker.anyhub.us.kg",
    "https://dockerhub.jobcher.com",
    "https://dockerhub.icu",
    "https://docker.ckyl.me",
    "https://docker.awsl9527.ch"
  ],
  "runtimes": {
    "nvidia": {
      "path": "nvidia-container-runtime",
      "runtimeArgs": []
    }
  }
}
```
