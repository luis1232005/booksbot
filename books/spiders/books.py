# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["xkm.com.tw"]
    start_urls = [
        "http://www1.xkm.com.tw/hr/DATA/HR190604.htm"
    ]

    def parse(self, response):
        count = 0
        for tr in response.xpath('//body/table/tr'):
            count = count + 1
            tds = len(tr.xpath('td'))
            item = {}
            if(count > 4 and tds > 6):
                item['tv'] = tr.xpath('td[2]/text()').extract()
                item['program'] = tr.xpath('td[3]/text()').extract()
                item['time'] = tr.xpath('td[4]/text()').extract()
                item['viewingRate'] = tr.xpath('td[5]/text()').extract()
                yield item
