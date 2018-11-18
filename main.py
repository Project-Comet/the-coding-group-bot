import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
bot = Bot(command_prefix="?")
@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="tricks on your mind"))
@bot.command(pass_context=True)
async def ping(ctx):
    """Sends a reply to show the bot is working."""
    await bot.say("Pong")
bot.run(os.getenv("TOKEN"))
