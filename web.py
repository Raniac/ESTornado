import tornado.ioloop
import tornado.web
import tornado.gen
from elasticsearch import Elasticsearch
import json
import time

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world!")

class SearchHandler(tornado.web.RequestHandler):
    def initialize(self): 
        self.es = Elasticsearch([{'host':'127.0.0.1', 'port':9200}])

    async def get(self):
        q = self.get_query_argument('q', '')
        try:
            # r = await self.es.search(index='logstash-2015.08.20', q='http_status_code:5* AND server_name:"web1"', from_='124119')
            r = await IOTest()
        except Exception as e:
            r = str(e)
            print(e)
        response = {'query': q, 'results': r}
        self.write(response)
    
    # def get(self):
    #     q = self.get_query_argument('q', '')
    #     try:
    #         # r = self.es.search(index='logstash-2015.08.20', q='http_status_code:5* AND server_name:"web1"', from_='124119')
    #         r = IOTest()
    #     except Exception as e:
    #         r = str(e)
    #         print(e)
    #     response = {'query': q, 'results': r}
    #     self.write(response)
    
    # @tornado.gen.coroutine
    # def get(self):
    #     q = self.get_query_argument('q', '')
    #     try:
    #         # r = self.es.search(index='logstash-2015.08.20', q='http_status_code:5* AND server_name:"web1"', from_='124119')
    #         r = yield IOTest()
    #     except Exception as e:
    #         r = str(e)
    #         print(e)
    #     response = {'query': q, 'results': r}
    #     self.write(response)

async def IOTest():
    await tornado.gen.sleep(10)
    return 'Non-Blocking'
# def IOTest():
#     time.sleep(10)
#     return 'Blocking'
# @tornado.gen.coroutine
# def IOTest():
#     yield tornado.gen.sleep(10)
#     raise tornado.gen.Return('Non-Blocking')

class AddHandler(tornado.web.RequestHandler):
    def initialize(self): 
        self.es = Elasticsearch([{'host':'127.0.0.1', 'port':9200}])

    def post(self):
        data = json.loads(self.request.body)
        response = {'query': data['q']}
        self.write(response)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/search", SearchHandler),
        (r"/add", AddHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(7474)
    tornado.ioloop.IOLoop.current().start()