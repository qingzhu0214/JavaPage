[gp参考文档](https://gp-docs-cn.github.io/docs/admin_guide/monitoring/monitoring.html)
[实习时参考的系统](https://www.solarwinds.com/zh/database-performance-monitor/integrations/postgres-monitoring)

### 整体设计模块
[参考pgdash](https://pgdash.io/)

- 查询：有关执行的每个 SQL 查询的大量信息，包括时间序列图、具有可视化的执行计划以及提高查询性能的建议。
- 主备复制：监控广泛的复制指标，包括主服务器和备用服务器的延迟、物理和逻辑复制槽信息以及备用恢复进度。
- 表格和索引：显示有关每个表和索引的信息，例如大小、膨胀、活动、真空和分析信息、缓存效率等。
- 锁和后端：查看哪些查询并等待其他哪些查询。跟踪等待锁定的后端、打开时间过长的事务、空闲事务。

### Sigar安装
监控CPU使用率，内存，磁盘

```
<mirror>
<id>alimaven</id>
<mirrorOf>central</mirrorOf>
<name>aliyun maven</name>
<url>http://maven.aliyun.com/nexus/content/repositories/central/</url>
</mirror>
```

```
<dependency>
	<groupId>org.fusesource</groupId>
	<artifactId>sigar</artifactId>
	<version>1.6.4</version>
</dependency>
```

Windows系统下载这三个文件：sigar-amd64-winnt.dll、sigar-x86-winnt.dll、sigar-x86-winnt.lib。放到jdk安装目录即可【C:/ProgarmFile/java/jdk】！

[参考](https://www.i4k.xyz/article/qq_27093465/54096101)

### PostgreSQL监控
连接数量 select count( * ) from pg_stat_activity

索引命中率和表命中率：
```sql
SELECT	'index hit rate' AS name,
(sum(idx_blks_hit)) / nullif(sum(idx_blks_hit + idx_blks_read),0) AS ratio
FROM pg_statio_user_indexes
UNION ALL
SELECT
'table hit rate' AS name,
sum(heap_blks_hit) / nullif(sum(heap_blks_hit) + sum(heap_blks_read),0) AS ratio
FROM pg_statio_user_tables;
```

查看所有数据库的大小：[参考](https://cloud.tencent.com/developer/article/1558721)
```sql
select pg_database.datname, pg_size_pretty (pg_database_size(pg_database.datname)) AS size from pg_database;
```

查看数据库的历史执行SQL语句 [参考](https://www.v2ex.com/t/580631) [参考2](https://zhidao.baidu.com/question/332505527268297365.html)

### 前端组件库
Element-ui
echart
