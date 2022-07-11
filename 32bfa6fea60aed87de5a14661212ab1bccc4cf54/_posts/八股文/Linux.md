linux中线程的状态
Linux内核了解吗 
硬链接与软连接
常用的Linux指令
select, poll, epoll：IO多路复用
epoll算是同步模型么？


### Linux线程切换怎么实现？

## Linux基本命令（进程、日志、打包、解压等等）

### [Linux命令中的grep](https://segmentfault.com/a/1190000022722655)
grep 命令在所给文件中查找特定模式的字符串，可以提供多个文件名，在多个文件中查找。如果没有提供文件名，则读取标准输入。

“| grep”中的“|”是什么意思？

如果确实需要用 grep 命令来查找字符串，可以用管道操作符 | 来连接标准输入。例如用 echo 命令打印字符串的值，然后通过管道操作符把这个值传递到 grep 命令的标准输入。

```shell
echo "This is a test string." | grep string
```

### select, poll, epoll
[参考](https://www.jianshu.com/p/dfd940e7fca2)
I/O多路复用就是通过一种机制，一个进程可以监视多个描述符，一旦某个描述符就绪（一般是读就绪或者写就绪），能够通知程序进行相应的读写操作。但select，pselect，poll，epoll本质上都是同步I/O，因为他们都需要在读写事件就绪后自己负责进行读写，也就是说这个读写过程是阻塞的，而异步I/O则无需自己负责进行读写，异步I/O的实现会负责把数据从内核拷贝到用户空间。

select本质上是通过设置或者检查存放fd标志位的数据结构来进行下一步处理。这样所带来的缺点是：
1. select最大的缺陷就是单个进程所打开的FD是有一定限制的，它由FD_SETSIZE设置，默认值是1024。
2. 对socket进行扫描时是线性扫描，即采用轮询的方法，效率较低。
3. 需要维护一个用来存放大量fd的数据结构，这样会使得用户空间和内核空间在传递该结构时复制开销大。

poll本质上和select没有区别，它将用户传入的数组拷贝到内核空间，然后查询每个fd对应的设备状态，如果设备就绪则在设备等待队列中加入一项并继续遍历，如果遍历完所有fd后没有发现就绪设备，则挂起当前进程，直到设备就绪或者主动超时，被唤醒后它又要再次遍历fd。这个过程经历了多次无谓的遍历。

它没有最大连接数的限制，原因是它是基于链表来存储的，但是同样有一个缺点：
1. 大量的fd的数组被整体复制于用户态和内核地址空间之间，而不管这样的复制是不是有意义。
2. poll还有一个特点是“水平触发”，如果报告了fd后，没有被处理，那么下次poll时会再次报告该fd。

epoll使用一个文件描述符管理多个描述符，将用户关系的文件描述符的事件存放到内核的一个事件表中，这样在用户空间和内核空间的copy只需一次。

epoll支持水平触发和边缘触发，最大的特点在于边缘触发，它只告诉进程哪些fd刚刚变为就绪态，并且只会通知一次。还有一个特点是，epoll使用“事件”的就绪通知方式，通过epoll_ctl注册fd，一旦该fd就绪，内核就会采用类似callback的回调机制来激活该fd，epoll_wait便可以收到通知。

### Linux Socket
一个完整的Socket的组成应该是由【协议，本地地址，本地端口，远程地址，远程端口】组成的一个5维数组。

服务器首先启动，通过调用socket()建立一个套接字，然后调用bind()将该套接字和本地网络地址联系在一起，再调用listen()使套接字做好侦听的准备，并规定它的请求队列的长度，之后就调用accept()来接收连接。客户端在建立套接字后就可调用connect()和服务器建立连接。连接一旦建立，客户机和服务器之间就可以通过调用read()和write()来发送和接收数据。最后，待数据传送结束后，双方调用close()关闭套接字。

### LINUX查看进程的4种方法
- ps aux
- ps -elf
- top：以全屏交互式的界面显示进程排名，及时跟踪包括CPU、内存等系统资源占用情况，默认情况下每三秒刷新一次，其作用基本类似于Windows系统中的任务管理器。
- pstree -aup：以树状图的方式展现进程之间的派生关系，显示效果比较直观。

**两个具有相同名称不同路径的程序启动的进程，要kill一个，怎样知道要kill哪一个？**
查询指定路径下的进程：ps aux | grep 指定路径
根据进程 id 杀掉指定进程：kill -9 指定进程号

### 线程在Linux怎么实现？

### 项目部署在Linux服务器时有哪些常用命令？
```shell
# 到指定目录
cd 
# 源目录，目标目录
mv   /tmp/Test.jar  /opt/nspring
mkdir

# 将aaa目录及其子级的 读、写、执行 权限 开放给所有用户
chmod -R 777 aaa

# 查询进程信息
ps -ef | grep java 

# 杀进程
kill -9 20996
```

文件管理：ls、cd、touch创建普通文件、rm删除、mkdir新建目录、mv移动、cp拷贝、chmod修改权限；
进程管理：ps显示进程信息、kill杀死进程；
系统管理：top、free显示系统运行信息、vmstat输出各资源使用情况；
网络通讯：ping测试网络连通性、netstat显示网络相关信息；

### Linux命令怎么查看端口的占用情况
[参考](https://www.runoob.com/w3cnote/linux-check-port-usage.html)
lsof(list open files)是一个列出当前系统打开文件的工具。
lsof -i:端口号

netstat -tunlp 用于显示 tcp，udp 的端口和进程等相关情况。
netstat -tunlp | grep 端口号

### linux通过什么命令查看日志
[参考](https://cloud.tencent.com/developer/article/1579977)
- tail  -n  10   test.log   查询日志尾部最后10行的日志;
- tail -fn 1000 test.log | grep '关键字'
- head -n  10  test.log   查询日志文件中的头10行日志;
- cat filename
- sed -n '5,10p' filename 这样你就可以只查看文件的第5行到第10行。

### 查看cpu大小和内存大小的命令？
CPU配置信息：cat /proc/cpuinfo
查看内存大小：free  默认以字节为单位，如果需要以兆为单位，可以使用free -m


