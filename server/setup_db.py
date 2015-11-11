# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------
# Copyright (c) Yovole network tech info (Shanghai) Co. Ltd.  All rights reserved.
# -----------------------------------------------------------------------------------

__author__ = 'hubian'

from server.database import Base, engine
from server.database.models import Host
from server.database import db_adapter


def setup_db():
    """Initialize db tables

    make sure database and user correctly created in mysql
    in case upgrade the table structure, the origin table need be dropped firstly
    """
    Base.metadata.create_all(bind=engine)

    # init REQUIRED db data.
    db_adapter.add_object_kwargs(Host,
                                 id='1',
                                 hostname='test1',
                                 public_ip='10.0.2.15',
                                 private_ip='127.0.0.1',
                                 mem='32G',
                                 cores=16
                                 )
setup_db()