import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run('OTUxOTE3MzUzODc1MTYxMjQ4.YiucHg.S5C4E_cGCQGDZLnakMnsJI0ep-Q')
