

class EC2:
    def __init__(self, client):
        """ :type : pyboto3.ec2"""
        self._client = client

    def create_key_pair(self, key_name):
        print('Creating a key pair with name: ' + key_name)
        self._client.create_key_pair(
            KeyName=key_name
        )
