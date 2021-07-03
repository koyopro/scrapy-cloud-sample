from scrapy import Spider


class ProxySpider(Spider):
    '''
    Proxyサーバーを経由して、グローバルIPアドレスを確認するサンプル
    '''
    name = 'proxy'
    start_urls = [
        "https://www.cman.jp/network/support/go_access.cgi",
    ]
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'books.middlewares.ProxyMiddleware': 350,
            'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 400,
        }
    }

    def parse(self, response):
        yield {
            'URL': response.url,
            'ip': response.css('div.outIp::text').get().strip(),
        }
