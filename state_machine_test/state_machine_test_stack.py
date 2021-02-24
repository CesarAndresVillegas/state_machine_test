from aws_cdk import (
    aws_iam as _iam,
    aws_lambda as _lambda,
    aws_dynamodb as _dynamodb,
    aws_apigateway as _apigw,
    core
)


class StateMachineTestStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        state_machine_role = _iam.Role(self, "state_machine_role",
            assumed_by = _iam.ServicePrincipal("lambda.amazonaws.com"),
        )

        state_machine_role.add_to_policy(_iam.PolicyStatement(
            resources = ["*"],
            actions = [
                    "lambda:InvokeFunction",
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents",
                ],
        ))

        state_machine_handler = _lambda.Function(
            self, 'state_machine_handler',
            code = _lambda.Code.asset('lambdas'),
            environment = {
                "REGION": "us-east-1",
            },
            function_name = "state_machine_handler",
            handler = 'state_machine_handler.lambda_handler',
            role = state_machine_role,
            runtime =_lambda.Runtime.PYTHON_3_7,
            timeout = core.Duration.seconds(2),
        )

        api_gateway_definition = _apigw.RestApi(
            self, 'api_gateway_definition',
            default_cors_preflight_options = {
                "allow_origins": _apigw.Cors.ALL_ORIGINS,
                "allow_methods": _apigw.Cors.ALL_METHODS,
            },
            description = "Api to engage or handler states machines.",
            rest_api_name = "state_machine_api_gateway",
        )

        state_machine = _apigw.LambdaIntegration(state_machine_handler);

        state_machine_resource = api_gateway_definition.root.add_resource("sm")

        state_machine_resource.add_method("GET", state_machine);

        _dynamodb.Table(
            self, "solicitud_test",
            table_name = "solicitud_test",
            partition_key = _dynamodb.Attribute(
                name = "id",
                type = _dynamodb.AttributeType.STRING
            ),
            stream = _dynamodb.StreamViewType.NEW_AND_OLD_IMAGES,
        )
