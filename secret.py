import boto3


def get_secret():
    secret_name = "dev/eudpag/token"
    region_name = "us-east-1"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )

        return get_secret_value_response['SecretString']
    except Exception as e:
        raise e


get_secret()
