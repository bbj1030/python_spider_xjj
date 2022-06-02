import os
from urllib.request import urlretrieve

dir = os.getcwd() + os.sep + '下载图片'
if not os.path.isdir(dir):
    os.makedirs(dir)
path = os.getcwd() + os.sep + '图片链接.txt'
npath = os.getcwd() + os.sep + '图片名.txt'
i = 1
with open(file=path, mode='r', encoding='utf-8') as f:
    with open(file=npath, mode='r', encoding='utf-8') as f1:
        for line in f.readlines():
            name = f1.readline().replace('\n', '')
            urlretrieve(line, f'{dir}{os.sep}{name}.jpg')
            i += 1
print("下载完成")
