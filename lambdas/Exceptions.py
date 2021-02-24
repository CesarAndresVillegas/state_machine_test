
def handler(func):
    def handle(*args):
        try:
            returned_value = func(*args)
        except KeyError as e:
            print({"statusCode": 501, "body": {"message": 'Internal server error occurs.', "cause": e}})
            returned_value = {"statusCode": 501, "body": {"message": 'Internal server error occurs', "cause": e}}

        except Exception as e:
            print({"statusCode": 500, "body": {"message": 'Internal server error occurs', "cause": e}})
            returned_value = {"statusCode": 500, "body": {"message": 'Internal server error occurs.', "cause": e}}
        return returned_value
    return handle
