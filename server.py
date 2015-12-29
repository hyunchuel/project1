import tornado.ioloop
import tornado.web
import os.path

import handler.auth


class Application(tornado.web.Application):

    def __init__(self):

        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates")
        )
        routing = [
            (r"/auth/register", handler.auth.AuthRegisterHandler),
            (r"/login", handler.auth.LoginHandler)
        ]

        tornado.web.Application.__init__(self, routing, **settings)


if __name__ == "__main__":
    PORT = 8888
    app = Application()
    app.listen(PORT)
    print "Start Web Server!! port:" +str(PORT)
    tornado.ioloop.IOLoop.current().start()
