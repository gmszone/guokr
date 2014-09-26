# -*- coding: utf-8 -*-
import scrapy

from tutorial.items import GuokrItem


class GuokrSpider(scrapy.Spider):
    name = "guokr"
    allowed_domains = ["guokr.com"]
    start_urls = []
    for num in range(1, 98):
        start_urls.append("http://mooc.guokr.com/course/?page=" + str(num))

    def parse(self, response):
        for sel in response.css('.course_list li.course'):
            item = GuokrItem()
            item['title_en'] = sel.css('.course-title span')[0].xpath('text()').extract()
            item['title_zh'] = sel.css('.course-title span')[1].xpath('text()').extract()
            item['link'] = sel.xpath('a/@href').extract()[0]
            item['count'] = sel.css(".course-info-num").xpath('text()').extract()[0]
            item['update_date'] = sel.css('.course-info-sp').xpath('text()').extract()
            yield item