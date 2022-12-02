import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

from props import TEMPLATES

class Main:
    def __init__(self, route, var):
        self.var = var
        self.roure = route

    def router(self):
        env = Environment(
        loader=FileSystemLoader('template'),
        autoescape=select_autoescape(['html']))
        if self.roure == '/test':
            template = env.get_template('test.html')
        elif self.roure == '/about':
            template = env.get_template('about.html')
        else:
            template = env.get_template('index.html')
        return template


    def run(self):
        res = self.router()
        # template = Template(res)
        res = res.render(var=self.var)
        return res.encode('utf-8')


def guicorn_starter(environ, start_response):
    path = environ['PATH_INFO']
    main = Main(path, 'my_test_var')
    # data = render().encode('utf-8')
    start_response("200 OK", [
      ("content-type", "text/html"), ("Content-Length", str(len(main.run())))])
    return iter([main.run()])

