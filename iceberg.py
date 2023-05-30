import discord
import json
import requests
import subprocess
import time
from organise import *
from functions import *
from discord.ext import commands

#load JSON config
config = json.load(open('config.json', 'r'))

# IceBerg.py
# Main python file, calls discord client and other stored functions from commands
#



#Standard DiscordPY setup
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
    async def on_message(self, message):
        if message.content == '/list':
            await message.channel.send(getUserList())
        if message.content.startswith('/locateUser'):
            print("locate user command called")
            await message.channel.send(embed=getUserLocation(message.content[12:]))
        if message.content.startswith('/locateID'):
            print("locate userID command called")
            await message.channel.send(embed=getUserIDLocation(message.content[10:]))
        if message.content.startswith('/getID'):
            print("locate getID command called")
            await message.channel.send(getID(message.content[7:]))
intents = discord.Intents.all()
intents.message_content = True
intents.members = True
client = MyClient(intents=intents)
client.run(config['token'])
