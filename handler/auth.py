import tornado


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html')
        pass

    def post(self):
        self.get_body_argument("message")

        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.get_body_argument("message"))
        pass
