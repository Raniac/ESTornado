import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world!")

class SearchHandler(tornado.web.RequestHandler):
    def get(self):
        pass

class AddHandler(tornado.web.RequestHandler):
    def post(self):
        pass

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/search/(*)", SearchHandler),
        (r"/add/", AddHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(7474)
    tornado.ioloop.IOLoop.current().start()