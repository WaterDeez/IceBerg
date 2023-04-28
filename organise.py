import json
import time
import discord

#Organise someone's location
def organiseLocation(text):
    if text is None:
        return
    name = str(text['firstName']) + "'s current location is: ```"
    long = "\nLongitude: " + str(text['location']['longitude'])
    lat = "\nLatitude: " + str(text['location']['latitude'])
    #acc = "\nAccuracy: " + str(text['location']['accuracy'])
    place = "\nPlace: " + str(text['location']['address1'])
    since = "\nSince " + str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(text['location']['since'])))
    gmap = "https://maps.google.com/?q=" + str(text['location']['latitude']) + "," + str(text['location']['longitude'])
    location = name + lat + long + place + since + "``` " +gmap
    return location

#Organise Leaderboard

#Organise Userlist
def oragniseUserlist(data):
    if data is None:
        return
    list = "Here is all " + data['memberCount'] + " members of " + data['name'] + "```"
    for member in data['members']:
        list += "\n\nName: " + str(member["firstName"]) + " " + str(member["lastName"])
        if member["location"] != None:
            location = member.get('location', {})
            place = f"\nPlace: {location.get('name', 'Unknown')}"
            since_timestamp = location.get("since", None)
            if since_timestamp:
                since = "\nSince: " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(since_timestamp))
            else:
                since = "\nSince: Unknown"
            list += place + since
        else:
            list += "\nLocation Services are disabled for this user (bitch)"
    list += "```"
    return list
