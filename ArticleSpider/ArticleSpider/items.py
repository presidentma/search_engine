# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobBoleArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #响应地址
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 封面图片
    front_image_url = scrapy.Field()
    # 封面图片本地路径
    front_image_path = scrapy.Field()
    # 发布时间
    publish_time = scrapy.Field()
    # 赞数量
    praise = scrapy.Field()
    # 收藏数量
    collection_num = scrapy.Field()
    # 评论数量
    comment_num = scrapy.Field()
    # 正文内容
    content = scrapy.Field()
    # 文章分类
    variety = scrapy.Field()
