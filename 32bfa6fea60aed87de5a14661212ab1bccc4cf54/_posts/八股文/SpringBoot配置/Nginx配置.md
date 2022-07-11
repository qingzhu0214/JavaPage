[下载安装](https://www.cnblogs.com/minutes/p/12596635.html)

```
nginx.exe -s stop 关闭Nginx（快速停止nginx，可能并不保存相关信息）  
nginx.exe -s quit 关闭Nginx（完整有序的停止nginx，保存相关信息）  
nginx.exe -s reload 重新加载Nginx
```

配置文件：
```
# 配置请求转发，对外暴露9001端口，如果url路径有snowflake则转发到8095端口，url路径有/api/data-rule/则转发到8094端口
server {
	# 监听端口号
    listen       9001;
	# 主机名称
    server_name  localhost;

	# ~表示使用正则匹配
    location ~ /snowflake/ {
		proxy_pass http://localhost:8095;
    }

    location ~ /api/data-rule/ {
		proxy_pass http://localhost:8094;
    }
 }
```

[Spring配合Nginx实现文件下载](https://www.jianshu.com/p/514581593684)

[spring boot 三两行代码实现文件的上传和下载](https://www.jianshu.com/p/5a8287aebc8f)

[root和alias区别](https://www.cnblogs.com/ruiy/p/12581600.html)

路径重写的例子：
```
#将/info/22/yellowcong/717350389@11.com 转化为 /info?age=12&name=yellowcon&email=717350389
#[0-9]表示 0-9 范围i 数字 也可以使用\d+
#+ 表示1个或多个
#w+ 表示是字符串
#$ 表示结尾 
rewrite ^/info/([0-9]+)\/(\w+)\/(\w+)$ /info?age=$1&name=$2&email=$3 ;
break;
```