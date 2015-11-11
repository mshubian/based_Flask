# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------
# Copyright (c) Yovole network tech info (Shanghai) Co. Ltd.  All rights reserved.
# -----------------------------------------------------------------------------------

__author__ = 'hubian'

from utils import Utils
from log import Log
from factory import factory
from server.database import db_session
from server.database.db_adapters import SQLAlchemyAdapter

def init_factory():
    factory.provide("util", Utils)
    factory.provide("log", Log)
    factory.provide("db", SQLAlchemyAdapter, db_session)

