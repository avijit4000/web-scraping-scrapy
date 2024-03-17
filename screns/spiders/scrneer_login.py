import scrapy
from scrapy import FormRequest

class NewiSpider(scrapy.Spider):
    name = "newi"
    allowed_domains = ["www.screener.in"]
    start_urls = ["https://www.screener.in/login/?"]

    def parse(self, response):
        csrf_token = response.xpath("//input[@name='csrfmiddlewaretoken']/@value").get()
        yield FormRequest.from_response(
            response,
            formxpath='//form',
            formdata={
                'csrf_token': csrf_token,
                'username': 'avijit4000@gmail.com',
                'password': 'Biswas.123'
            },
            callback=self.after_login
        )
    def after_login(self, response):
        # If there's a "logout" text on the page, print "Successfully logged in!"
        if response.xpath('(//button[@class="button-plain"])[2]/br').get():
            print('Successfully logged in!')
