#!/usr/bin/env python3

from aws_cdk import core

from state_machine_test.state_machine_test_stack import StateMachineTestStack


app = core.App()
StateMachineTestStack(app, "state-machine-test", env={'region': 'us-east-1'})

app.synth()
