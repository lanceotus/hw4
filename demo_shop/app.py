import os.path
from flask import Flask, render_template, abort
from demo_shop.database import db_session
from demo_shop.models import Product
from demo_shop.db_generator import generate_db


app = Flask(__name__)


@app.route('/', methods=['GET'], endpoint='index')
def index():
    return render_template('index.html', fld='ЫЫыы')


@app.route('/products/', methods=['GET'])
def products():
    res = Product.query.all()
    catalog = []
    for pr in res:
        itm = dict()
        itm['id'] = pr.id
        itm['name'] = pr.name
        itm['picture'] = pr.picture
        itm['price'] = pr.price
        catalog.append(itm)
    return render_template('products.html', product_list=catalog)


@app.route('/products/<int:product_id>/', methods=['GET'])
def product(product_id):
    res = Product.query.filter(Product.id == product_id).all()
    if len(res) == 0:
        return abort(404)
    pr = res[0]
    return render_template('product.html', name=pr.name, picture=pr.picture, blade_material=pr.blade_material,
                           hardness=pr.hardness, handle_material=pr.handle_material, lock=pr.lock,
                           action=pr.action, blade_length=pr.blade_length, full_length=pr.full_length,
                           blade_thickness=pr.blade_thickness, weight=pr.weight, producer=pr.producer,
                           origin=pr.origin, price=pr.price)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    db_path = './db/shop.db'
    if not os.path.exists(db_path):
        generate_db('./static/json/data.json')
    app.run('localhost', 9093)
