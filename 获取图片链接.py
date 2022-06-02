import os
import re
from urllib.request import urlopen, Request

# path = os.getcwd() + os.sep + '图片链接.txt'

path = os.path.join(os.getcwd(), '图片链接.txt')

npath = os.getcwd() + os.sep + '图片名.txt'
n = int(input("选择要下载几页:"))
for i in range(1, n + 1):
    url = f'https://www.3gbizhi.com/meinv/index_{str(i)}.html'
    print(url)
    # 2.请求地址
    # 2.1反爬机制
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
    }
    try:
        request = Request(url=url, headers=headers)
        content = urlopen(request).read().decode('utf-8')
        # 3.获取壁纸图片
        link = re.findall('lazysrc="(.*?jpg)"', content)
        name = re.findall('img alt="(.*?)"', content)
        with open(file=path, mode='a+', encoding='utf-8') as f:
            for l in link:
                f.writelines(l + '\n')
        with open(file=npath, mode='a+', encoding='utf-8') as f1:
            for n in name:
                f1.writelines(n + '\n')
    except:
        continue
