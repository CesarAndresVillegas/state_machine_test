import json
import pytest

from aws_cdk import core
from state_machine_test.state_machine_test_stack import StateMachineTestStack


def get_template():
    app = core.App()
    StateMachineTestStack(app, "state-machine-test")
    return json.dumps(app.synth().get_stack("state-machine-test").template)

def test_iam_role_create():
    assert("AWS::IAM::Role" in get_template())

def test_lambdas():
    assert("AWS::Lambda::Function" in get_template())
    assert("state_machine_handler.lambda_handler" in get_template())

def test_dynamo_table():
    assert("AWS::DynamoDB::Table" in get_template())