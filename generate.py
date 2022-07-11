import os

file_name = "index.md"
    
file = open(file_name, 'w', encoding='utf-8')

base = os.path.join("_posts")

def recur(rootDir):
    for lists in os.listdir(rootDir): 
        path = os.path.join(rootDir, lists)
        if path.split('.')[-1] == 'md':
            # - [C++](_posts/2020-9-24-cpp.md)
            file.write("- [{}]({})".format(path.split('\\')[-1][0:-3], '/'.join(path.split('\\'))))
            file.write('\n')
        elif path.split('\\')[-1] != "image":
            file.write("### {}".format(path.split('\\')[-1]))
            file.write('\n')
        print(path)
        if os.path.isdir(path) and path.split('\\')[-1] != "image": 
            recur(path) 
            
recur(base)
file.close()