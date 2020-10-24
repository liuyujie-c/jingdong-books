# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JingdongItem(scrapy.Item):
    # define the fields for your item here like:
    book_name = scrapy.Field()  # 书名
    book_link = scrapy.Field()  # 详情页面链接
    picture = scrapy.Field()    # 图书图片
    price = scrapy.Field()      # 价格
    author = scrapy.Field()     # 作者

