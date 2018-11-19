import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import time
bot = Bot(command_prefix="?")
@bot.event
async def on_ready():
    while True:
        await bot.change_presence(game=discord.Game(name="with fire"))
        time.sleep(5)
        await bot.change_presence(game=discord.Game(name="tricks on your mind"))
        time.sleep(5)
@bot.command(pass_context=True)
async def ping(ctx):
    """Sends a reply to show the bot is working."""
    await bot.say("Pong")
bot.run(os.getenv("TOKEN"))
