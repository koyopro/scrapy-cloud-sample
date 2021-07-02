from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class IsetanSpider(CrawlSpider):
    name = 'isetan'
    allowed_domains = ['www.mistore.jp']
    start_urls = ['https://www.mistore.jp/shopping']

    rules = [Rule(LinkExtractor(), callback='parse_pageinfo', follow=True)]

    def __init__(self):
        super().__init__()
        self.download_delay = 1

    def parse_pageinfo(self, response):
        item = {}
        item['URL'] = response.url
        titles = response.xpath('/html/head/title/text()').extract()
        if titles:
            item['title'] = titles[0]
            return item
