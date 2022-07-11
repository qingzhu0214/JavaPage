### 实体类
- STATUS_CHANGE_TYPE 异动类型
	大类，小类，是否院系代申请，是否需要上传文件
- StatusChangeRequest
	申请人用户名，提前毕业日期，硕博连读日期，原/新专业，原/新院系，原/新导师，原/新院系代码，休学日期，返校日期，结业日期，预计毕业日期，申请理由


**上传excel文件，解析成一个个对象**

```java
InputStream inputStream = file.getInputStream();

workbook = new XSSFWorkbook(inputStream);

Sheet sheet = workbook.getSheetAt(0);
for (int i = 1; i <= sheet.getLastRowNum(); i++) {
	Row row = sheet.getRow(i);
	if (row == null) {
		continue;
	}
	tUser user = new tUser();
	// 账号
	if (row.getCell(0) != null) {
		row.getCell(0).setCellType(Cell.CELL_TYPE_STRING);
		String account = row.getCell(0).getStringCellValue();
		user.setAccount(account);
	}
	// 姓名
	if (row.getCell(1) != null) {
		row.getCell(1).setCellType(Cell.CELL_TYPE_STRING);
		String name = row.getCell(1).getStringCellValue();
		user.setName(name);
	}

	userRepository.save(user);
}
```

**生成excel**

- 设置excel表头
- 设置序列号
- 设置sheet名
- 把List\<USer>的数据改成List\<List\<String>>数据

```java
XSSFRow currRow = sheet.createRow(rowNum);
currRow.createCell(i).setCellValue(obj.get(i - 1));
```

### 导出excel
```java
response.setContentType("application/vnd.ms-excel");
response.setHeader("Content-Disposition", "attachment;filename=" + URLEncoder.encode(filename, "utf-8"));
OutputStream outputStream = response.getOutputStream();
workbook.write(outputStream);
outputStream.flush();
outputStream.close();
```