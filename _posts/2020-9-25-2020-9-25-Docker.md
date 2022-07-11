了解docker镜像吗
了解docker网络吗
了解k8s吗
docker打包

### Docker复制命令
```
docker cp b80f4b3ad86a:/root/Neptune/docs ~/
```
将`b80f4b3ad86a`docker中的`docs`文件夹复制到宿主机的`home`目录下

### CMD和ENTERPOINT的区别
作为开发者, 你希望在docker镜像启动后, 自动运行其他程序。所以, 你需要用CMD或者ENTRYPOINT命令显式地指定具体的命令。

- RUN命令执行命令并创建新的镜像层，通常用于安装软件包
- CMD命令设置容器启动后默认执行的命令及其参数，但CMD设置的命令能够被docker run命令后面的命令行参数替换
- ENTRYPOINT用于设置容器启动时要执行的命令及其参数
