import tinify
import os

# https://tinypng.com/dashboard/api key从这里获取，每月500次调用次数
tinify.key = 'you key '

fileArray = []

# 递归深度遍历文件
def traverse(f):
    fs = os.listdir(f)
    for f1 in fs:
        tmp_path = os.path.join(f, f1)
        if not os.path.isdir(tmp_path):
            if is_img(tmp_path):
                fileArray.append(tmp_path)
        else:
            traverse(tmp_path)

# 根据路径判断文件是不是img
def is_img(path):
    path = path.split('.')[-1].upper()
    return True if (path == 'PNG') | (path == 'JPG') | (path=='JPEG') else False

traverse('E:\codeingSpace\zipimg\img')
for imgpath in fileArray:
    print("compressing ..." + imgpath)
    tinify.from_file(imgpath).to_file(imgpath)