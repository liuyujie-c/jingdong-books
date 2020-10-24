# -*- coding: utf-8 -*-
import scrapy
import time
import random
import re
from jingdong.items import JingdongItem
from scrapy_redis.spiders import RedisSpider


class BooksSpider(RedisSpider):
    name = 'books'

    # allowed_domains = ['jd.com']
    # start_urls = ['https://pjapi.jd.com/book/sort']
    redis_key = "start_url"

    def __init__(self, *args, **kwargs):
        """获取allowed_domains"""
        domain = kwargs.pop('domain', '')
        self.allowed_domains = list(filter(None, domain.split(',')))
        super(BooksSpider, self).__init__(*args, **kwargs)

    def make_requests_from_url(self, start_urls):
        """重写start_request"""
        date = int(time.time() * 1000)
        rand = random.randint(10000, 99999)
        callback = "jsonp_%d_%d" % (date, rand)
        start_url = start_urls + "?source=bookSort&callback=%s" % callback
        headers = {
            "referer": "https://book.jd.com/",
        }
        return scrapy.Request(
            url=start_url,
            callback=self.parse,
            headers=headers
        )

    def parse(self, response):
        """从图书分类界面中提取分类的url返回给引擎"""
        id_list = re.findall(
            '"categoryId":(\d+)\.0,"categoryName":"\w*","fatherCategoryId":(\d+)\.0',
            response.body.decode("utf8")
        )
        for el in id_list:
            if el[-1] != "1713":
                url = "https://list.jd.com/list.html?cat=1713,%s,%s&page=1&s=1" % (el[-1], el[0])
                yield scrapy.Request(url=url, callback=self.parse_book_list)

    def parse_book_list(self, response):
        """处理图书列表界面，提取数据并翻页"""

        el_list = response.xpath('//*[@id="J_goodsList"]/ul/li/div')
        if len(el_list) != 0:
            for el in el_list:
                item = JingdongItem()
                item["book_name"] = el.xpath('./div[3]/a/em/text()|./div/div[2]/div[2]/div[3]/a/em/text()').extract_first()
                item["book_link"] = response.urljoin(
                    el.xpath('./div[3]/a/@href|./div/div[2]/div[2]/div[3]/a/@href').extract_first())
                item["picture"] = response.urljoin(el.xpath(
                    './div[1]/a/img/@data-lazy-img|./div/div[2]/div[1]/div[1]/a/img/@data-lazy-img').extract_first())
                item["price"] = el.xpath(
                    './div[2]/strong/i/text()|./div/div[2]/div[1]/div[2]/strong/i/text()').extract_first()
                item["author"] = el.xpath(
                    './div[4]/span[1]/a/text()|./div/div[2]/div[1]/div[4]/span[1]/a/text()').extract_first()
                yield item

            if len(el_list) == 30:

                data = self.make_url_parameter(response.url)
                ajax_url = "https://list.jd.com/listNew.php?%s" % data
                time.sleep(random.random()*3)
                yield scrapy.Request(
                    url=ajax_url,
                    callback=self.parse_book_list,
                )

                next_data = self.make_url_parameter(ajax_url)
                next_url = "https://list.jd.com/list.html?%s" % next_data
                time.sleep(random.random() * 4)
                yield scrapy.Request(
                    url=next_url,
                    callback=self.parse_book_list
                )

    @staticmethod
    def make_url_parameter(url):
        """按照翻页请求参数的规律制作ajax请求和下一页请求的url参数"""
        data_list = url.split("?")[1].split("&")
        page = int(data_list[1].split("=")[-1])
        s = int(data_list[2].split("=")[-1])
        data = "%s&page=%d&s=%d" % (data_list[0], page + 1, s + 26)
        return data


