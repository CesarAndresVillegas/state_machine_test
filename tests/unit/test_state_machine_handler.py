import json
import sys

sys.path.append('lambdas')
import state_machine_handler


def test_lambda_handler():
    response = state_machine_handler.lambda_handler(None, None)
    expected = {
        "statusCode": 200,
        "body": json.dumps('Hello from Lambda!')
    }
    
    assert response["statusCode"] == expected["statusCode"]
    assert response["body"] == expected["body"]
