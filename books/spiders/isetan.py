from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class IsetanSpider(CrawlSpider):
    '''
    三越伊勢丹のショッピングページを再帰クローリングしてページごとのタイトルを取得するサンプル
    '''
    name = 'isetan'
    allowed_domains = ['www.mistore.jp']
    start_urls = ['https://www.mistore.jp/shopping']
    rules = [Rule(LinkExtractor(), callback='parse_pageinfo', follow=True)]
    custom_settings = {'DOWNLOAD_DELAY': 1}

    def parse_pageinfo(self, response):
        item = {
            'URL': response.url,
            'title': response.xpath('/html/head/title/text()').extract_first().strip()
        }
        if item['title']:
            return item
