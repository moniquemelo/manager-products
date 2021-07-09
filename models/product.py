from models.base import base


class Product(base.Model):

    code = base.Column(base.Integer, unique=True, primary_key=True)
    name = base.Column(base.String(128), nullable=False)
    price = base.Column(base.DECIMAL(10, 2), nullable=False)
    image = base.Column(base.String(255))
    brand = base.Column(base.String(128))
    quantity = base.Column(base.Integer, nullable=False)

    def __init__(self, code, name, price, image, brand, quantity):
        self.code = code
        self.name = name
        self.price = price
        self.image = image
        self.brand = brand
        self.quantity = quantity

    def __repr__(self):
        return self.name
