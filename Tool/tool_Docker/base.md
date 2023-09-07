# docker base

## 退出容器

```
# 退出容器后容器停止运行
exit 或 Ctrl+D

# 退出容器继续运行
win：Ctrl+p+q
mac：control+p+q
```

## 容器通讯问题

在容器内的服务或请求的host写为host.docker.internal，可访问宿主机的localhost或127.0.0.1

### 容器内访问宿主机:

- 1 在容器内直接 curl host.docker.internal:8866/exp
- 2 启动容器时 --add-host host.docker.internal:host-gateway， 在/etc/hosts下看host.docker.internal映射的host；
  在容器中curl 映射的host:8866/exp

### 宿主机访问容器