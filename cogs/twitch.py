#---------- Dependencies ----------


import sys
import discord
from discord.ext import commands
from discord.ext.tasks import loop

from Twitch import get_notifications



#---------- Cog setup 1/2 ----------



class twitch (commands.Cog) :
    def __init__(self, bot, *args, **kwargs) :
        self.bot = bot



    #---------- Twitch notification ----------
        


        @loop(seconds=180)
        async def check_streamer() :
            channel = bot.get_channel(1064994193589674045)
            notifications = get_notifications()
            for notification in notifications :
                await channel.send("{} ist jetzt online! {}".format(notification["users_login"], notification))
                
        check_streamer.start()




#---------- Cog setup 2/2 ----------



async def setup(bot):
    await bot.add_cog(twitch(bot))
    print('Twitch wurde geladen')