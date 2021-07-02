from scrapy.spiders import SitemapSpider


class BaycrewsSitemapSpider(SitemapSpider):
    name = 'baycrews_sitemap'
    sitemap_urls = ['https://temporary-self.s3.ap-northeast-1.amazonaws.com/tmp/sitemap.xml']

    def __init__(self):
        super().__init__()
        self.download_delay = 1

    def parse(self, response):
        item = {}
        item['URL'] = response.url
        item['name'] = response.css('h1 > div.name::text').get()
        item['before_price'] = response.css('div.detail > div.price > del::text').get()
        item['after_price'] = response.css('div.detail > div.price > span.after::text').get()
        item['price'] = response.css('div.detail > div.price::text').get().strip()
        return item
