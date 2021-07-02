from scrapy.spiders import Spider


class BaycrewsListSpider(Spider):
    name = 'baycrews_list'
    allowed_domains = ['baycrews.jp']
    start_urls = [
        "https://baycrews.jp/item/detail/lappartement/pants/21040560104310",
        "https://baycrews.jp/item/detail/lechoppe/pants/21032050000910",
        "https://baycrews.jp/item/detail/edifice/shoes/21093310221520",
        "https://baycrews.jp/item/detail/js-relume/cutsew/21071465001220",
        "https://baycrews.jp/item/detail/js-relume/cutsew/21071464024020",
    ]

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
        yield item
