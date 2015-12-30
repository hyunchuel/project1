import tornado


class BaseClient(tornado.web.RequestHandler):
    def render(self, url, **kwargs):
        kwargs['server'] = 'http://localhost:8888'

        super(BaseClient, self).render(url, **kwargs)


class LoadHandler(BaseClient):
    def get(self):
        self.render('index.html')


class RegisterHandler(BaseClient):
    def get(self):
        self.render('register.html')