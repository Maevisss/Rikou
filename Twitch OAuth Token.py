#Based on code by vojay-dev
#Get the Twitch OAuth Token and replace the old one

import requests

def get_access_token() :
        with open('files/txt/twitch_client_id.txt', 'r', encoding = 'utf-8') as TwitchClientID :
            ClientID = (TwitchClientID.read())

        with open('files/txt/twitch_secret.txt', 'r', encoding = 'utf-8') as TwitchClientSecret :
            ClientSecret = (TwitchClientSecret.read())

        values = {
            "client_id" : ClientID,
            "client_secret" : ClientSecret,
            "grant_type" : "client_credentials"
            }
        

        response = requests.post("https://id.twitch.tv/oauth2/token", params = values)
        access_token = response.json()["access_token"]

        with open('files/txt/twitch_oauth_token.txt', 'a') as file :
                file.write(access_token)
        return access_token

access_token = get_access_token()
print(access_token)

open('files/txt/twitch_oauth_token.txt', 'w')
with open('files/txt/twitch_oauth_token.txt', 'a') as file :
    file.write(access_token)
    print("Wrote Twitch OAuth token to file!")