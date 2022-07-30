# PR测试
# PR测试
import os
import re
from urllib.request import urlopen, Request, urlretrieve

path = os.getcwd() + os.sep + 'xjj'
def download(n):
    if not os.path.isdir(path):
        os.makedirs(path)
    print(path)
    # 1.找到地址,找到多页地址
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
            zip_list = list(zip(name, link))
        except:
            continue
        # 4.壁纸下载
        for imgurl in zip_list:
            try:
                urlretrieve(imgurl[1], f'{path}{os.sep}{imgurl[0]}.jpg')
            except:
                continue


def main():
    n = int(input('请输入需要下载的页数:'))
    download(n)
    print('下载完成，请查看xjj文件夹')


if __name__ == '__main__':
    main()
