#Code by vojay-dev
#---------- Dependencies ----------


import discord
from discord.ext import commands
from discord.ext.tasks import loop
from TwitchAPI import get_notifications



#---------- Cog setup 1/2 ----------



class twitch (commands.Cog) :
    def __init__(self, bot, *args, **kwargs) :
        self.bot = bot



    #---------- Twitch notification ----------
       

        @loop(seconds=60)
        async def check_streamer() :
            await self.bot.wait_until_ready()
            channel = bot.get_channel(1064994193589674045)
            notifications = get_notifications()
            await channel.send(notifications)
            await channel.send("{} ist jetzt online!".format(notification["users_login"]))#, notification))
            
            for notification in notifications :
                print("check2")
                print(str("{} ist jetzt online! {}".format(notification["users_login"], notification)))
                #await channel.send("{} ist jetzt online! : {}".format(notification["users_login"], notification))
                
        check_streamer.start()



#---------- Cog setup 2/2 ----------



async def setup(bot):
    await bot.add_cog(twitch(bot))
    print('Twitch wurde geladen')