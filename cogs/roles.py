import discord
from discord.ext import commands

class roles (commands.Cog) :
    def __init__(self, bot, *args, **kwargs) :
        self.bot = bot

    
    #---------- Generate messages to react ----------


    @commands.command()
    #Create message for welcome channel - main role
    async def rulemsg(self, ctx) :
        role = "836504687766405140" #Developer role only
        user = ctx.author
        
        if discord.utils.get(user.roles, name = 'Developer') is None : 
            await ctx.channel.send('Du hast keine Berechtigun diesen Befehl zu nutzen.')
        else :
            with open('files/txt/welcome_message.txt', 'r', encoding = 'utf-8') as ReadyFile :
                Rollen = await ctx.channel.send(ReadyFile.read())
            await Rollen.add_reaction('<SFD_Logo:883728440291889202>')
            
    @commands.command()
    #Create message for intern roles
    async def rolemsg(self, ctx) :
        role = "836504687766405140" #Developer role only
        user = ctx.author
        
        if discord.utils.get(user.roles, name = 'Developer') is None :
            await ctx.channel.send('Du hast keine Berechtigung diesen Befehl zu nutzen.')
        else :
            with open('files/txt/role_message.txt', 'r', encoding = 'utf-8') as RoleFile :
                RoleMessage = await ctx.channel.send(RoleFile.read())

            await RoleMessage.add_reaction('<:XBOXKonsole:847372038301155359>')
            await RoleMessage.add_reaction('<:PlayStation:847368856381292565>')
            await RoleMessage.add_reaction('<:Nintendo:847369837005111326>')
            await RoleMessage.add_reaction('<:PC:847370184817508352>')
            await RoleMessage.add_reaction('<:XBOXGamePass:847368497272061992>')
            await RoleMessage.add_reaction('<:CatGun:847370798259240980>')
            await RoleMessage.add_reaction('<:YouTube:848996415690637403>')
            await RoleMessage.add_reaction('<:Twitch:848996435134251049>')
            await RoleMessage.add_reaction('<:Code:930747586992816128>')


    #---------- Add role on reaction ----------


    @commands.Cog.listener()
    #Add roles when reaction is set
    async def on_raw_reaction_add(self, payload) :
        
        #Reaction welcome message
        with open('files/txt/msg_id_ext.txt', 'r') as ext_id :
            eid = ext_id.read()
        
        message_id = payload.message_id
        if str(message_id) == str(eid) :
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)
            if payload.emoji.name == "SFD_Logo" :
                role = discord.utils.get(guild.roles, name='SFD')
                await payload.member.add_roles(role)

        #Reaction on role message
        with open('files/txt/msg_id_int.txt', 'r') as int_id :
            iid = int_id.read()

        message_id = payload.message_id
        if str(message_id) == str(iid) :
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)

            if payload.emoji.name == "XBOXKonsole" :
                role = discord.utils.get(guild.roles, name='XBOX')
                await payload.member.add_roles(role)
            elif payload.emoji.name == "PlayStation" :
                role = discord.utils.get(guild.roles, name='PlayStation')
                await payload.member.add_roles(role)
            elif payload.emoji.name == "Nintendo" :
                role = discord.utils.get(guild.roles, name='Nintendo')
                await payload.member.add_roles(role)
            elif payload.emoji.name == "PC" :
                role = discord.utils.get(guild.roles, name='PC')
                await payload.member.add_roles(role)
            elif payload.emoji.name == "XBOXGamePass" :
                role = discord.utils.get(guild.roles, name='GamePass')
                await payload.member.add_roles(role)
            elif payload.emoji.name == "CatGun" :
                role = discord.utils.get(guild.roles, name='AirSoft')
                await payload.member.add_roles(role)
            elif payload.emoji.name == "Script" :
                role = discord.utils.get(guild.roles, name='FüllerFechten')
                await payload.member.add_roles(role)
            elif payload.emoji.name == "YouTube" :
                role = discord.utils.get(guild.roles, name='YouTube')
                await payload.member.add_roles(role)
            elif payload.emoji.name == "Twitch" :
                role = discord.utils.get(guild.roles, name='Twitch')
                await payload.member.add_roles(role)
            elif payload.emoji.name == "Code" :
                role = discord.utils.get(guild.roles, name='Developer')
                await payload.member.add_roles(role)

        
#Setup cog
def setup(bot):
    bot.add_cog(roles(bot))
    print('Roles wurde geladen')