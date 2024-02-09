#Code by vojay-dev
#Run this to generate a new Twitch OAuth Token.
#Token needs to be replaced every 60 days.

import json
import requests


with open("files/config.json") as config_file:
    config = json.load(config_file)


def get_app_access_token():
    params = {
        "client_id": config["client_id"],
        "client_secret": config["client_secret"],
        "grant_type": "client_credentials"
    }

    response = requests.post("https://id.twitch.tv/oauth2/token", params=params)
    access_token = response.json()["access_token"]
    return access_token

access_token = get_app_access_token()
print(access_token)