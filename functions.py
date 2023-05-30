import json
import time
import subprocess
import requests

from organise import *

#load JSON config
config = json.load(open('config.json', 'r'))

#Life360 API URLs
_BASE_URL = 'https://api.life360.com/v3/'
_TOKEN_URL = _BASE_URL + 'oauth2/token.json'
_CIRCLES_URL = 'https://www.life360.com/v3/circles'
_CIRCLE_URL = _BASE_URL + 'circles/'
_CIRCLE = _CIRCLE_URL + config['circleID']
_CIRCLE_MEMBERS_URL = _CIRCLE + '/members/'
_CIRCLE_PLACES_URL = _CIRCLE_URL + '/places'

# Functions.py
# Commonly used functions are now stored here instead of the main iceberg.py
#

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
    if data == None:
        return "System Error"
    return (data)

#Get memberID from full name
def getID(name):
    if name is None:
        return "Enter a name"
    #for member in apicon(_CIRCLE['members']):
    data = json.loads(str(apicon(_CIRCLE + '/members')))
    for member in data['members']:    
        if str(member["firstName"]) == name:
            return str(member["id"])
    return "Error!" 
 
#locate User with Name
def getUserLocation(text):
    link = json.loads(str(apicon(_CIRCLE_MEMBERS_URL + getID(text))))
    return organiseLocationEmbed(link)

#locate User with Name
def getUserIDLocation(text):
    link = json.loads(str(apicon(_CIRCLE_MEMBERS_URL + text)))
    return organiseLocationEmbed(link)

#Get userList
def getUserList():
    print("list called")
    list = json.loads(str(apicon(_CIRCLE)))
    text = oragniseUserlist(list)
    return text

