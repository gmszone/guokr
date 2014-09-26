# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GuokrItem(scrapy.Item):
    title_zh = scrapy.Field()
    title_en = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    count = scrapy.Field()
    update_date = scrapy.Field()


class GuokrDetailItem(scrapy.Item):
    title = scrapy.Field()
    desc = scrapy.Field()
    rank = scrapy.Field()
    comments_count = scrapy.Field()
    comments = scrapy.Field()