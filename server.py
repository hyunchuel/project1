import tornado.ioloop
import tornado.web
import os.path

import handler.auth
import handler.client


class Application(tornado.web.Application):

    def __init__(self):

        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static")
        )
        routing = [
            (r"/client", handler.client.LoadHandler),
            (r"/client/register", handler.client.RegisterHandler),


            (r"/auth/register", handler.auth.AuthRegisterHandler),
            (r"/auth/login", handler.auth.AuthLoginHandler),
            (r"/login", handler.auth.LoginHandler)
        ]

        tornado.web.Application.__init__(self, routing, **settings)


if __name__ == "__main__":
    PORT = 8888
    app = Application()
    app.listen(PORT)
    print "Start Web Server!! port:" +str(PORT)
    tornado.ioloop.IOLoop.current().start()
