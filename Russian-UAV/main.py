import discord
from discord.ext import tasks
import urllib.request as ur 
from bs4 import BeautifulSoup 

Client = discord.Client()
Text_Channel = 315240368927145985

def results ():
    website = "https://www.google.com/search?client=firefox-b-d&q=presidential+election" 
    headers = dict() 

    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

    req = ur.Request(website, headers=headers)
    google = ur.urlopen(req)
    html = google.read().decode()
    html = html.replace('"', '').replace('/', '/')
    soup = BeautifulSoup(html, "html.parser")
    b = str(soup.findAll("span", {"class": "rDMtnd"})[0]).split('>')[1].split('<')[0].strip()
    t = str(soup.findAll("span", {"class": "rDMtnd"})[1]).split('>')[1].split('<')[0].strip()
    return b , t

@Client.event
async def on_ready():
    print("Bot is Ready!")
    myLoop.start()

@tasks.loop(seconds=120)
async def myLoop():
    b, t = results()
    if (int(b) >= 270):
        embed=discord.Embed(title="2020 US election results", description=f"New Russian Enemy Detected: Joe Biden")
        await Client.get_channel(Text_Channel).send(embed=embed)
        await Client.get_channel(Text_Channel).send("<@325651365789564940> <@258709200312598528> <@515509035638980608>")
    if (int (t) >= 270): 
        embed=discord.Embed(title="2020 US election results", description=f"A Russian Enemy Has Renewed His Subscription: Donald Trump")
        await Client.get_channel(Text_Channel).send(embed=embed)
        await Client.get_channel(Text_Channel).send("<@325651365789564940> <@258709200312598528> <@515509035638980608>")
    else: 
        embed=discord.Embed(title="2020 US election results", description=f"Joe Biden:{b}\nDonald Trump:{t}")
        await Client.get_channel(Text_Channel).send(embed=embed)
        await Client.get_channel(Text_Channel).send("<@325651365789564940> <@258709200312598528> <@515509035638980608>")


Client.run('NzczNjc0MTYxMjI2MjUyMzI4.X6MqNg.2TICgEcppF-wbReTFTdGCSeUEoE')