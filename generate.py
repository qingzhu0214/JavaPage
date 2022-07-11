import os

file_name = "index.md"
    
file = open(file_name, 'w', encoding='utf-8')

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
fileList = os.listdir(base)
for fname in fileList:
    # oldname=base + os.sep + fname
    # newname=base + os.sep +'2020-9-25-'+ fname
    # os.rename(oldname,newname)
    file.write("- [{}]({})".format(fname.split('-')[-1][0:-3], '_posts/'+fname))
    file.write('\n')
file.close()