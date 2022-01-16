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
from discord.commands import slash_command

import random
import uuid




class Basic_Commands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot



	@slash_command(name="debug", description="Debug the bot to get it's permissions that are enabled and disabled.")
	async def debug(self, ctx):
            embed = discord.Embed(title="Permissions", description=f"{dict(ctx.me.guild_permissions)}", color=0xD708CC)
            embed.timestamp = datetime.utcnow()
            await ctx.respond(embed=embed)



	@slash_command(name="info", description="Information about this bot")
	async def info(self, ctx):

            self.bot_embed_guilds = []

            for t in self.bot.guilds:
                self.bot_embed_guilds.append(t)
            embed = discord.Embed(title="Bot Info", description="General information about Anti-Links", color=0xD708CC)
            embed.add_field(name="Bot developers:", value="User319183#3149, Thewizzzzzz1338#6367", inline=True)
            embed.add_field(name="Guild Count:", value=f"{len(self.bot_embed_guilds)}", inline=True)
            embed.add_field(name="Websocket Ping:", value=f"{round(self.bot.latency * 1000)}")
            embed.timestamp = datetime.utcnow()
            await ctx.respond(embed=embed)



	@commands.Cog.listener()
	async def on_ready(self):
		print('[READY] Cog "Basic_Commands" has been loaded!')
		print(f'---------------------------------------')







def setup(bot):
	bot.add_cog(Basic_Commands(bot))