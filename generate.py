import os  
mdfile = open("index.md", 'w', encoding='utf-8')

base = os.path.join("_posts")

fixed_date = '2020-9-25-'

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
        if name.endswith(".md"):
            if name.find(fixed_date) == -1:
                os.rename(os.path.join(root, name), os.path.join(root, fixed_date + name))
                mdfile.write("- [{}]({})".format(name.split('.')[0], convert_path(os.path.join(root, fixed_date + name))))
                mdfile.write('\n')
            else:
                mdfile.write("- [{}]({})".format(name.split('-')[-1].split('.')[0], convert_path(os.path.join(root, name))))
                mdfile.write('\n')
            