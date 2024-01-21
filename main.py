import discord
from discord.ext import commands
import os
import config

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix = "!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged {bot.user.name}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')   

bot.run(config.bottoken)