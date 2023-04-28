import discord
import json
import requests
import subprocess
import time
from organise import *

#Life360 API URLs
_BASE_URL = 'https://api.life360.com/v3/'
_TOKEN_URL = _BASE_URL + 'oauth2/token.json'
_CIRCLES_URL = 'https://www.life360.com/v3/circles'
_CIRCLE_URL = _BASE_URL + 'circles/'
_CIRCLE_MEMBERS_URL = _CIRCLE_URL + '/members'
_CIRCLE_PLACES_URL = _CIRCLE_URL + '/places'

#load JSON config
config = json.load(open('config.json', 'r'))

#get Life360 header auth token
def auth():
       session = requests.session()
       data = {
               'grant_type': 'password',
               'username': config['username'],
               'password': config['password'],
           }    
       resp = session.post(_TOKEN_URL.format(1), data=data, timeout=None,
               headers={'Authorization': 'Basic ' + config['authToken']})
   
       if not resp.ok:
               try:
                   err_msg = json.loads(resp.text)['errorMessage']
               except:
                   resp.raise_for_status()
                   raise ValueError('Unexpected response to {}: {}: {}'.format(
                       _TOKEN_URL, resp.status_code, resp.text))
               raise ValueError(err_msg)
       resp = resp.json()
       return resp['access_token']

#Call apicon.sh with url
def apicon(link):
    data = subprocess.run("./locate.sh %s %s" % (str(auth()), link), shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
    return (data)

#Standard DiscordPY setup
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
    async def on_message(self, message):
        if message.content == '/list':
            print("list called")
            list = json.loads(str(apicon(str(_CIRCLE_URL + config['circleID']))))
            await message.channel.send(oragniseUserlist(list))
        if message.content == '/jod':
            await message.channel.send(organiseLocation(apicon(str(_CIRCLE_URL + config['circleID'] + "/members/" + config['memberID']))))
            print("Jod command called")
intents = discord.Intents.all()
intents.message_content = True
client = MyClient(intents=intents)
#client.run(config['token'])
client.run('NTA3NzU0OTQxNzU1MTYyNjU1.GzOVRK.x5QgWDZgjz35co6TCnd5PtlmgXzf9UtTLMLdj0')


