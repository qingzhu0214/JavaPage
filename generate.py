import os  
mdfile = open("index.md", 'w', encoding='utf-8')

base = os.path.join("_posts")

# def recur(rootDir):
#     for lists in os.listdir(rootDir): 
#         path = os.path.join(rootDir, lists)
#         if os.path.isdir(path) and path.split('\\')[-1] != "image": 
#             fileList = os.listdir(path)
#             for fname in fileList:
#                 oldname=path + os.sep + fname
#                 newname=path + os.sep +'2020-9-25-'+ fname
#                 os.rename(oldname,newname)
#             recur(path) 
#         elif os.path.isfile(path):
#             file.write("- [{}]({})".format(path.split('\\')[-1].split('-')[-1][0:-3], '/'.join(path.split('\\'))))
#             file.write('\n')
            
# recur(base)
# fileList = os.listdir(base)
# for fname in fileList:
#     # oldname=base + os.sep + fname
#     # newname=base + os.sep +'2020-9-25-'+ fname
#     # os.rename(oldname,newname)
#     file.write("- [{}]({})".format(fname.split('-')[-1][0:-3], '_posts/'+fname))
#     file.write('\n')
# file.close()

# def rename(file):
#     oldname=base + os.sep + file
#     newname=base + os.sep +'2020-9-25-'+ file
#     os.rename(oldname,newname)

# fileList = os.listdir(base)
# print(fileList)
# for file in fileList:
#     print(os.path.isfile(file))
#     if os.path.isdir(file):
#         print('print')
#         print(os.path.dirname(__file__))
#         # rename(file)
#         file.write("- [{}]({})".format(file.split('-')[-1][0:-3], '_posts/'+file))
#         file.write('\n')

def convert_path(path: str) -> str:
    seps = r'\/'
    sep_other = seps.replace(os.sep, '')
    return path.replace(sep_other, os.sep) if sep_other in path else path

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
        if name.endswith(".md"):
            os.rename(os.path.join(root, name), os.path.join(root, '2020-9-25-' + name))
            mdfile.write("- [{}]({})".format(name.split('.')[0], convert_path(os.path.join(root, '2020-9-25-' + name))))
            mdfile.write('\n')
            