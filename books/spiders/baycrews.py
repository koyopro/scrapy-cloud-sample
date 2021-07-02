from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class BaycrewsSpider(CrawlSpider):
    '''
    ファッションサイトを再帰クローリングして商品名と価格を取得するサンプル
    '''
    name = 'baycrews'
    allowed_domains = ['baycrews.jp']
    start_urls = ['https://baycrews.jp']
    custom_settings = {'DOWNLOAD_DELAY': 1}
    rules = [
        Rule(LinkExtractor(allow=('/item/detail/',)), callback='parse_pageinfo'),
        Rule(LinkExtractor(deny=('/item/review/', '/blog/')))
    ]

    def parse_pageinfo(self, response):
        item = {}
        item['URL'] = response.url
        item['name'] = response.css('h1 > div.name::text').get()
        item['before_price'] = response.css('div.detail > div.price > del::text').get()
        item['after_price'] = response.css('div.detail > div.price > span.after::text').get()
        item['price'] = response.css('div.detail > div.price::text').get().strip()
        if item['name']:
            return item
