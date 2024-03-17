import scrapy
from scrapy import FormRequest


class SciSpider(scrapy.Spider):
    name = "sci"
    allowed_domains = ["www.screener.in"]
    start_urls = ["https://www.screener.in/login/"]

    def parse(self, response):
        csrf_token = response.xpath("//input[@name='csrfmiddlewaretoken']/@value").get()
        # sending FormRequest (FormRequest extends the base Request with functionality for dealing with HTML forms)
        # FormRequest.from_response() simulates a user login
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
        # here we define the after_login function we used in callback

    def after_login(self, response):
        # If there's a "logout" text on the page, print "Successfully logged in!"
        if response.xpath("//i[@class='icon-user']/text()").get():
            print('Successfully logged in!')
        pass
