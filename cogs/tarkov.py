import discord
from discord.ext import commands

class tarkov (commands.Cog) :
    def __init__(self, bot, *args, **kwargs) :
        self.bot = bot
        
        
    @commands.command()
    #Show list of useless eft keys
    async def keys(self, ctx) :
        with open('files/txt/eft_keys.txt', 'r') as file :
            keys = file.read()
        await ctx.channel.send(keys)

    @commands.command()
    #Add key to file
    async def addkey(self, ctx, *, arg) :
        with open('files/txt/eft_keys.txt', 'a') as file :
            file.write(arg + '\n')
        await ctx.channel.send('Der Schlüssel ' + arg + ' wurde hinzugefügt.')

    @commands.command()
    #Remove key from file
    async def removekey(self, ctx, *, arg) :
        with open('files/txt/eft_keys.txt', 'r') as file :
                keys = file.read()
                keylist = keys.split('\n')
                if arg in keylist :
                    keylist.remove(str(arg))
                    with open('files/txt/eft_keys.txt', 'w') as file :
                        for line in keylist :
                            file.write('%s\n' % line )
                    await ctx.channel.send(arg + ' wurde aus der Liste entfernt.')
                else :
                    await ctx.channel.send(arg + ' ist nicht in der Liste.')


#Setup cog
def setup(bot):
    bot.add_cog(tarkov(bot))
    print('Tarkov wurde geladen')