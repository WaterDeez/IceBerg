import discord
import json
import requests
import subprocess
import time

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
#Turn JSON data into readable discord message
def organise(text):
    if text is None:
        return
    name = str(text['firstName']) + "'s current location is: ```"
    long = "\nLongitude: " + str(text['location']['longitude'])
    lat = "\nLatitude: " + str(text['location']['latitude'])
    acc = "\nAccuracy: " + str(text['location']['accuracy'])
    place = "\nPlace: " + str(text['location']['address1'])
    since = "\nSince " + str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(text['location']['since'])))
    location = name + lat + long + acc + place + since + "```"
    return location
#Call locate.sh with url and auth and return as JSON
def locate():
    link = str(_CIRCLE_URL + config['circleID'] + "/members/" + config['memberID'])
    data = json.loads(subprocess.run("./locate.sh %s %s" % (str(auth()), link), shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8'))
    return organise(data)

#Standard DiscordPY setup
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
    async def on_message(self, message):
        if message.content == '/jod':
            await message.channel.send(locate())
intents = discord.Intents.all()
intents.message_content = True
client = MyClient(intents=intents)
client.run(config['token'])



