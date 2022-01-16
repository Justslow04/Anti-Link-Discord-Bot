
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


#json

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









# ---------------------- end json ---------------------- #


intents = discord.Intents.default()
# intents.typing = False
# intents.presences = False
intents.members = True
# intents.reactions = True



bot = commands.Bot(command_prefix=command_prefix, intents=intents, activity=discord.Activity(type=discord.ActivityType.watching, name=f"for links"))


for fn in os.listdir('./cogs'):
	if fn.endswith('.py'):
		bot.load_extension(f"cogs.{fn[:-3]}")


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    print('Bot is loading modules.')
    print('------')











#REG FILTER

@bot.listen()
async def on_message(message):


        urls = re.findall(
            'http[s][‎]?://(?:[a-zA-Z]|[‎]|[0-9]|[‎]|[$-_@.&+]|[‎]|[!*(),]|[‎]|(?:%[0-9a-fA-F]|[‎][0-9a-fA-F]))+', message.content.lower())

        message.content = message.content.lower()
        message.content = discord.utils.remove_markdown(message.content)
        bypassedRole = discord.utils.get(message.guild.roles, name="Bypassed")


        if whitelist in message.content:
            return

        if message.author.bot:
            return
        
        try:
            if "Bypassed" in message.channel.topic:
                return
            
        except:
            pass


        if bypassedRole in message.author.roles:
            return

        
        if urls:
    
            await message.delete()
            embed = discord.Embed(title="Url Blocked", description=f"{message.author.mention}, URLs aren't allowed.", color=15158332)
            embed.timestamp = discord.utils.utcnow()
            await message.channel.send(embed=embed)
            

            the_guild = message.guild
            the_channel = discord.utils.get(the_guild.text_channels, name="link-logs")
                
            try:
                embed = discord.Embed(title="Link Blocked", description=f"{message.author.mention} sent a link", color=15158332)
                embed.add_field(name="Blocked Link", value=f"{urls}", inline=False)
                embed.add_field(name="Channel", value=f"{message.channel.mention}", inline=False)
                embed.timestamp = discord.utils.utcnow()
                await the_channel.send(embed=embed)

            except:
                pass
































#MESSAGE EDIT FILTER


@bot.listen()
async def on_message_edit(before, after):
        urls = re.findall(
            'http[s][‎]?://(?:[a-zA-Z]|[‎]|[0-9]|[‎]|[$-_@.&+]|[‎]|[!*(),]|[‎]|(?:%[0-9a-fA-F]|[‎][0-9a-fA-F]))+', after.content.lower())

        after.content = after.content.lower()
        after.content = discord.utils.remove_markdown(after.content)
        bypassedRole = discord.utils.get(after.guild.roles, name="Bypassed")

        if whitelist in after.content:
            return

        if after.author.bot:
            return
        
        try:
            if "Bypassed" in before.channel.topic:
                return
            
        except:
            pass
        

        if bypassedRole in after.author.roles:
            return

        if urls:
            await after.delete()
            embed = discord.Embed(title="Url Blocked", description=f"{after.author.mention}, URLs aren't allowed.", color=15158332)
            embed.timestamp = discord.utils.utcnow()
            await after.channel.send(embed=embed)


            the_guild = after.guild
            the_channel = discord.utils.get(the_guild.text_channels, name="link-logs")
        
        
            try:
                embed = discord.Embed(title="Link Blocked", description=f"{after.author.mention} sent a link", color=15158332)
                embed.add_field(name="Blocked Link", value=f"{urls}", inline=False)
                embed.add_field(name="Channel", value=f"{after.channel.mention}", inline=False)
                embed.timestamp = discord.utils.utcnow()
                await the_channel.send(embed=embed)

            except:
                pass












bot.run(token)