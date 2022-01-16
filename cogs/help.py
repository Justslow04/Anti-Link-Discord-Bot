import discord

from discord.ext import commands

from discord import activity

from discord.commands import Option

import os


import json

import asyncio as asyncio




from discord.ext import *
from discord.ext.commands import *
from ctypes import *
from datetime import datetime

from discord.commands import slash_command # Importing the decorator that makes slash commands.








class Help_Commands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot






	@slash_command(name="help", description="Default help panel")
	async def help(self, ctx):

		
            embed=discord.Embed(title="Help Panel", color=0xD708CC, description = "Default help panel.")
            embed.add_field(name = "Commands", value = f" \n 1. help \n 2. debug \n 3. info \n 4. delete_links \n")
            embed.add_field(name = "Support Server", value = "https://discord.gg/ecz2z36gkB")
            embed.add_field(name = "How to bypass", value = "\n Bypassing is easy! To bypass one or a few users you need to make a role called `Bypassed`. \n To bypass a channel, set the channel's description to `Bypassed`.")
            embed.timestamp = datetime.utcnow()
            await ctx.respond(embed=embed)








	@commands.Cog.listener()
	async def on_ready(self):
		print('[READY] Cog "Help_Commands" has been loaded!')
		print(f'---------------------------------------')


def setup(bot):
	bot.add_cog(Help_Commands(bot))
	