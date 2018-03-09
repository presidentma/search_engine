# _*_ coding: utf-8 _*_
import scrapy
from scrapy.http import Request
import re
from urllib import parse

from ArticleSpider.items import JobBoleArticlespiderItem

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['http://blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        """
        获取文章列表中的文章url并交给解析函数进行解析
        获取下一页url ，继续爬取
        """
        #当前页文章链接列表
        posturl_node = response.css(".post-thumb a")
        for post_node in posturl_node:
            #文章地址
            post_url = post_node.css('::attr(href)').extract_first()
            image_url = post_node.css('img::attr(src)').extract_first()
            yield scrapy.Request(url=post_url, callback=self.parse_detail, meta={"front_image_url":image_url}, dont_filter=True)

        # 提取下一页url
        next_page = response.xpath('//a[@class="next page-numbers"]/@href').extract_first()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse, dont_filter=True)

    #解析文章详情
    def parse_detail(self, response):
        article_items = JobBoleArticlespiderItem()
        #标题
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract_first()
        #封面图片
        front_image_url = response.meta.get("front_image_url","")
        #发布时间
        publish_time = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract_first().strip().replace(" ·","")
        #赞数量
        praise = response.xpath('//div[@class="post-adds"]//h10/text()').extract_first()
        praise = int(praise)
        #收藏数量
        collection = response.xpath('//div[@class="post-adds"]/span[2]/text()').extract_first()
        match_re = re.match(r".*?(\d+).*", collection)
        if match_re:
            collection_num = match_re.group(1)
        else:
            collection_num = 0
        #评论数量
        comment = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/ a[2]/text()').extract_first()
        match_re = re.match(r".*?(\d+).*", comment)
        if match_re:
            comment_num = match_re.group(1)
        else:
            comment_num =0
        #正文内容
        content = response.xpath('//div[@class="entry"]').extract_first()
        #文章分类
        variety = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/ a[1]/text()').extract_first()
        article_items["title"] = title
        article_items["front_image_url"] = [front_image_url]
        article_items["publish_time"] = publish_time
        article_items["praise"] = praise
        article_items["collection_num"] = collection_num
        article_items["comment_num"] = comment_num
        article_items["content"] = content
        article_items["variety"] = variety
        yield article_items