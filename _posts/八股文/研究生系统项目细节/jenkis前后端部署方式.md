### 学籍模块
git pull
mvn clean compile install
java -jar xxx.war直接运行

### 培养模块
检查端口，占用的就kill掉
mvn clean compile install
nohup mvn spring-boot:run -Pprod &

### 前端部署
- 把master分支的修改合并到production-xxb-k8s
- 合并完成后，将production-xxb-k8s推至远端
- 打上一个tag推送到远端 [参考：提tag自动打包](https://juejin.cn/post/6844903744681803789)
- 停止正在运行的容器，删除镜像
	- `docker stop $CONTAINER_ID`
	- `docker image rm`
- 上传镜像到私有仓库
	- 打包镜像
	- 上传镜像`docker tag express-app 111.111.111.111:5000/sunhengzhe/express-app:v1`
- docker pull最新的镜像
- 启动最新的镜像
	- `docker start`


使用docker build+Dockerfile构建jenkins镜像：
```shell
docker build -t donhui/jenkins .
```

dockerFile
```shell
FROM myregistry.com:5000/tomcat-cst
COPY dist /usr/local/tomcat/webapps/yjsy-ui
```

tomcat部署angular项目
将项目进行编译，再将编译后的文件放到tomcat的webapps目录下