import scrapy


class ScreenerSpider(scrapy.Spider):
    name = "screener"
    allowed_domains = ["www.screener.in"]

    def start_requests(self):
        # Set the login URL and credentials
        login_url = 'https://www.screener.in/login/?'
        username = 'avijit4000@gmail.com'
        password = 'Biswas.123'

        # Request the login page to get CSRF token
        yield scrapy.Request(login_url, callback=self.parse_login, meta={'username': username, 'password': password})

    def parse_login(self, response):
        # Extract CSRF token from the login page
        csrf_token = response.css('input[name="csrfmiddlewaretoken"]::attr(value)').get()

        # Retrieve the username and password from meta
        username = response.meta['username']
        password = response.meta['password']

        # Perform login
        yield scrapy.FormRequest(
            url=response.url,
            formdata={
                'csrfmiddlewaretoken': csrf_token,
                'username': username,
                'password': password,
            },
            callback=self.after_login
        )

    def after_login(self, response):
        # Check if the login was successful
        if "Welcome" in response.text:
            self.log("Login successful. Proceeding with data extraction.")
            # Continue with data extraction after successful login
            url = "https://www.screener.in/company/BEDMUTHA/consolidated/"
            yield scrapy.Request(url, callback=self.parse_data)
        else:
            self.log("Login failed. Check your credentials or the login process.")

    def parse_data(self, response):
        # Extract the desired data from the page
        for number in response.css('div.company-ratios span.number::text'):
            print(number.get())

# To run the spider, use the following command in the terminal:
# scrapy runspider your_spider_script_name.py
