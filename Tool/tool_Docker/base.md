# docker

## 基础用法
### 退出容器

```
# 退出容器后容器停止运行
exit 或 Ctrl+D

# 退出容器继续运行
win：Ctrl+p+q
mac：control+p+q
```

### 容器通讯问题

在容器内的服务或请求的host写为host.docker.internal，可访问宿主机的localhost或127.0.0.1

#### 容器内访问宿主机:

- 1 在容器内直接 curl host.docker.internal:8866/exp
- 2 启动容器时 --add-host host.docker.internal:host-gateway， 在/etc/hosts下看host.docker.internal映射的host；
  在容器中curl 映射的host:8866/exp

#### 宿主机访问容器

## 常用指令
# docker
|功能|指令|其他|
|:-----|:-----|:-----|
|登录镜像仓库|docker login iregistry.baidu-int.com -u v_suchuncun -p Scc@123456  <br> docker login iregistry.baidu-int.com -u v_zhangyu42 -p Zhangyu970516||
|镜像包下载为镜像|docker load < {tar_archive_file_name_prefix}.tar.gz|
|镜像打包|docker save {image_tag} \|gzip > {tar_archive_file_name_prefix}.tar.gz|
|基于dockerfile构建镜像|docker build [--network host] -t {image_tag} -f {Dockerfile} .  <br> 例：docker build --network host -t pyml:300 -f py38.Dockerfile .||
|重命名tag|docker tag old{image_id} new{image_tag}|
|提交容器为镜像|docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]] <br> -a :提交的镜像作者；-c :使用Dockerfile指令来创建镜像；-m :提交时的说明文字；-p :在commit时，将容器暂停。|
|进入容器|docker exec -it container_id /bin/sh|
|删除生成缓存。文件|docker builder prune|
