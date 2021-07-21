from flask_restplus import Api
from flask import Blueprint
from .main.controller.test_controller import api as test_ns


blueprint = Blueprint('api', __name__, url_prefix='/api/v1')

api = Api(blueprint,
          title='Test API Structure',
          version='1.0',
          description='API web service'
          )


api.namespaces.clear()
api.add_namespace(test_ns)
