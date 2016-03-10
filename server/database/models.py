# -*- coding: utf-8 -*-

__author__ = 'hubian'

import json
from . import Base, db_adapter
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, TypeDecorator
from sqlalchemy.orm import relation, backref


def relationship(*arg, **kw):
    ret = relation(*arg, **kw)
    db_adapter.commit()
    return ret


def to_dic(inst, cls):
    # add your coversions for things like datetime's
    # and what-not that aren't serializable.
    convert = dict()
    # convert[TZDateTime] = date_serializer

    d = dict()
    for c in cls.__table__.columns:
        v = getattr(inst, c.name)
        if c.type.__class__ in convert.keys() and v is not None:
            try:
                func = convert[c.type.__class__]
                d[c.name] = func(v)
            except:
                d[c.name] = "Error:  Failed to covert using ", str(convert[c.type.__class__])
        else:
            d[c.name] = v
    return d


def to_json(inst, cls):
    return json.dumps(to_dic(inst, cls))


class DBBase(Base):
    """
    DB model base class, providing basic functions
    """
    __abstract__ = True

    def __init__(self, **kwargs):
        super(DBBase, self).__init__(**kwargs)

    def dic(self):
        return to_dic(self, self.__class__)

    def json(self):
        return to_json(self, self.__class__)

    def __repr__(self):
        return '%s: %s' % (self.__class__.__name__, self.json())


class Host(DBBase):
    __tablename__ = 'host'

    id = Column(Integer, primary_key=True)
    hostname = Column(String(50), unique=True, nullable=False)
    public_ip = Column(String(50), unique=True, nullable=False)
    private_ip = Column(String(50), unique=True, nullable=False)
    mem = Column(String(50), nullable=False)
    cores = Column(Integer, nullable=False)
    disk = Column(String(50), nullable=False)
    create_time = Column(DateTime, nullable=False)
    update_time = Column(DateTime)


class VM(DBBase):
    __tablename__ = 'vm'

    id = Column(Integer, primary_key=True)
    vm_name = Column(String(50), unique=True, nullable=False)
    os_type = Column(String(50), nullable=False)  # constants 0:linux 1:windows
    cores = Column(Integer, nullable=False)
    mem = Column(String(50), nullable=False)
    capacity_g = Column(Integer, nullable=False)
    config = Column(String(50))
    user = Column(String(50), nullable=False)
    create_time = Column(DateTime, nullable=False)
    update_time = Column(DateTime)

    image_id = Column(Integer, ForeignKey('image.id', ondelete='CASCADE'))
    image = relationship('Image', backref=backref('images_vms', lazy='dynamic'))

    host_id = Column(Integer, ForeignKey('host.id', ondelete='CASCADE'))
    host = relationship('Host', backref=backref('host_vms', lazy='dynamic'))


class Network(DBBase):
    __tablename__ = "network"

    id = Column(Integer, primary_key=True)
    mac = Column(String(50), unique=True, nullable=False)
    type = Column(String(50), nullable=False)  # constants 0:public 1:private
    address = Column(String(50), unique=True, nullable=False)
    device = Column(String(50), nullable=False)
    create_time = Column(DateTime, nullable=False)
    update_time = Column(DateTime)

    vm_id = Column(Integer, ForeignKey('vm.id', ondelete='CASCADE'))
    vm = relationship('VM', backref=backref('networks', lazy='dynamic'))


class Disk(DBBase):
    __tablename__ = "disk"

    id = Column(Integer, primary_key=True)
    type = Column(Integer, nullable=True)  # constants 0:system 1:mounted
    capacity_g = Column(Integer, nullable=False)
    format = Column(Integer, nullable=False)  # constants 0:ntfs 1:ext4
    path = Column(String(50), unique=True, nullable=False)
    create_time = Column(DateTime, nullable=False)
    update_time = Column(DateTime)

    vm_id = Column(Integer, ForeignKey('vm.id', ondelete='CASCADE'))
    vm = relationship('VM', backref=backref('disks', lazy='dynamic'))


class Image(DBBase):
    __tablename__ = "image"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    type = Column(Integer, nullable=True)  # constants 0:default 1:provide 2:customize
    path = Column(String(50), unique=True, nullable=False)
    create_by = Column(String(50))
    create_time = Column(DateTime, nullable=False)
    update_time = Column(DateTime)
