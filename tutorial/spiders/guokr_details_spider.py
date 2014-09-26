# -*- coding: utf-8 -*-
import json

import scrapy

from tutorial.items import GuokrDetailItem


class GuokrDetailSpider(scrapy.Spider):
    name = "guokr_detail"
    allowed_domains = ["guokr.com"]
    json_data = open('json/guokr_items.json')
    start_urls = []
    for data in json.load(json_data):
        start_urls.append(data["link"])

    json_data.close()

    def parse(self, response):
        for sel in response.css('html'):
            item = GuokrDetailItem()
            item['title'] = sel.css('h1.course-title').xpath('text()').extract()
            item['desc'] = sel.xpath('meta/@Description/text()').extract()
            item['rank'] = sel.css('.course-score-average').xpath('text()').extract()
            item['comments_count'] = sel.css(".course-score-people").xpath('text()').extract()[0]
            if sel.css('p.cmt-content')[0].xpath('text()').extract() != "":
                item['comments'] = sel.css('p.cmt-content')[0].xpath('text()').extract()

            yield item