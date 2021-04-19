from flask import Blueprint, render_template


error = Blueprint('error', __name__)


@error.app_errorhandler(404)
def not_found(e):
    return render_template('error/not_found.html'), e.code
