# jingdong-books说明文档

## 介绍

jingdong-books是一个基于Scrapy-redis的机票爬虫，是通过京东图书分类界面爬取京东所有的图书信息



本程序使用了scrapy-redis分布式框架，需要提前安装

user_agent_all.txt文件用于保存随机user-Agent


数据库使用了redis数据库，运行需要安装redis

数据库使用Mongodb存储，运行需要安装Mongodb



## 运行

命令在Spiders/目录下运行，和books.py同级目录，运行命令：

scrapy runspider books


## MongoDB部分数据

{
    "_id" : ObjectId("5f93f10b3a8d39b177a2f6e3"),
    "book_name" : "我在未来等你（刘同作品，李光洁、费启鸣、孙千、辛云来、徐婕、张植绿主演，同名原著小说，肖战机场同款书）",
    "book_link" : "https://item.jd.com/12182317.html",
    "picture" : "https://img12.360buyimg.com/n1/s200x200_jfs/t8176/149/1451400837/507149/70f143d2/59ba4a72N42919975.jpg",
    "price" : "39.80",
    "author" : "刘同"
}

{
    "_id" : ObjectId("5f93f10b3a8d39b177a2f6e4"),
    "book_name" : "余华作品：兄弟（新版）",
    "book_link" : "https://item.jd.com/12174895.html",
    "picture" : "https://img10.360buyimg.com/n1/s200x200_jfs/t7438/177/2381955617/172904/76c3a01d/59ae13d2N9521015d.jpg",
    "price" : "49.00",
    "author" : "余华"
}

{
    "_id" : ObjectId("5f93f10b3a8d39b177a2f6e5"),
    "book_name" : "2019第十届茅盾文学奖获奖作品：应物兄",
    "book_link" : "https://item.jd.com/12505366.html",
    "picture" : "https://img11.360buyimg.com/n1/s200x200_jfs/t1/10964/3/5667/170923/5c18f175E4904fb71/00401ba65b609b93.jpg",
    "price" : "79.00",
    "author" : "李洱"
}
