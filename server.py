import tornado.ioloop
import tornado.web
import handler.auth
import os.path


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class Application(tornado.web.Application):

    def __init__(self):

        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates")
        )
        routing = [
            (r"/", handler.auth.LoginHandler),
            (r"/login", handler.auth.LoginHandler)
        ]

        tornado.web.Application.__init__(self, routing, **settings)


if __name__ == "__main__":
    PORT = 8888
    app = Application()
    app.listen(PORT)
    print "Start Web Server!! port:" +str(PORT)
    tornado.ioloop.IOLoop.current().start()
