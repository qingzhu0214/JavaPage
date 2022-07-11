## Redis安装
安装docker下的redis：
```
docker run -itd --name redis -p 6379:6379 redis
```

执行以下命令看安装是否成功：
```
➜ docker exec -it redis redis-cli 
127.0.0.1:6379> ping
PONG
```

## 缓存配置
[参考](https://segmentfault.com/a/1190000039341264)
 jedis和lettuce简单比较(lettuce为下文的commons-pool2依赖)：
- Jedis在实现上是直接连接Redis服务器，在多个线程间共享一个Jedis 实例时是线程不安全的，如果想要在多线程场景下使用Jedis，需要使用连接池，每个线程都使用自己的Jedis实例，当连接数量增多时，会消耗较多的物理资源。
- 与Jedis相比，lettuce 则完全克服了其线程不安全的缺点：lettuce 是一个可伸缩的线程安全的 Redis客户端，支持同步、异步和响应式模式。多个线程可以共享一个连接实例， 而不必担心多线程并发问题。它基于优秀Netty NIO框架构建，支持Redis的更多高级功能。

增加依赖项：
```xml
<dependencies>
	<dependency>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-data-redis</artifactId>
	</dependency>

	<dependency>
		<groupId>org.apache.commons</groupId>
		<artifactId>commons-pool2</artifactId>
	</dependency>
</dependencies>
```

application.properties文件中添加
```
spring.redis.host=127.0.0.1
spring.redis.port=6379
#客户端超时
spring.redis.timeout=10000
#最大连接数
spring.redis.lettuce.pool.max-active=20
#最小空闲
spring.redis.lettuce.pool.min-idle=5
#连接超时
spring.redis.lettuce.pool.max-wait=5000ms
#最大空闲
spring.redis.lettuce.pool.max-idle=20
```

启动类添加注解`@EnableCaching`
```java
@SpringBootApplication
@EnableCaching
public class RedisdemoApplication {
    public static void main(String[] args) {
        SpringApplication.run(RedisdemoApplication.class, args);
    }
}
```

编写配置类：
```java
@Configuration
public class RedisConfig {

    @Bean
    RedisTemplate<String, Object> redisTemplate(RedisConnectionFactory redisConnectionFactory) {
        RedisTemplate<String, Object> redisTemplate = new RedisTemplate<>();
        redisTemplate.setConnectionFactory(redisConnectionFactory);
        redisTemplate.setValueSerializer(new GenericJackson2JsonRedisSerializer());
        redisTemplate.setKeySerializer(new StringRedisSerializer());
        redisTemplate.setHashKeySerializer(new StringRedisSerializer());
        redisTemplate.afterPropertiesSet();
        return redisTemplate;
    }

    @Bean
    public RedisCacheManager redisCacheManager(RedisConnectionFactory redisConnectionFactory) {
        RedisCacheConfiguration redisCacheConfiguration = RedisCacheConfiguration.defaultCacheConfig()
                .serializeValuesWith(RedisSerializationContext.SerializationPair.fromSerializer(new GenericJackson2JsonRedisSerializer()));
        redisCacheConfiguration.serializeKeysWith(RedisSerializationContext.SerializationPair.fromSerializer(new StringRedisSerializer()));

        Map<String, RedisCacheConfiguration> redisExpireConfig = new HashMap<>();
        //这里设置了一个一分钟的超时配置，如果需要增加更多超时配置参考这个新增即可
        redisExpireConfig.put("1min", RedisCacheConfiguration.defaultCacheConfig()
                .serializeValuesWith(RedisSerializationContext.SerializationPair.fromSerializer(new GenericJackson2JsonRedisSerializer()))
                .serializeKeysWith(RedisSerializationContext.SerializationPair.fromSerializer(new StringRedisSerializer()))
                .entryTtl(Duration.ofMinutes(1)).disableCachingNullValues());

        RedisCacheManager redisCacheManager = RedisCacheManager.builder(RedisCacheWriter.nonLockingRedisCacheWriter(redisConnectionFactory))
                .cacheDefaults(redisCacheConfiguration)
                .withInitialCacheConfigurations(redisExpireConfig)
                .transactionAware()
                .build();
        return redisCacheManager;
    }
}
```

测试代码：
```java
import lombok.Data;

@Data
public class User {
    String uid;
    String email;
    String name;
}
```

```java
@RestController
@RequestMapping(value = "/user")
public class UserController {

    @GetMapping(value = "/info")
    @Cacheable(value = "user", key = "#uid")
    public User getUser(@RequestParam(value = "uid") String uid) {
        System.out.println("getUser====>" + uid);
        User user = new User();
        user.setUid(uid);
        user.setEmail(uid + "@definesys.com");
        user.setName(uid + ":" + System.currentTimeMillis());
        return user;
    }
}
```

用postman发送请求：
```
http://localhost:8080/user/info?uid=ceshi
```

改成`@Cacheable(value = "1min", key = "#uid")`可以给key加上1分钟的过期时间，通过`ttl 1min:userName`查看

用`redis-cli`登录redis查看：
```
➜ docker exec -it redis redis-cli 
127.0.0.1:6379> keys *
127.0.0.1:6379> ttl 1min::ceshi
```

出现的问题：查看发现keys * 一直返回空数组，结果测试发现是SpringBoot连接到了本地之前安装的Redis，卸载了本地的redis后SpringBoot会重新自动连接到了docker的Redis。

## 直接使用
需要将RedisTemplate自动注入进当前的Controller中：

```java
@RestController
@RequestMapping(value = "/user")
public class UserController {

    @Autowired
    RedisTemplate redisTemplate;

    @GetMapping(value = "/redisTest")
    public void redisTest(){
        redisTemplate.opsForValue().set("mykey", 123);
        System.out.println(redisTemplate.opsForValue().get("mykey"));
    }
}
```

使用postman调用如下接口
```
http://localhost:8080/user/redisTest
```

对象的保存都需要序列化，对象要实现Serializable接口或者使用Json序列化，我们在一开始的配置文件中使用了Json序列化。

一开始的配置中使用了自定义的RedisTemplate<String,Object> 的Bean，key使用String(包括Redis Hash 的key)，value存取Redis时默认使用Json格式转换。

我们项目中开发一般不会使用原生方法写代码，提供一个RedisUtils封装一些常用操作供参考：

利用setnx机制实现简单的分布式锁：
[参考](https://www.jianshu.com/p/5b7296445a0e)

[spring cache 学习 —— @Cacheable 使用详解](https://www.cnblogs.com/coding-one/p/12401630.html)
