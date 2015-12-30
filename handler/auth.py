import tornado
from handler.base import BaseHandler


class AuthRegisterHandler(BaseHandler):
    def get(self):
        pass

    def post(self):
        args = self.request_post()
        print args

        self.send_write({
            'result': 'success'
        })


class AuthLoginHandler(BaseHandler):
    def get(self):
        pass

    def post(self):
        pass






class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html')
        pass

    def post(self):
        self.get_body_argument("message")

        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.get_body_argument("message"))
        pass
