import scrapy


class DataSpider(scrapy.Spider):
    name = "data"
    allowed_domains = ["www.screener.in"]
    start_urls = ["http://www.screener.in/"]

    def parse(self, response):
        pass
