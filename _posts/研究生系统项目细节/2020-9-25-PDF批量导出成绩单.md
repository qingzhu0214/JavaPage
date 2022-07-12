### 实体表
成绩单下载记录
签章配置

### 生成成绩单
- 获取到学生的成绩list
- 将生产的pdf放到本地文件目录下
- 使用itext pdf 生成pdf [参考](https://www.jianshu.com/p/20d4905383b4)
	- 从另一个系统里取一寸照
```java
String outid = String.format("31AD111DE2210E5CDC95663B%s%d", sno, calendar.get(Calendar.DAY_OF_MONTH));
return String.format(PHOTO_PATTERN, sno, DigestUtils.md5DigestAsHex(outid.getBytes()));
```

- 计算绩点

### 签章
```java
// anysign包
byte[] pdfBty = ClientUtil.readFileToByteArray(file);
ChannelMessage message = this.anySignClientTool.pdfSign(ruleNumList, pdfBty);
ClientUtil.writeByteArrayToFile(file, message.getBody());

// 转成byte[]
FileUtils.readFileToByteArray(file)
```

### 批量导出
- 勾选多选框
- 通过上传学生excel进行导出
- 转zip
```java
ZipOutputStream zipOut = new ZipOutputStream(new ByteArrayOutputStream());
// 用文件名构造ZipEntry
// 用write方法写入字节流
```