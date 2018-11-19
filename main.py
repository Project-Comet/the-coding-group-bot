import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
bot = Bot(command_prefix="?")
@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="with fire"))
@bot.command(pass_context=True)
async def ping(ctx):
    """Sends a reply with the bot latency."""
    await bot.say('Pong! {0}'.format(round(bot.latency, 1))
bot.run(os.getenv("TOKEN"))
