import os.path
from flask import Flask, render_template, abort
from demo_shop.database import db_session
from demo_shop.models import Product
from demo_shop.db_generator import generate_db


app = Flask(__name__)


@app.route('/', methods=['GET'], endpoint='index')
def index():
    return render_template('index.html')


@app.route('/products/', methods=['GET'])
def products():
    res = Product.query.all()
    catalog = []
    for result_item in res:
        catalog_item = dict()
        catalog_item['id'] = result_item.id
        catalog_item['name'] = result_item.name
        catalog_item['picture'] = result_item.picture
        catalog_item['price'] = result_item.price
        catalog.append(catalog_item)
    return render_template('products.html', product_list=catalog)


@app.route('/products/<int:product_id>/', methods=['GET'])
def product(product_id):
    res = Product.query.filter(Product.id == product_id).all()
    if len(res) == 0:
        return abort(404)
    result_item = res[0]
    return render_template('product.html', product=result_item)


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
