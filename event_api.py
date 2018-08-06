import requests
import os
import json

INTEGRATION_KEY = os.environ['integration_key']
AUTHORIZATION_TOKEN = os.environ['api_key']

API = "https://events.pagerduty.com/generic/2010-04-15/create_event.json"
EVENT_TYPE = 'resolve' #'acknowledge' or 'resolve'
DESCRIPTION = "it's resolved"
INCIDENT_KEY = '33d971f9ce16487f9f4b6e2c52fbeb54'

payload = {
    'service_key': INTEGRATION_KEY,
    'event_type':EVENT_TYPE,
    # 'description': DESCRIPTION
    'incident_key': INCIDENT_KEY
}

# r = requests.post(API, data = json.dumps(payload))
r = requests.post(API, json=payload)


print r