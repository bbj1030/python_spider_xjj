import os
from urllib.request import urlretrieve

import cv2
import numpy as np
import paddlehub as hub

path = os.getcwd() + os.sep + 'models'


# 1.皮肤的面积/整张图片的面积
# 2.皮肤的面积/人的面积


# 从彩色图片中提取皮肤区域
def 提取皮肤区域(imColor, imMask):
    hsv_img = cv2.cvtColor(imColor, cv2.COLOR_BGR2HSV)
    color_area = 提取特定颜色区域(hsv_img, [5, 0, 0], [20, 255, 255])
    return cv2.bitwise_and(color_area, imMask)


# 提取特定颜色区域
def 提取特定颜色区域(hsv_img, lower_hsv, high_hsv):
    lowerb = np.array(lower_hsv)  # 提取颜色的低阈值
    upperb = np.array(high_hsv)  # 提取颜色的高阈值
    return cv2.inRange(hsv_img, lowerb, upperb)


# 计算黑白图像中的白色区域面积
def 计算白色区域面积(im):
    bodyArea = 0
    h, w = im.shape
    for col in range(w):
        for row in range(h):
            if im[row, col] != 0:
                bodyArea += 1
    return bodyArea


if __name__ == "__main__":
    # 当前文件夹
    base_dir = os.path.abspath(os.path.dirname(__file__))

    # 加载模型
    human_seg = hub.Module(name='deeplabv3p_xception65_humanseg')

    print('1) 正在提取人体轮廓...')

    # 获取当前文件目录
    model_path = os.path.join(base_dir, 'models' + os.sep)
    print(model_path)
    # 获取文件列表
    lst_image = [model_path + f for f in os.listdir(model_path)]
    print(lst_image)
    results = human_seg.segmentation(paths=lst_image, visualization=True, output_dir='humanseg_output')

    # res_img_path = 'humanseg_output/test.png'
    # img = mpimg.imread(res_img_path)
    # plt.figure(figsize=(10, 10))
    # plt.imshow(img)
    # plt.axis('off')
    # plt.show()
    # 人像抠图并放在自动生成的humanseg_output文件夹中
    # results = human_seg.segmentation(data={'image': lst_image})

    print('2) 正在计算皮肤区域面积...')
    # 去除背景后的文件目录
    human_body_path = os.path.join(base_dir, 'humanseg_output/')
    # 获取文件列表
    lst_human_body = [human_body_path + f for f in os.listdir(human_body_path)]

    for f in lst_human_body:
        imColorful = cv2.imread(f, cv2.IMREAD_UNCHANGED)
        # a) 提取alpha通道(人体部分为白，其余为黑),计算人体部分的面积
        _, _, _, a_channel = cv2.split(imColorful)
        bodyArea = 计算白色区域面积(a_channel)

        # b) 计算彩色图片中皮肤的面积.imSkin中白色部分代表皮肤区域
        imSkin = 提取皮肤区域(imColorful, a_channel)
        skinArea = 计算白色区域面积(imSkin)

        # c) 计算皮肤占身体的比例并通过阈值做判断
        skinPercent = int(100 * skinArea / bodyArea)

        # d) 将models文件夹中的图片重命名，加skinPercent作为前缀
        folder, name_and_ext = os.path.split(f)
        name, extension = os.path.splitext(name_and_ext)
        os.rename(model_path + name + '.png', model_path + str(skinPercent) + '-' + name + '.png')
        print('\t{}.png 皮肤占身体比例:{}'.format(name, skinPercent))

    print('3) 图片分析完成！')































    urlretrieve("http://file.eagleslab.com:8889/%E6%B4%BB%E5%8A%A8%E6%B5%B7%E6%8A%A5/%E6%9A%91%E5%81%87%E7%8F%AD%E4%BA%91%E8%AE%A1%E7%AE%97%E6%B5%B7%E6%8A%A5.png",f"{model_path}{os.sep}暑假云计算开始啦.jpg")
    urlretrieve("http://file.eagleslab.com:8889/%E6%B4%BB%E5%8A%A8%E6%B5%B7%E6%8A%A5/%E6%9A%91%E5%81%87%E7%8F%AD%E4%BA%91%E8%AE%A1%E7%AE%97%E4%BB%8B%E7%BB%8D.png",f"{model_path}{os.sep}性感孙老师带你学云计算.jpg")





   
