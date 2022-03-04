import os
import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
        if message.author == bot.user.name:
            return
        if message.content == 'i like stats':
            await message.channel.send('omg me too i love statistics')

bot.run(TOKEN)