# IceBERG Bot
A simple Python Discord Bot that integrates with the Life360 API

## Setup Guide
There is an install.sh script, which is intended for a Proxmox debian container. The script is run as the root user, which is not ideal but I personally dont care.
You can copy that bash file into your linux flavour and run just to semi-automate the following steps:
- Update repositories
- Clone this repository
- Edit config.json
- Make sure python and dependencies are installed
- Start using python (python3 iceberg.py)

## Extra Info
This was adapted from the Home Assitant implementation of the Life360 API. Check out their code for the authToken for the life360 API.
I got the circleID and memberID just using curl manually, I'm sure there are easier ways to find those ID's.

## Plans
- [ ] Circle Leaderboard 
- [ ] Discord users integration
- [ ] Proper Discord Command Implementation
- [ ] Docker container


## Support Me
The best way to support me is by word of mouth. If you use and enjoy this software solution, share and recommend it to others!