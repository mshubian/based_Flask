# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------
# Copyright (c) Yovole network tech info (Shanghai) Co. Ltd.  All rights reserved.
# -----------------------------------------------------------------------------------

__author__ = 'hubian'

from flask import Flask
from flask_restful import Api


# initialize flask and flask restful
app = Flask(__name__)
app.config['SECRET_KEY'] = "sunnycloud!@#"
app.debug = True

api = Api(app)

from utils import init_factory
init_factory()

from views import init_routes
init_routes()