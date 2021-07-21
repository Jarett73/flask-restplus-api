

class Const():
    secret_key = 'testsecretkey'
    authorizations = {
        'apikey': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'X-API-KEY'
        }
    }

    # Message Constants
    SUCCESS = 'SUCCESS'
    FAIL = 'FAIL'
    SUCCESS_CODE = 201
    FAILURE_CODE = 400
