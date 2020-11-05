import discord
import json 
import urllib.request as ur 
from discord.ext import tasks
from bs4 import BeautifulSoup 



Client = discord.Client()
with open("vars.json") as T:
    vars = json.load(T)
    TOKEN = vars["TOKEN"] # Add your token to vars.json
    Text_Channel = vars["CHANNEL"] # Add channel ID to vars.json
    Mention_IDs = vars["IDs"] # Add users IDs as list to vars.json 
old_message = None


def make_mentions(IDs):
    string = str()
    for id in IDs: 
        string += '<@{0}> '.format(id)

    return string

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

@Client.event
async def on_message(message):
    global old_message
    if(message.author.id == 773674161226252328):
        old_message = message

@tasks.loop(seconds=120)
async def myLoop():
    global old_message
    global Mention_IDs 
    b, t = results()
    if(old_message != None):
        try: 
            await old_message.delete()
        except:
            pass
    if (int(b) >= 270):
        embed=discord.Embed(title="2020 US election results", description=f"New Russian Enemy Detected: Joe Biden\n{make_mentions(Mention_IDs)}")
        await Client.get_channel(Text_Channel).send(embed=embed)
    elif (int (t) >= 270): 
        embed=discord.Embed(title="2020 US election results", description=f"A Russian Enemy Has Renewed His Subscription: Donald Trump\n{make_mentions(Mention_IDs)}")
        await Client.get_channel(Text_Channel).send(embed=embed)
    else: 
        embed=discord.Embed(title="2020 US election results", description=f"Joe Biden:{b}\nDonald Trump:{t}\n{make_mentions(Mention_IDs)}")
        await Client.get_channel(Text_Channel).send(embed=embed)


Client.run(TOKEN)