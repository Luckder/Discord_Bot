# bot.py
from ast import alias
import os
from pydoc import doc
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

from datetime import datetime
import requests
import pandas as pd
import urllib.request
import re
import csv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='$')

@bot.command(pass_context = True , aliases=['motivate'])
async def inspire(ctx):
    r = requests.get("https://zenquotes.io/api/random")
    df = pd.json_normalize(r.json())

    await ctx.send(df.at[0,'q'])

@bot.command(name='time')
async def time(ctx):
    bruh = datetime.now().strftime("%H.%M")
    await ctx.send(f'The time is {bruh}')

@bot.command(pass_context = True , aliases=['nigger', 'nig'])
async def nigga(ctx):
    r = requests.get("https://api.unsplash.com/photos/random/?client_id=bGS-uWPJIlvpPMVJPZT0sjO63l5DYaLRbKROoPnPROU&query=black person")
    data = r.json()["urls"]['raw']

    e = discord.Embed()
    e.set_image(url=data)
    await ctx.send(embed=e)

@bot.command(pass_context = True , aliases=['2D', '2d', 'waifu'])
async def anime(ctx):
    website = urllib.request.urlopen('https://danbooru.donmai.us/posts/random?login=Luckder&api_key=WVTKTsqoE5sGA85BaEDetBBL')
    html = website.read() #https://stackoverflow.com/questions/19477252/finding-images-in-html-source-code-with-python
    pat = re.compile (rb'<img [^>]*src="([^"]+)')
    img = pat.findall(html)[0].decode()

    e = discord.Embed()
    e.set_image(url=img)
    await ctx.send(embed=e)

@bot.command(pass_context = True, aliases=['burn', 'roast', 'urmom', 'bully'])
async def insult(ctx):
    r = requests.get("https://api.yomomma.info/")
    burn = r.json()['joke']
    await ctx.send(burn)

@bot.command(pass_context = True, aliases=['god', 'holy', 'heaven', 'verse', 'bible-verse'], books="Gay", help='Returns a bible verse(KJV). Usage: $bible <book_name(WITH DASHES)> <chapter_number> <verse_number> Eg: $bible 1-John 3 16, for 1 John 3:16 verse. For a list of books, use $bible books')
async def bible(ctx, arg1, arg2=None, arg3=None):

    book = arg1
    ch = arg2
    v = arg3
    text = ""
    booklist = []
    prevbook = "Book Name"
    books = ""

    with open("kjv.csv", 'r') as f:
        mycsv = csv.reader(f)

        if arg1 == "books":
            for row in mycsv:
                if row[1] != prevbook:

                    booklist.append(row[1])
                    prevbook = row[1]

            for i, j in enumerate(booklist):
                books += f"{i+1}) {j}; "

            await ctx.send(books)

        else:

            for row in mycsv:

                if row[1].lower() == book.lower() and row[3] == ch and row[4] == v:
                    text = row[5]

                elif row[2] == book and row[3] == ch and row[4] == v:
                    text = row[5]

            if text == "":
                await ctx.send("Invalid Input!")

            else:
                await ctx.send(text)




bot.run(TOKEN)