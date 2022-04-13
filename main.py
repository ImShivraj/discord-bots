import discord
from discord.ext import commands
from music import music

cogs = [music]

client = commands.Bot(command_prefix='?', intents= discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)


client.run('OTYzNDQ0MzU4NTI1MzU4MTUw.YlWLew.GkGulTWZ25gvDkvjP85vEV6xsqg')