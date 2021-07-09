import json

import requests
from flask import Blueprint, render_template

from models import Product, base

home = Blueprint('home', __name__)


@home.route('/', methods=['GET'])
def getindex():
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                             '91.0.4472.124 Safari/537.36'}

    request = requests.get('https://servicespub.prod.api.aws.grupokabum.com.br/home/v1/home/produto', headers=headers)
    api = json.loads(request.content)


    for product in api['produtos']:
        prod_code = product['codigo']
        prod_name = product['nome']
        prod_price = product['preco']
        prod_image = product['img']  # verificar se vale a pena
        prod_brand = product['fabricante']['nome']
        prod_quantity = 0
        if 'quantidade' in product['oferta']:
            prod_quantity = product['oferta']['quantidade']


        all_product = Product(prod_code, prod_name, prod_price, prod_image, prod_brand, prod_quantity)
        base.session.add(all_product)
        base.session.commit()
    return render_template('home/index.html')


@home.route('/', methods=['POST'])
def postindex():
    return "Testando o post :)"
