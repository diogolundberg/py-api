from os import path
from sanic import Sanic
from sanic.response import text
from sanic.exceptions import FileNotFound
from .api import api

application = Sanic()
application.static('/static', './static')
application.static('/favicon.ico', './static/favicon.ico')
application.blueprint(api)
