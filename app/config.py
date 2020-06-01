import os

broker_options = {
    'region':os.getenv('AWS_REGION','us-east-1'),
    'predefined_queues': {
        'default': {
            'url': os.getenv('SQS_URL')
        }
    }
}
