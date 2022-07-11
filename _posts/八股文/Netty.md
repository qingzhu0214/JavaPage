netty作用，自己的理解，组件
-   [Netty](https://www.nowcoder.com/jump/super-jump/word?word=Netty) 的线程模型

### [讲讲 Netty 的 Boss 和 worker 线程组？](https://www.modb.pro/db/175043)
1. MainReactor、SubReactor：主从Reactor线程，两者结构相似，功能不同。
	- MainReactor通过select监控建立连接事件，收到事件后通过Acceptor接收，处理建立连接事件，然后把建立好的连接分配给子线程SubReactor处理
	- SubReactor将连接加入连接队列进行监听，并创建一个Handler用于处理各种连接事件
1.  Acceptor：处理客户端连接请求
2. Handler：执行非阻塞读/写，read读取数据后，会分发给后面的Worker线程池进行业务处理
3. Worker：Worker线程池会分配独立的线程完成真正的业务处理，如何将响应结果发给Handler进行处理

Boss Group 对应的是 MainReactor 角色，Work Group 对应的是 SubReactor 角色

Boss Group 和 Work Group 都是 NioEventLoopGroup,  只是负责的分工不同。Boss Group 下的 EventLoop 处理 Accept 事件，Work Group 下的 EventLoop 处理 Read / Write 等事件