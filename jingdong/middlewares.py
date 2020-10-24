# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import random


class RandomUserAgent(object):
    """设置随机user-agent"""
    def process_request(self, request, spider):
        with open("./user_agent_all.txt", "r") as file:
            user_agent_list = file.readlines()
        user_agent = random.choice(user_agent_list).strip()
        request.headers["User-Agent"] = user_agent


