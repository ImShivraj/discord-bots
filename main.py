import discord
from discord.ext import commands


#import all of the cogs
from help_cog import help_cog
from music_cog import music_cog

bot = commands.Bot(command_prefix='/')

#remove the default help command so that we can write out own
bot.remove_command('help')

#register the class with the bot
bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))

#start the bot with our token
bot.run('OTYzNDQ0MzU4NTI1MzU4MTUw.YlWLew.6sEfrW0kviirJNo8fmpHuNBv11I')