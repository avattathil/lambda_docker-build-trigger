from botocore.vendored import requests
import json

print('Trigger build')

def lambda_handler(event, context):
        url = event['build_trigger']
        payload = json.dumps("{build: false}")
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        build_trigger = requests.post(url, data=json.dumps(payload), headers=headers)
        responseData = {}
        responseData['Data'] = build_trigger.status_code
        print("trigger = " + event['build_trigger'])
        print("branch = " + event['branch'])
        return build_trigger.status_code
