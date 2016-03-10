# -*- coding: utf-8 -*-

__author__ = 'hubian'


from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from db_adapters import SQLAlchemyAdapter


engine = create_engine('mysql://root:123456@localhost/sunnycloud',
                       convert_unicode=True,
                       pool_size=50,
                       max_overflow=100,
                       echo=False)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=True,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
db_adapter = SQLAlchemyAdapter(db_session)

from models import *