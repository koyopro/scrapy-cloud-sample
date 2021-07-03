from scrapy.spiders import Spider


class SplashSpider(Spider):
    '''
    splashを用いてajaxの要素を取得するサンプル
    '''
    name = 'splash'
    start_urls = [
        "http://news.tv-asahi.co.jp/news_society/articles/000089004.html",
    ]
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'books.middlewares.SplashMiddleware': 350,
            'scrapy_splash.SplashCookiesMiddleware': 723,
            'scrapy_splash.SplashMiddleware': 725,
            'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
        },
        'SPIDER_MIDDLEWARES': {
            'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
        },
        'DUPEFILTER_CLASS': 'scrapy_splash.SplashAwareDupeFilter',
        'HTTPCACHE_STORAGE': 'scrapy_splash.SplashAwareFSCacheStorage'
    }

    def parse(self, response):
        item = {}
        item['URL'] = response.url
        item['ajax_list'] = response.css('p.list-text::text').getall()
        yield item
