class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta["proxy"] = "http://11.111.11.111:3128"
