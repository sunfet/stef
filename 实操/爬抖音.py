'''
怎么找到视频网址
浏览器-更多工具-开发者工具-网络(network)-媒体(media)
网页刷新-有1~3条数据-点击-标头-URL

'''

url = 'https://v2-zj-shcm.kwaicdn.com/upic/2025/04/13/15/BMjAyNTA0MTMxNTE3MDhfMzA1ODk3MzYxNV8xNjE2NTQ4NTg0MDFfMV8z_b_Bf89e90484576882e4adf35045b04ef50.mp4?tag=1-1746446677-unknown-0-wqgtd077s7-72e8f776f05222ad&provider=self&clientCacheKey=3x8b4b2eaexfh8k_b.mp4&di=758f07b0&bp=10004&Aecs=172.17.0.73&ocid=100000499&tt=b&ss=vp'
#导入请求模块,在终端pip install requests
import requests
#使用模块
res = requests.get(url)
#print(res.status_code) #状态码 200 成功 403 拒绝 404 失败 405  方法错误 500 服务器错误
#print(res.content)            #响应的内容

'''得到的内容保存
打开文件 open('文件名','打开方式)
打开方式:
    1. r 只读(read)
    2. w 写入(覆盖)(write)
    3. a 追加
    4. rb 二进制读取
    5. wb 二进制写入
    6. ab 二进制追加
    7. r+ 读写
    8. w+ 读写
    9. a+ 读写
    10. rb+ 二进制读写
    11. wb+ 二进制读写
    12. ab+ 二进制读写
    13. r+b 二进制读写
    14. w+b 二进制读写
    15. a+b 二进制读写
读还是写的问题?
文本文件还是二进制文件?
    1. 文本文件: 文本文件的内容是字符串,可以直接读取(TXT)
    2. 二进制文件: 二进制文件的内容是二进制数据,不能直接读取,需要使用二进制读取方式打开


'''
import os

# 检查并创建目标目录
os.makedirs('d:\\python\\downloads', exist_ok=True)

with open('d:\\python\\downloads\\视频.mp4', 'wb') as f: # 写入二进制文件
    # 写入
    f.write(res.content)
#open('视频.mp4','rb').write(res.content)