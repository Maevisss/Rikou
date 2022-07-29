import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound

#Python 3.10
#discord.py 1.7

#Intents needed for command decoration - check if enabled in developer portal


bot = discord.Client()
bot = commands.Bot(command_prefix='R!', intents = discord.Intents().all())



#---------- Load cogs from folder ----------


cogs = ['cogs.basics', 'cogs.roles', 'cogs.gear', 'cogs.tarkov']

if __name__=='__main__' :
    for cog in cogs :
        try:
            bot.load_extension(cog)
        except Exception as e :
            print(f'{cog} wurde nicht geladen!')


#---------- The core ----------


@bot.event
#On Bot login
async def on_ready() :
    print('RikouDev ist Online!')
        

@bot.event
#Send error if command is unknown
async def on_command_error(ctx, error) :
    if isinstance(error, CommandNotFound) :
        await ctx.channel.send('Dieser Befehl ist nicht bekannt. Überprüfe ob du ihn richtig geschrieben hast oder schaue bei !info nach.')
        return

@bot.event
#Bot shouldn't react on own messages
async def on_message(message) :
    if message.author == bot.user :
        return
    else :
        #Just dont ask...
        if 'loli' in message.content.lower() :
            await message.channel.send('<:MatsuLewd:945282530477752332>')
        elif 'lolis' in message.content.lower() :
            await message.channel.send('<:MatsuLewd:945282530477752332>')

        #Prevents that on_message kills all commands
        await bot.process_commands(message)


#---------- Read Token from file ----------


with open('files\TokenDev.txt', 'r') as TokenFile :
    Token = TokenFile.read() 
bot.run(Token)