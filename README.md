# jingdong-books说明文档

## 介绍

jingdong-books是一个基于Scrapy-redis的机票爬虫，是通过京东图书分类界面爬取京东所有的图书信息



本程序使用了scrapy-redis分布式框架，需要提前安装



数据库使用了redis数据库，运行需要安装redis

数据库使用Mongodb存储，运行需要安装Mongodb



## 运行

命令在Spiders/目录下运行，和books.py同级目录，运行命令：

scrapy runspider books