# This Python file uses the following encoding: utf-8
# bot.py
from ast import alias
import os, sys
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

bot = commands.Bot(command_prefix='$', activity = discord.Game(name="Ur Mom"), status=discord.Status.online, help_command = commands.DefaultHelpCommand(no_category = 'Commands'))

@bot.command(pass_context = True , aliases=['motivate', 'inspire', 'clever', 'smart', 'intelligent'])
async def wise(ctx):
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

@bot.command(pass_context = True , aliases=['2D', '2d', 'girl', 'boy', 'husbando'])
async def waifu(ctx):
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

@bot.command(pass_context = True, aliases=["video"], help="| Usage: '$youtube <video name>'")
async def youtube(ctx, *, arg1):
    r = requests.get(f"https://youtube.googleapis.com/youtube/v3/search?part=snippet&q={arg1}&key=AIzaSyCsnNNcUPQvjzIVP1ephVgkiZhPL0SHgyw")
    id = r.json()["items"][0]["id"]["videoId"]
    url = f"https://www.youtube.com/watch?v={id}"

    await ctx.send(url)

@bot.command(pass_context=True)
async def news(ctx, arg1=None):
    
    if arg1:

        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=sg&q={arg1}&apiKey=982f18895dbd465e8bfedaa965e88eea")

    else:

        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=sg&apiKey=982f18895dbd465e8bfedaa965e88eea")

    for obj in r.json()['articles']:
        try:
            title = obj['title']
            url = obj['url']
            desc = obj['description']
        except KeyError:
            continue  # Ignore and skip to next one.
        
        try:

            e = discord.Embed(
            color= discord.Colour.orange() # or any color you want
            )
            e.add_field(name=f'{title}' ,value=f'[{desc}]({url})', inline=False)
            await ctx.send(embed=e)

        except:
            continue

@bot.command(pass_context = True, help="| Usage: $anime upcoming/airing/all/<anime_name> to get anime details.")
async def anime(ctx, *, arg1 = None):
    
    if arg1 == None:
        await ctx.send("Error! $anime upcoming/airing/all")

    arg1 = arg1.lower()

    if (arg1 != "upcoming") or (arg1 != "airing") or (arg1 != "all"):
        r = requests.get(f"https://api.myanimelist.net/v2/anime?q={arg1}&limit=5", headers={"X-MAL-CLIENT-ID":"21a5395ef35705314be29a385b38716b"})

        count = 0

        for obj in r.json()['data']:
                try:
                    title = obj['node']['title']
                    id = obj['node']['id']

                except KeyError:
                    continue  # Ignore and skip to next one.

                try:

                    count += 1
                    e = discord.Embed(
                    color= discord.Colour.orange() # or any color you want
                    )
                    e.add_field(name=f'result anime {count}: ' ,value=f'[{title}](https://myanimelist.net/anime/{id}/)', inline=False)
                    await ctx.send(embed=e)

                except:
                    continue

    else:
        r = requests.get(f"https://api.myanimelist.net/v2/anime/ranking?ranking_type={arg1}&limit=10", headers={"X-MAL-CLIENT-ID":"21a5395ef35705314be29a385b38716b"})

        count = 0

        for obj in r.json()['data']:
                try:
                    title = obj['node']['title']
                    id = obj['node']['id']

                except KeyError:
                    continue  # Ignore and skip to next one.

                try:

                    count += 1
                    e = discord.Embed(
                    color= discord.Colour.orange() # or any color you want
                    )
                    e.add_field(name=f'{arg1} anime {count}: ' ,value=f'[{title}](https://myanimelist.net/anime/{id}/)', inline=False)
                    await ctx.send(embed=e)

                except:
                    continue
    
    


