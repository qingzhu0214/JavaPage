import os
import datetime

today=datetime.date.today()

mdfile = open("index.md", 'w', encoding='utf-8')

base = os.path.join("_posts")

fixed_date = today.strftime('%Y-%#m-%#d-')

search_text = "./image"
replace_text = "https://github.com/qingzhu0214/JavaPage/raw/wuzu/_posts/image"

def replace(file_name):
    with open(file_name, 'r', encoding='UTF-8') as file:
        # 使用 read() 函数读取文件内容并将它们存储在一个新变量中
        data = file.read()
        # 使用 replace() 函数搜索和替换文本
        data = data.replace(search_text, replace_text)
        
    # 以只写模式打开我们的文本文件以写入替换的内容
    with open(file_name, 'w', encoding='UTF-8') as file:
        # 在我们的文本文件中写入替换的数据
        file.write(data)

def convert_path(path: str) -> str:
    return path.replace('\\', '/')

for root,dirs,files in os.walk(base):
    print(root)
    # for dr in dirs:
        # print("dr: " + dr)
    title = root.split("\\")[-1]
    if title != "image":
        mdfile.write("## {}".format(title))
        mdfile.write('\n')
        print(files)
    for name in files:
        if name.endswith("基础.md"):
            replace(os.path.join(root, name))
            if name.find(fixed_date) == -1:
                os.rename(os.path.join(root, name), os.path.join(root, fixed_date + name))
                mdfile.write("- [{}]({})".format(name.split('.')[0], convert_path(os.path.join(root, fixed_date + name))))
                mdfile.write('\n')
            else:
                mdfile.write("- [{}]({})".format(name.split('-')[-1].split('.')[0], convert_path(os.path.join(root, name))))
                mdfile.write('\n')
            