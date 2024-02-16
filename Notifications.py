from configparser import ConfigParser
import requests

def load_config(file_path='config.ini'):
    config = ConfigParser()
    config.read(file_path)
    return config['credentials']


def send_notification(message="test", title="", priority=0):
    config_data = load_config()
    token = config_data['api_token']
    user = config_data['user_key']
    url = "https://api.pushover.net/1/messages.json"

    payload = {
        'token': token,
        'user': user,
        'message': message,
        'title':title,
        priority:priority
    }
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    res = requests.request("POST", url, headers=headers, data=payload)
    return res

