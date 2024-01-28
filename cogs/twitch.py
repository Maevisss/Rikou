#---------- Dependencies ----------


import json
import discord
import requests
from discord.ext import commands
#Based on code by vojay-dev



#---------- Cog setup 1/2 ----------



class twitch (commands.Cog) :
    def __init__(self, bot, *args, **kwargs) :
        self.bot = bot



    #---------- Twitch notification ----------



        with open("files/txt/config.json") as twitch_config :
            config = json.load(twitch_config)

        values = {
            "client_id" : config("client_id"),
            "client_secret" : config("client_secret"),
            "grant_type" : "client_credentials"
            }
        
        headers = {
                "Authorization" : "Bearer {}".format(config["oauth_token"]),
                "Client-Id" : config["client_id"]
            }

        @commands.command()
        #Remember to add the token from the txt to the config.json
        async def get_access_token() :
             response = requests.post("https://id.twitch.tv/oauth2/token", params = values)
             oauth_token = response.json()["access_token"]
                
             open('files/txt/twitch_oauth_token.txt', 'w')
             with open('files/txt/twitch_oauth_token.txt', 'a') as file :
                file.write(oauth_token)
             
             return oauth_token


        async def get_users(login_names) :
            params = {
                "login" : login_names
                }
            
            response = requests.get("https://api.twitch.tv/helix/users", params = values, headers = headers)
            return {entry["login"] : entry["id"] for entry in response.json()["data"]}
    
        
        #print(users)

        async def get_streams(users) :
            params = {
                "user_id" : users.values()
            }

            response = requests.get("https://api.twitch.tv/helix/streams", params = values, headers = headers)
            return {entry["users_login"] :  entry for entry in response.json()["data"]}
        

        users = get_users(config["streamer"])
        streams = get_streams(users)
        print(streams)
        print("Done")





        
        
    
   

#---------- Cog setup 2/2 ----------


async def setup(bot):
    await bot.add_cog(twitch(bot))
    print('Twitch wurde geladen')