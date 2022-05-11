# bot.py
import os
from datetime import datetime

import discord
from dotenv import load_dotenv
from discord.ext import commands

import requests
import pandas as pd

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
bot = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hello {member.name}, welcome to the Bots Testing Server!'
    )

@bot.command(name='inspire')
async def inspire(ctx):
    r = requests.get("https://zenquotes.io/api/random")
    df = pd.json_normalize(r.json())

    await ctx.send(df.at[0,'q'])

@bot.command(name='time')
async def time(ctx):
    bruh = datetime.now().strftime("%H.%M")
    await ctx.send(f'The time is {bruh}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return



client.run(TOKEN)
bot.run(TOKEN)