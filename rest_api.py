import requests
import os
import json

authorization_token = os.environ['api_key']

email = "haojing@rocketmail.com"

def list_users():
    headers = {
    "Accept": "application/vnd.pagerduty+json;version=2",
    'Authorization': 'Token token=' + authorization_token
    }

    url = "https://api.pagerduty.com/users"
    payload = {"query": email}
    r = requests.get(url, headers=headers, params=payload)
    print r
    print r.encoding

def create_user():
    url = 'https://api.pagerduty.com/users'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token=' + authorization_token,
        'Content-type': 'application/json',
        'From': email
    }
    payload = {
        'user': {
            'type': 'user',
            'name': "Ana",
            'email': "byby@gfieo.com",
            'role': 'user'
        }
    }
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    print 'Status Code: {code}'.format(code=r.status_code)
    # print r.json()

if __name__ == '__main__':
    create_user()
    print "list_users:"
    list_users()

