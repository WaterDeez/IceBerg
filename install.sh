#!/bin/bash
echo "This script is intended for a proxmox container, and thus run as root."
read -p "Continue? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1
apt update
apt -y upgrade
apt install -y python python3-pip git curl
pip install requires discord.py
git clone https://github.com/WaterDeez/IceBerg
cd IceBerg
echo "Edit the config.json, then run: python3 iceberg.py"

