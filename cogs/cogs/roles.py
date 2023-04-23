import discord
from discord.ext import commands
# Array with Rolenames - Emoticon
rollenliste = [["XBOX", "XBOX"], ["PlayStation", "PlayStation"], ["Nintendo", "Nintendo"], ["PC", "Computer"],
                       ["GamePass", "GamePass"], ["AirSoft", "CatGun"], ["YouTube", "YouTube"], ["Twitch", "Twitch"],
                       ["Anime", "RemPout"], ["IT", "Server"], ["Developer", "Terminal"],
                       ["Schwarzfuchs", "SFD"], ["GameCentral", "GC"]]


class roles (commands.Cog) :
    def __init__(self, bot, *args, **kwargs) :
        self.bot = bot




    
    #---------- Generate messages to react ----------


    @commands.command()
    #Create message for intern roles
    async def rolemsg(self, ctx) :
        role = "1063530524259405875" #Developer role only

        user = ctx.author
        
        if discord.utils.get(user.roles, name = 'Developer') is None :
            await ctx.channel.send('Du hast keine Berechtigung diesen Befehl zu nutzen.')
        else :
            with open('files/txt/role_message.txt', 'r', encoding = 'utf-8') as RoleFile :
                RoleMessage = await ctx.channel.send(RoleFile.read())

            await RoleMessage.add_reaction('<:XBOX:1061629245559935017>')
            await RoleMessage.add_reaction('<:PlayStation:1061629107202437151>')
            await RoleMessage.add_reaction('<:Nintendo:1061629069764075601>')
            await RoleMessage.add_reaction('<:Computer:1061629050281541712>')
            await RoleMessage.add_reaction('<:GamePass:1061629205516927027>')
            await RoleMessage.add_reaction('<:CatGun:1061633180328787988>>')
            await RoleMessage.add_reaction('<:YouTube:1063541188071796777>')
            await RoleMessage.add_reaction('<:Twitch:1063541229138223164>')
            await RoleMessage.add_reaction('<:RemPout:1063551455899951145>')
            await RoleMessage.add_reaction('<:Server:1063554322891284570>')
            await RoleMessage.add_reaction('<:Terminal:1063541718370242572>')
            await RoleMessage.add_reaction('<:JojoMario:1063546467584847892>') #Placeholder to make a space to "server role"
            await RoleMessage.add_reaction('<:SFD:1063542308169064528>')
            await RoleMessage.add_reaction('<:GC:1063542584749871225>')



    #---------- Add role on reaction ----------


    @commands.Cog.listener()
    # Add roles when reaction is set
    async def on_raw_reaction_add(self, payload) :

        # Reaction on role message
        with open('files/txt/msg_id_int.txt', 'r') as int_id :
            iid = int_id.read()

        message_id = payload.message_id

        if str(message_id) == str(iid) : #Needs to be static on live bot
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)

            for element in rollenliste:
                if payload.emoji.name == element[1]:
                    role = discord.utils.get(guild.roles, name=element[0])
                    await payload.member.add_roles(role)



    @commands.Cog.listener()
    # Remove roles when reaction is removed
    async def on_raw_reaction_remove(self, payload):

        # Reaction on role message
        with open('files/txt/msg_id_int.txt', 'r') as int_id:
            iid = int_id.read()
        message_id = payload.message_id
        # Array mit Rollenname , Emoticon


        if str(message_id) == str(iid):  # Needs to be static on live bot
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.bot.guilds)
            member = await guild.fetch_member(payload.user_id) ###fetch member becauser on removal there is id

            for element in rollenliste:
                if payload.emoji.name == element[1]:
                    role = discord.utils.get(guild.roles, name=element[0])
                    await member.remove_roles(role)


# Setup cog
async def setup(bot):
    await bot.add_cog(roles(bot))
    print('Roles wurde geladen')