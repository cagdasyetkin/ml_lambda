import json

import boto3


def test_sentiment_is_predicted():
    # specify the region name of the AWS account
    # you are using for this test
    boto3.setup_default_session(region_name='eu-west-1')
    # specify the secret key id and secret access key:




    client = boto3.client('lambda')


    response = client.invoke(
        FunctionName='ml-model-development-ml_model',
        InvocationType='RequestResponse',
        Payload=json.dumps({
            "text": "I am so happy! I love this tutorial! You really did a great job!"
        })
    )

    assert json.loads(response['Payload'].read().decode('utf-8'))["sentiment"] == "positive"