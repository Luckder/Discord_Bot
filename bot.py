# bot.py
import os
from datetime import datetime

import discord
from dotenv import load_dotenv

import requests
import pandas as pd

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

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

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "$time":
        bruh = datetime.now().strftime("%H.%M")
        await message.channel.send(f'The time is {bruh}')

    if message.content.lower() == "$inspire" or "$motivate":

        r = requests.get("https://zenquotes.io/api/random")
        df = pd.json_normalize(r.json())

        await message.channel.send(df.at[0,'q'])

client.run(TOKEN)