import scrapy
from scrapy.spiders import Spider
from scrapy.http import Request


class PinkoiLoginSpider(Spider):
    '''
    会員ログインをして、自身のユーザー名を取得するサンプル
    '''
    name = 'pinkoi_login'
    allowed_domains = ['jp.pinkoi.com']
    start_urls = [
        "https://jp.pinkoi.com/",
    ]
    custom_settings = {
        'DOWNLOAD_DELAY': 1,
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8'
    }

    def parse(self, response):
        item = {}
        item['URL'] = response.url
        item['username'] = response.css('div.user-menu > div > div > div > a > span.text::text').get()
        yield item

    def start_requests(self):
        return [scrapy.FormRequest("https://jp.pinkoi.com/apiv2/account/pinkoi_login",
                                   formdata={'uid': 'koyopro', 'passwd': 'password'},
                                   callback=self.logged_in)]

    def logged_in(self, response):
        for url in self.start_urls:
            yield Request(url, dont_filter=True)
