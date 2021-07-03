class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta["proxy"] = "http://11.111.11.111:3128"


class SplashMiddleware(object):
    def process_request(self, request, spider):
        request.meta["splash"] = {
            'args': {
                'html': True,
            },
            'splash_url': 'http://0.0.0.0:8050',
            'endpoint': 'render.html',
        }
