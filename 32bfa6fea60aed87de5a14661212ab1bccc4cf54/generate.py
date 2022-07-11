import os

file_name = "index1.md"
    
file = open(file_name, 'w')

# f.write("### hello world")
# # 实现换行的功能
# f.write('\n')

base = os.path.join("_posts", "八股文")

def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            yield f
            
for i in findAllFile(base):
    print(i)