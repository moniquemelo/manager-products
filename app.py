from flask import Flask

from models import db
from controllers import home

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(home)

db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()
