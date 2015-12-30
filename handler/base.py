import tornado
import simplejson


class BaseHandler(tornado.web.RequestHandler):
    def request_post(self):
        args = tornado.escape.json_decode(self.request.body)
        return args

    def send_write(self, res):
        self.set_header("Content-Type", "text/plain")
        self.write(simplejson.dumps(res))



