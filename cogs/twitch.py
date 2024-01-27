#---------- Dependencies ----------


import discord
from discord.ext import commands


#---------- Cog setup 1/2 ----------


class twitch (commands.Cog) :
    def __init__(self, bot, *args, **kwargs) :
        self.bot = bot



#---------- Cog setup 1/2 ----------
        
        
    
   

#---------- Cog setup 2/2 ----------


async def setup(bot):
    await bot.add_cog(twitch(bot))
    print('Twitch wurde geladen')