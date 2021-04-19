from flask import Flask

from models import base
from controllers import home, error

app = Flask(__name__)
app.config.from_object('config')

blueprints = (home, error)
for blueprint in blueprints:
    app.register_blueprint(blueprint)

base.init_app(app)
with app.app_context():
    base.create_all()

if __name__ == '__main__':
    app.run()
