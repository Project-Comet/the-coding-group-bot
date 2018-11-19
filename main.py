import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import time
bot = Bot(command_prefix="?")
@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name=""))
@bot.command(pass_context=True)
async def ping(ctx):
    """Sends a reply with the bot latency."""
    t = await bot.say('Pong!')
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
    await bot.edit_message(t, new_content='Pong! Took: {}ms'.format(int(ms)))
    print(f'Ping {int(ping)}ms')
@bot.command(pass_context=True)
async def punch(ctx, user: discord.Member):
    """Punches the specified user."""
    await bot.say("Now punching " + user.mention)
    await bot.send_message(user, "You've been punched!")
@bot.command()
async def suggest(*, msg: str):
    channel=bot.get_channel('513579486608883724')
    await bot.send_message(channel,msg)
bot.run(os.getenv("TOKEN"))
