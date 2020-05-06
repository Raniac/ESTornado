import tornado.ioloop
import tornado.web
import tornado.gen
# from elasticsearch import Elasticsearch
from elasticsearch_async import AsyncElasticsearch
import json
import time

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world!")

class SearchHandler(tornado.web.RequestHandler):
    def initialize(self): 
        # self.es = Elasticsearch([{'host':'127.0.0.1', 'port':9200}])
        self.es = AsyncElasticsearch(hosts=['localhost'])

    async def get(self):
        q = self.get_query_argument('q', '')
        try:
            r = await self.es.search(index='test-index', q='http_status_code:5* AND server_name:"web1"')
            # r = await IOTest()
        except Exception as e:
            r = str(e)
            print(e)
        response = {'query': q, 'results': r}
        self.write(response)

# async def IOTest():
#     await tornado.gen.sleep(10)
#     return 'Non-Blocking'

class IndexHandler(tornado.web.RequestHandler):
    def initialize(self): 
        self.es = AsyncElasticsearch(hosts=['localhost'])

    def post(self):
        data = json.loads(self.request.body)
        response = {'query': data['q']}
        self.write(response)

class InfoHandler(tornado.web.RequestHandler):
    def initialize(self): 
        self.es = AsyncElasticsearch(hosts=['localhost'])

    async def get(self):
        try:
            r = await self.es.info()
        except Exception as e:
            r = str(e)
            print(e)
        response = {'results': r}
        self.write(response)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/search", SearchHandler),
        (r"/index", IndexHandler),
        (r"/info", InfoHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(7474)
    tornado.ioloop.IOLoop.current().start()