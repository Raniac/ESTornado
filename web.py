import tornado.ioloop
import tornado.web
import tornado.gen
from elasticsearch import Elasticsearch
import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world!")

class SearchHandler(tornado.web.RequestHandler):
    def initialize(self, es): 
        self.es = es

    def get(self):
        q = self.get_query_argument('q', '')
        try:
            r = self.es.search(index='logstash-2015.08.20', q='http_status_code:5* AND server_name:"web1"', from_='124119')
        except Exception as e:
            r = str(e)
        response = {'query': q, 'results': r}
        self.write(response)

class AddHandler(tornado.web.RequestHandler):
    def initialize(self, es): 
        self.es = es

    def post(self):
        data = json.loads(self.request.body)
        response = {'query': data['q']}
        self.write(response)

def make_app():
    es = Elasticsearch([{'host':'127.0.0.1','port':9200}])
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/search", SearchHandler, dict(es=es)),
        (r"/add", AddHandler, dict(es=es)),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(7474)
    tornado.ioloop.IOLoop.current().start()