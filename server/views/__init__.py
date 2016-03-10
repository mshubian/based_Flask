# -*- coding: utf-8 -*-

__author__ = 'hubian'

from server import api
from server.database import db_adapter
from server.database.models import Host
from flask_restful import Resource


class TestResource(Resource):
    def get(self):
        return "server started"


class HostResource(Resource):
    def get(self):
        return db_adapter.find_first_object_by(Host, id=1).dic()


def init_routes():
    api.add_resource(TestResource, "/api/test")
    api.add_resource(HostResource, "/api/host")

