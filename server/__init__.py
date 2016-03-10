# -*- coding: utf-8 -*-

__author__ = 'hubian'

from flask import Flask
from flask_restful import Api


# initialize flask and flask restful
app = Flask(__name__)
app.config['SECRET_KEY'] = "myNameIsHuBian"
app.debug = True

api = Api(app)

from utils import init_factory
init_factory()

from views import init_routes
init_routes()
