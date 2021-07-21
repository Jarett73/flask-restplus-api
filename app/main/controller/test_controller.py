from ..service.test_service import test_get, test_post, test_put, test_delete
from ..util.test_dto import TestDto
from flask_restplus import Resource, reqparse
from flask import request


parser = reqparse.RequestParser()
parser.add_argument('test_id', type=int, required=True)

api = TestDto.api

_test_get = TestDto.TestGet
_test_post = TestDto.TestPost
_test_put = TestDto.TestPut
_test_delete = TestDto.TestDelete


@api.route('/')
class Test(Resource):
    @api.expect(parser, validate=True)
    @api.marshal_list_with(_test_get, envelope='data')
    def get(self):
        """Test get API"""
        args = parser.parse_args()
        return test_get(data=args)

    @api.expect(_test_post, validate=True)
    def post(self):
        """Test post API"""
        data = request.json
        return test_post(data=data)

    @api.expect(_test_put, validate=True)
    def put(self):
        """Test put API"""
        data = request.json
        return test_put(data=data)

    @api.expect(_test_delete, validate=True)
    def delete(self):
        """Test delete API"""
        data = request.json
        return test_delete(data=data)
