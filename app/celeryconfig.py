import os

CELERY_BROKER_TRANSPORT_OPTIONS = {
    'region':os.getenv('AWS_REGION','us-east-1'),
    'predefined_queues': {
        'default': {
            'url': os.getenv('SQS_URL')
        }
    }
}

broker_url="sqs://"
result_backend = 'rpc://'
enable_utc = True
