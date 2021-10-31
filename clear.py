#Join My Discord Server - https://discord.gg/rptymubqW5
#Visit My Website - http://quickhardgames.net


client.command(aliases=['c'])  #Adding Aliases
@commands.has_permissions(manage_messages=True)  #Only Mods can use this command
async def clear(ctx, amount=2):     #Defining our Function
    await ctx.channel.purge(limit=amount)   #Result of command