@bot.command(pass_context = True, aliases=['godC', 'holyC', 'heavenC', 'verseC', 'bible-verseC', 'biblec', 'godc', 'holyc', 'heavenc', 'versec', 'bible-versec'], help='| Returns a bible verse(Union - simplified). Usage: $bibleC <book_name(WITH DASHES)> <chapter_number> <verse_number> Eg: $bible 1-John 3 16, for 1 John 3:16 verse. For a list of books, use $bibleC books')
async def bibleC(ctx, arg1, arg2=None, arg3=None, arg4=None):

    book = arg1
    ch = arg2
    v = arg3
    end = arg4
    text = ""
    booklist = []
    clbooklist = ['书 名', '創 世 記', '出 埃 及 記', '利 未 記', '民 數 記', '申 命 記', '約 書 亞 記', '士 師 記', '路 得 記', '撒 母 耳 記 上', '撒 母 耳 記 下', '列 王 紀 上', '列 王 紀 下', '歷 代 志 上', '歷 代 志 下', '以 斯 拉 記', '尼 希 米 記', '以 斯 帖 記', '約 伯 記', '詩 篇', '箴 言', '傳 道 書', '雅 歌', '以 賽 亞 書', '耶 利 米 書', '耶 利 米 哀 歌', '以 西 結 書', '但 以 理 書', '何 西 阿 書', '約 珥 書', '阿 摩 司 書', '俄 巴 底 亞 書', '約 拿 書', '彌 迦 書', '那 鴻 書', '哈 巴 谷 書', '西 番 雅 書', '哈 該 書', '撒 迦 利 亞', '瑪 拉 基 書', '馬 太 福 音', '馬 可 福 音', '路 加 福 音', '約 翰 福 音', '使 徒 行 傳', '羅 馬 書', '歌 林 多 前 書', '歌 林 多 後 書', '加 拉 太 書', '以 弗 所 書', '腓 立 比 書', '歌 羅 西 書', '帖 撒 羅 尼 迦 前 書', '帖 撒 羅 尼 迦 後 書', '提 摩 太 前 書', '提 摩 太 後 書', '提 多 書', '腓 利 門 書', '希 伯 來 書', '雅 各 書', '彼 得 前 書', '彼 得 後 書', '約 翰 一 書', '約 翰 二 書', '約 翰 三 書', '猶 大 書', '启 示 录']
    engbooklist = ['Book Name', 'genesis', 'exodus', 'leviticus', 'numbers', 'deuteronomy', 'joshua', 'judges', 'ruth', '1-samuel', '2-samuel', '1-kings', '2-kings', '1-chronicles', '2-chronicles', 'ezra', 'nehemiah', 'esther', 'job', 'psalms', 'proverbs', 'ecclesiastes', 'song of solomon', 'isaiah', 'jeremiah', 'lamentations', 'ezekiel', 'daniel', 'hosea', 'joel', 'amos', 'obadiah', 'jonah', 'micah', 'nahum', 'habakkuk', 'zephaniah', 'haggai', 'zechariah', 'malachi', 'matthew', 'mark', 'luke', 'john', 'acts', 'romans', '1-corinthians', '2-corinthians', 'galatians', 'ephesians', 'philippians', 'colossians', '1-thessalonians', '2-thessalonians', '1-timothy', '2-timothy', 'titus', 'philemon', 'hebrews', 'james', '1-peter', '2-peter', '1-john', '2-john', '3-john', 'jude', 'revelation']
    prevbook = "书 名"
    books = ""

    with open("union.csv", mode='r', encoding="UTF-8") as f:
        mycsv = csv.reader(f)

        if arg1 == "books":
            for row in mycsv:
                if row[1] != prevbook:

                    booklist.append(row[1])
                    prevbook = row[1]

            for i, j in enumerate(booklist):
                books += f"{i+1}) {j}; "

            await ctx.send(books)

        elif arg2 and arg3 and arg4:

            for row in mycsv:

                for i in range(int(arg3), int(arg4) + 1):

                    try:

                        if (int(clbooklist.index(row[1])) == int(engbooklist.index(book.lower()))) and row[3] == ch and row[4] == str(i):
                            text = f"{row[1]} {ch}:{row[4]} {row[5]}"
                            await ctx.send(text)

                    except:

                        if row[2] == book and row[3] == ch and row[4] == str(i):
                            text = f"{row[1]} {ch}:{row[4]} {row[5]}"
                            await ctx.send(text)

            if text == "":
                await ctx.send("Invalid Input!")

        elif arg2 and arg3:

            for row in mycsv:

                try:

                    if (int(clbooklist.index(row[1])) == int(engbooklist.index(book.lower()))) and row[3] == ch and row[4] == v:
                        text = f"{row[1]} {ch}:{v} {row[5]}"

                except:

                    if row[2] == book and row[3] == ch and row[4] == v:
                        text = f"{row[1]} {ch}:{v} {row[5]}"

            if text == "":
                await ctx.send("Invalid Input!")

            else:
                await ctx.send(text)

        else:

            for row in mycsv:

                try:

                    if (int(clbooklist.index(row[1])) == int(engbooklist.index(book.lower()))) and row[3] == ch:
                        text = f"{row[1]} {ch}:{row[4]} {row[5]}"
                        await ctx.send(text)

                except:

                    if row[2] == book and row[3] == ch:
                        text = f"{row[1]} {ch}:{row[4]} {row[5]}"
                        await ctx.send(text)
            
            if text == "":
                await ctx.send("Invalid Input!")


@bot.command(pass_context = True, aliases=['god', 'holy', 'heaven', 'verse', 'bible-verse'], help='| Returns a bible verse(KJV). Usage: $bible <book_name(WITH DASHES)> <chapter_number> <verse_number> Eg: $bible 1-John 3 16, for 1 John 3:16 verse. For a list of books, use $bible books')
async def bible(ctx, arg1, arg2=None, arg3=None, arg4=None):

    book = arg1
    ch = arg2
    v = arg3
    end = arg4
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

        elif arg2 and arg3 and arg4:

            for row in mycsv:

                for i in range(int(arg3), int(arg4) + 1):

                    if row[1].lower() == book.lower() and row[3] == ch and row[4] == str(i):
                        text = f"{row[1]} {ch}:{row[4]} {row[5]}"
                        await ctx.send(text)

                    elif row[2] == book and row[3] == ch and row[4] == str(i):
                        text = f"{row[1]} {ch}:{row[4]} {row[5]}"
                        await ctx.send(text)

            if text == "":
                await ctx.send("Invalid Input!")

        elif arg2 and arg3:

            for row in mycsv:

                if row[1].lower() == book.lower() and row[3] == ch and row[4] == v:
                    text = f"{row[1]} {ch}:{v} {row[5]}"

                elif row[2] == book and row[3] == ch and row[4] == v:
                    text = f"{row[1]} {ch}:{v} {row[5]}"

            if text == "":
                await ctx.send("Invalid Input!")

            else:
                await ctx.send(text)

        else:

            for row in mycsv:

                if row[1].lower() == book.lower() and row[3] == ch:
                    text = f"{row[1]} {ch}:{row[4]} {row[5]}"
                    await ctx.send(text)

                elif row[2] == book and row[3] == ch:
                    text = f"{row[1]} {ch}:{row[4]} {row[5]}"
                    await ctx.send(text)
            
            if text == "":
                await ctx.send("Invalid Input!")

                



bot.run(TOKEN)