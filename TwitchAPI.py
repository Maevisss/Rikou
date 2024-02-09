#Code by vojay-dev



import json
import requests
from datetime import datetime


#Load json config to dictionary
with open("files/config.json") as config_file:
    config = json.load(config_file)


#Get user ids from streamers in config
def get_users(login_names):
    params = {
        "login": login_names
    }

    headers = {
        "Authorization": "Bearer {}".format(config["oauth_token"]),
        "Client-Id": config["client_id"]
    }

    response = requests.get("https://api.twitch.tv/helix/users", params=params, headers=headers)
    return {entry["login"]: entry["id"] for entry in response.json()["data"]}

#users = get_users(config["streamer"])
#print(users)


#Get information from streamers
def get_streams(users):
    params = {
        "user_id": users.values()
    }

    headers = {
        "Authorization": "Bearer {}".format(config["oauth_token"]),
        "Client-Id": config["client_id"]
    }

    response = requests.get("https://api.twitch.tv/helix/streams", params=params, headers=headers)
    #Keep username as key
    return {entry["user_login"]: entry for entry in response.json()["data"]} 

#users = get_users(config["streamer"])
#streams = get_streams(users)
#print(streams)


#Dictionary to memorize online users
online_users = {}


def get_notifications():
    users = get_users(config["streamer"])
    streams = get_streams(users)
    print(streams)

    
    notifications = []
    for user_name in config["streamer"]:
        #Add default value for every streamer to prevent a notification on bot start
        #if user_name not in online_users:
            #online_users[user_name] = datetime.utcnow()
        
        #Not in streams = offline else online
        if user_name not in streams:
            online_users[user_name] = None
        else:
            started_at = datetime.strptime(streams[user_name]["started_at"], "%Y-%m-%dT%H:%M:%SZ")
            #If user is online or is online after memorized last time
            if online_users[user_name] is None or started_at > online_users[user_name]:
                notifications.append(streams[user_name])
                online_users[user_name] = started_at

    return notifications