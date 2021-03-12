import scrapy
from scrapy import Spider
from lxml import etree
import json
from stock_forecast.items import Model


class Nio(Spider):
    name = "nio"
    allowed_domains = ["https://www.nasdaq.com"]
    start_urls = [
        "https://www.nasdaq.com/market-activity/index/ndx/historical"
    ]

    # def start_requests(self):
    #     start_urls = [
    #         'https://www.nasdaq.com/market-activity/stocks/nio/historical'
    #     ]
    #     # for url in urls:
    #     #     yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        model = Model()

        for i in json.loads(response.body):

            data = etree.HTML(i)

            # locate table
            model_xpath = ".//tbody[@class=\"historical-data__table-body\"]/tr"
            model_list = data.xpath(model_xpath)

            # fill items
            for j in model_list:
                model["DATE"] = j.xpath("./th[1]/text()")[0]
                model["CLOSE"] = j.xpath("./td[1]/text()")[0][1:]
                model["VOLUME"] = j.xpath("./td[2]/text()")[0]
                model["OPEN"] = j.xpath("./td[3]/text()")[0][1:]
                model["HIGH"] = j.xpath("./td[4]/text()")[0][1:]
                model["LOW"] = j.xpath("./td[5]/text()")[0][1:]
                yield model
        # for row in response.xpath("//tr"):
        #     alist = []
        #     for each in row.xpath("//"):
        #         alist.append(each)
        #     yield {
        #             'date': alist[0],
        #             'closePrice': alist[1],
        #             'volume': alist[2],
        #             'openPrice': alist[3],
        #             'high': alist[4],
        #             'low': alist[5]
        #         }