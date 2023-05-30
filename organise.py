import json
import time
import discord

# Organise.py
# Any function that handles text/json organisation or formatting for discord is stored here
#

#Organise someone's location
def organiseLocation(data):
    if data is None:
        return
    name = str(data["firstName"]) + "'s current location is: ```"
    long = "\nLongitude: " + str(data['location']['longitude'])
    lat = "\nLatitude: " + str(data['location']['latitude'])
    #acc = "\nAccuracy: " + str(text['location']['accuracy'])
    place = "\nPlace: " + str(data['location']['address1'])
    since = "\nSince " + str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data['location']['since'])))
    gmap = "https://maps.google.com/?q=" + str(data['location']['latitude']) + "," + str(data['location']['longitude'])
    location = name + lat + long + place + since + "``` " +gmap
    return location

#Organise someone's location (with discord embed)
def organiseLocationEmbed(data):
    #embed=discord.Embed(title=str(data["firstName"]) + " " + str(data["lastName"]), url="https://maps.google.com/?q=" + str(data['location']['latitude']) + "," + str(data['location']['longitude']), description="", color=0x8aa0d5)
    #embed=discord.Embed(title=str(data["firstName"]) + " " + str(data["lastName"]), url="", description="", color=0x8aa0d5)
    
    if data["location"] != None:
        embed=discord.Embed(title=str(data["firstName"]) + " " + str(data["lastName"]), url="https://maps.google.com/?q=" + str(data['location']['latitude']) + "," + str(data['location']['longitude']), description="", color=0x8aa0d5)
        location = data.get('location', {})
        embed.add_field(name="Place", value=location.get("name", 'Unknown'), inline=True)
        since_timestamp = location.get("since", None)
        if since_timestamp != None:
            embed.add_field(name="Since", value=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(since_timestamp)), inline=True)
        else:
            embed.add_field(name="Since", value="Unknown", inline=True)
    else:
        embed=discord.Embed(title=str(data["firstName"]) + " " + str(data["lastName"]), url="", description="", color=0x8aa0d5)
        embed.add_field(name="Location", value="Location Services are disabled for this user", inline=True)
    embed.set_thumbnail(url=data["avatar"])
    embed.add_field(name="Phone", value=data["loginPhone"], inline=True)
    embed.add_field(name="Email", value=data["loginEmail"], inline=True)
    return embed

#Organise Userlist
def oragniseUserlist(data):
    if data is None:
        return
    list = "Here is all " + data['memberCount'] + " members of " + data['name'] + "```"
    for member in data['members']:
        list += "\n\nName: " + str(member["firstName"]) + " " + str(member["lastName"])
        list += "\nID: " + str(member["id"])
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

#Organise Leaderboard