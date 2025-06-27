from fake_useragent import UserAgent
import random

ua = UserAgent()

# 随机生成10个UA
for _ in range(10):
    print(ua.random)
print(ua.random)  # 随机生成 UA
