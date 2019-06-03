from sqlalchemy import Table, Column, String, Integer, Float
from sqlalchemy.orm import mapper
from demo_shop.database import metadata, db_session


class Product(object):
    query = db_session.query_property()

    def __init__(self, name=None, picture=None, blade_material=None, hardness=None,
                 handle_material=None, lock=None, action=None, blade_length=None,
                 full_length=None, blade_thickness=None, weight=None, producer=None,
                 origin=None, price=None):
        self.name = name
        self.picture = picture
        self.blade_material = blade_material
        self.hardness = hardness
        self.handle_material = handle_material
        self.lock = lock
        self.action = action
        self.blade_length = blade_length
        self.full_length = full_length
        self.blade_thickness = blade_thickness
        self.weight = weight
        self.producer = producer
        self.origin = origin
        self.price = price

    def __repr__(self):
        return '<Product %r>' % self.name


products = Table('products', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', String(255), unique=True),
                 Column('picture', String(255)),
                 Column('blade_material', String(255)),
                 Column('hardness', String(10)),
                 Column('handle_material', String(255)),
                 Column('lock', String(50)),
                 Column('action', String(255)),
                 Column('blade_length', Float),
                 Column('full_length', Float),
                 Column('blade_thickness', Float),
                 Column('weight', Float),
                 Column('producer', String(255)),
                 Column('origin', String(255)),
                 Column('price', Float)
              )
mapper(Product, products)
