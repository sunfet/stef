# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import random
from Douban.settings import user_agent_list
from scrapy import signals

#定义一个中间件类
class UserAgentRandom(object):
    def process_request(self, request, spider):
        # 随机选择一个user-agent
        user_agent = random.choice(user_agent_list)
        # 设置user-agent
        request.headers['User-Agent'] = user_agent

