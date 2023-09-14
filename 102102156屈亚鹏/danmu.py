import cProfile

import requests
import json
import re
from collections import Counter
import csv
import wordcloud  # 词云图 pip install wordcloud
import imageio.v2 as imageio # 读取本地图片 修改词云图形
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
from openpyxl import Workbook


def get_danmu(bvid,headers):
    #获取视频地址
    Cid_url = "https://api.bilibili.com/x/web-interface/view?bvid=" + bvid
    #发送请求
    Cid_req = requests.get(Cid_url, headers=headers)
    #选取内容
    Cid_res = json.loads(Cid_req.text)
    #设定格式
    cid = Cid_res['data']['cid']
    #
    Danmu_url = "https://comment.bilibili.com/" + str(cid) + ".xml"
    Danmu_req = requests.get(Danmu_url, headers=headers)
    #转码，防止乱码
    Danmu_req.encoding = 'utf-8'
    Danmu_list = re.findall('<d p=".*?">(.*?)</d>',Danmu_req.text)
    # for index in danmu_list:
    #     with open('弹幕.txt', mode='a', encoding='utf-8') as f:
    #         f.write(index)
    #         f.write("\n")
    #         print(index)
    return Danmu_list
    pass

# 打开txt文件
def main():
 with open('E:\pythonProject4\弹幕.txt', 'r',encoding='utf-8') as file:
    # 逐行读取文件内容并存入列表
    barrage_list = file.readlines()
    # 使用 Counter 统计每种弹幕的数量
    barrage_counts = Counter(barrage_list)
    #数据可视化
    top_20_barrages = barrage_counts.most_common(20)
    barrages = [barrage for barrage, count in top_20_barrages]
    counts = [count for barrage, count in top_20_barrages]

    # 设置合适的字体
    font = FontProperties(fname='C:\Windows\Fonts\msyh.ttc')
    # 绘制柱状图
    plt.bar(range(len(barrages)), counts, tick_label=barrages)
    plt.xlabel('弹幕', fontproperties=font)
    plt.ylabel('数量', fontproperties=font)
    plt.title('弹幕数量排名前20', fontproperties=font)
    plt.xticks(rotation=90, fontproperties=font)
    plt.subplots_adjust(bottom=0.2)
    plt.show()
# 输出数量排名前20的弹幕
    for barrage, count in top_20_barrages:
       print(f'弹幕"{barrage}"的数量为：{count}')

    wb = Workbook()
    ws = wb.active
    # 写入表头
    ws.append(['弹幕', '数量'])
# 写入数据
    for danmu, count in top_20_barrages:
       ws.append([danmu, count])
# 保存Excel文件
    wb.save('danmu_statistics.xlsx')





    img = imageio.imread('榴莲.png')

    f = open('弹幕.txt', encoding='utf-8')
    text = f.read()
# # 列表转成字符串
    text_str = ' '.join(text)
# print(text_str)
    wc = wordcloud.WordCloud(
       width=500,  # 宽度
       height=500,  # 高度
       background_color='white', # 背景颜色
       mask=img,
    # stopwords={'海洋', '日本', '保护', '的', '核污水', '排海'},
       font_path='msyh.ttc'  # 字体文件
    )
    wc.generate(text_str)
    wc.to_file('词云1.png')
if __name__ == "__main__":
    profile = cProfile.Profile()
    profile.run("main()")
    profile.print_stats()






