
import discord

from discord.ext import commands

from discord import activity

from discord.commands import Option

import os
import sys

import json

import asyncio as asyncio

import re
import string


from discord.ext import *
from discord.ext.commands import *
from ctypes import *
from datetime import datetime


import inspect
import io
import textwrap
import traceback
import aiohttp
from contextlib import redirect_stdout

import re

import string






if os.path.exists(os.getcwd() + "/config.json"):
    
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"Token": ""}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f) 

token = configData["Token"]









with open("./config.json") as f:
    command_prefix = json.load(f)

command_prefix = configData["command_prefix"]









with open("./config.json") as f:
    ownerID = json.load(f)

ownerID = configData["ownerID"]










with open("./config.json") as f:
    admins = json.load(f)

admins = configData["admins"]













with open("./config.json") as f:
    whitelist = json.load(f)

whitelist = configData["whitelist"]














class Mod_Commands(commands.Cog):




    @slash_command()
    @commands.has_permissions(administrator = True)
    async def delete_links(self, ctx):
        messages = await ctx.channel.history(limit=10000000000).flatten()

        for msg in messages:

            urls = re.findall(
                'http[s][‎]?://(?:[a-zA-Z]|[‎]|[0-9]|[‎]|[$-_@.&+]|[‎]|[!*(),]|[‎]|(?:%[0-9a-fA-F]|[‎][0-9a-fA-F]))+', msg.content.lower())

            msg.content = msg.content.lower()
            msg.content = discord.utils.remove_markdown(msg.content)
            bypassedRole = discord.utils.get(msg.guild.roles, name="Bypassed")


            if whitelist in msg.content:
                return

            if msg.author.self.bot:
                return
            
            try:
                if "Bypassed" in msg.channel.topic:
                    return
                
            except:
                pass


            if bypassedRole in msg.author.roles:
                return

            
            if urls:

                await msg.delete()
                await ctx.send("Attempting to delete all URLS. This may take some time depending on how many links were sent by users who weren't bypassed.")
            
          
          
          
    @commands.Cog.listener()
    async def on_ready(self):
        print('[READY] Cog "Mod_Commands" has been loaded!')
        print(f'---------------------------------------')


def setup(bot):
    bot.add_cog(Mod_Commands(bot))