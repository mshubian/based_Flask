# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------
# Copyright (c) Yovole network tech info (Shanghai) Co. Ltd.  All rights reserved.
# -----------------------------------------------------------------------------------

__author__ = 'hubian'


MYSQL_HOST = "localhost"
MYSQL_USER = "sunnycloud"
MYSQL_PWD = "sunnycloud"
MYSQL_DB = "sunnycloud"
MYSQL_PORT = 3306

Config = {
    "mysql": {
        "connection": 'mysql://%s:%s@%s:%s/%s' % (MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_PORT, MYSQL_DB)
    },
    "white_list": ['localhost'],

}
