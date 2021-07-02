from scrapy.spiders import Spider


class BasicAuthSpider(Spider):
    name = 'basic_auth'
    start_urls = [
        "http://leggiero.sakura.ne.jp/xxxxbasic_auth_testxxxx/secret/kaiin_page_top.htm",
    ]
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware': 543,
        }
    }
    http_user = 'kaiin'
    http_pass = 'naisho'

    def parse(self, response):
        yield {
            'URL': response.url,
            'body': response.css('body::text').get().strip(),
        }
