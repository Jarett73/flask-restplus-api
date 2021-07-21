from flask_restplus import Namespace, fields

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}


class TestDto:
    api = Namespace('test', authorizations=authorizations, description='Test APIs')

    TestGet = api.model('TestGet', {
        'test_id': fields.Integer(),
        'test_name': fields.String()
    })

    TestPost = api.model('TestPost', {
        'test_id': fields.Integer(),
        'test_name': fields.String()
    })

    TestPut = api.model('TestPut', {
        'test_id': fields.Integer(),
        'test_name': fields.String()
    })

    TestDelete = api.model('TestDelete', {
        'test_id': fields.Integer()
    })
