import tornado.ioloop
import tornado.web
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host':'127.0.0.1','port':9200}])
es.search(index='logstash-2015.08.20', q='http_status_code:5* AND server_name:"web1"', from_='124119')

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world!")

class SearchHandler(tornado.web.RequestHandler):
    def initialize(self):
        pass

    def get(self):
        pass

# class AddHandler(tornado.web.RequestHandler):
#     def post(self):
#         pass

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        # (r"/search/(*)", SearchHandler),
        # (r"/add/", AddHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(7474)
    tornado.ioloop.IOLoop.current().start()