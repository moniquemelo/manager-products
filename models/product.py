from models.base import base


class Product(base.Model):

    id = base.Column(base.Integer, primary_key=True)
    name = base.Column(base.String(128), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name
