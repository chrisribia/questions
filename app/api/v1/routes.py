from flask import Blueprint
from flask_restful import Api


from .questions.views import Quest


VERSION_ONE = Blueprint('api', __name__, url_prefix='/api/v1')
API = Api(VERSION_ONE)
API.add_resource(Quest, '/questions')