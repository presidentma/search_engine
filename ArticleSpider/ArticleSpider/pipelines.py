# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline

class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item


#自定义图片处理类
class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        if "front_image_url" in item:
            for ok, val in results:
                image_file_path = val["path"]
            item["front_image_path"] = image_file_path
        return item

