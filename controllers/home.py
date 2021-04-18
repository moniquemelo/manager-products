from flask import Blueprint, render_template


home = Blueprint('home', __name__)


@home.route('/', methods=['GET'])
def getindex():
    return render_template('home/index.html')


@home.route('/', methods=['POST'])
def postindex():
    return "Testando o post :)"
