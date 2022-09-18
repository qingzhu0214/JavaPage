import os
import datetime
import shutil


today=datetime.date.today()

mdfile = open("index.md", 'w', encoding='utf-8')

shutil.rmtree("_posts", ignore_errors=True)
os.mkdir("_posts")
base = os.path.join("_posts")

fixed_date = today.strftime('%Y-%#m-%#d-')

search_text1 = "./image"
search_text2 = "/image"
replace_text = "https://github.com/qingzhu0214/JavaPage/raw/wuzu/_posts/myimg"

def replace(file_name):
    with open(file_name, 'r', encoding='UTF-8') as file:
        # 使用 read() 函数读取文件内容并将它们存储在一个新变量中
        data = file.read()
        # 使用 replace() 函数搜索和替换文本
        data = data.replace(search_text1, replace_text)
        data = data.replace(search_text2, replace_text)
        
    # 以只写模式打开我们的文本文件以写入替换的内容
    with open(file_name, 'w', encoding='UTF-8') as file:
        # 在我们的文本文件中写入替换的数据
        file.write(data)

def convert_path(path: str) -> str:
    return path.replace('\\', '/')

# 拷贝文件
from shutil import copyfile
file_need_copy_list = ["Java基础.md", "JVM虚拟机.md", "MySQL数据库.md", "Redis.md", "SpringBoot.md", "操作系统.md", "计算机网络.md", "设计模式.md", "消息队列.md", "Linux.md"]
for file_need_copy in file_need_copy_list:
    copyfile(os.path.join("D:\graduate\JavaStereotypedWriting\Java相关\八股文", file_need_copy), os.path.join("D:\graduate\JavaPage\_posts", file_need_copy))
    
shutil.copytree(os.path.join("D:\graduate\JavaStereotypedWriting\Java相关\八股文", "image"), os.path.join("D:\graduate\JavaPage\_posts", "myimg")) 

for root,dirs,files in os.walk(base):
    print(root)
    # for dr in dirs:
        # print("dr: " + dr)
    title = root.split("\\")[-1]
    if title == "image":
        os.rename(os.path.join(root, name), os.path.join(root, "myimg"))
    if title != "myimg":
        mdfile.write("## {}".format(title))
        mdfile.write('\n')
        print(files)
    for name in files:
        if name.endswith(".md"):
            replace(os.path.join(root, name))
            if name.find(fixed_date) == -1:
                os.rename(os.path.join(root, name), os.path.join(root, fixed_date + name))
                mdfile.write("- [{}]({})".format(name.split('.')[0], convert_path(os.path.join(root, fixed_date + name))))
                mdfile.write('\n')
            else:
                mdfile.write("- [{}]({})".format(name.split('-')[-1].split('.')[0], convert_path(os.path.join(root, name))))
                mdfile.write('\n')