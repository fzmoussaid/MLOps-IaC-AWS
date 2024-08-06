import sys
import os

def handler(event, context):
    return 'Hello from AWS Lambda using Python' + sys.version + ' and environmental variable ' + os.environ['TEST_ENV_VAR'] + '!'