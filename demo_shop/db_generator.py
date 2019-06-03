import json
from demo_shop.database import init_db, db_session
from demo_shop.models import Product


def generate_db(filename):
    with open(filename, 'r', encoding='UTF-8') as fp:
        data = json.load(fp)
    init_db()
    for rec in data:
        pr = Product(rec['name'], rec['picture'], rec['blade_material'], rec['hardness'], rec['handle_material'],
                     rec['lock'], rec['action'], rec['blade_length'], rec['full_length'], rec['blade_thickness'],
                     rec['weight'], rec['producer'], rec['origin'], rec['price'])
        db_session.add(pr)
    db_session.commit()
