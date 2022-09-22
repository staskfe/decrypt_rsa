import logging
import boto3
from botocore.exceptions import ClientError
from base64 import b64encode

logger = logging.getLogger(__name__)

KEY_ID = ""


class KMS:
    def __init__(self):
        region_name = "us-east-1"

        session = boto3.session.Session()
        self.kms_client = session.client(
            service_name='kms',
            region_name=region_name
        )

    def decrypt(self, message):
        try:
            text = self.kms_client.decrypt(
                KeyId=KEY_ID,
                CiphertextBlob=message,
                EncryptionAlgorithm="RSAES_OAEP_SHA_256")['Plaintext']
            print(text)

        except ClientError as err:
            print(err.response)
        except Exception as err:
            logger.error(err.response['Error']['Message'])
        else:
            return text.decode()

    def get_public_key_by_kms(self):
        response = self.kms_client.get_public_key(
            KeyId=KEY_ID
        )

        return b64encode(response["PublicKey"])
