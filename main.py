import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import itertools
import random
import json
authorized_users = [
    "466677474672246795", # bsoyka#7570
    "210593330101354496"  # joshy#9000
]
with open("jokes.json") as file:
    jokes = json.load(file)
bot = Bot(command_prefix="?")
bot.remove_command("help")
status_list = [("with fire", 0), ("the endless game of debugging", 0), ("cat videos on YouTube", 3), ("tricks on your mind", 0), ("my code being written", 3), ("the screams of children", 2)]
async def change_status():
    await bot.wait_until_ready()
    msgs = itertools.cycle(status_list)
    while not bot.is_closed:
        next_status = next(msgs)
        await bot.change_presence(game=discord.Game(name=next_status[0], type=next_status[1]))
        await asyncio.sleep(10)
@bot.event
async def on_ready():
    pass
@bot.command(pass_context=True)
async def ping(ctx):
    """Sends a reply with the bot latency."""
    t = await bot.say('Pong!')
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
    await bot.delete_message(t)
    embed = discord.Embed(title="Ping", description="Pong", color=0x149900)
    embed.add_field(name="Latency", value=str(int(ms)) + " ms", inline=False)
    await bot.say(embed=embed)
    print(f'Ping {int(ping)}ms')
@bot.command(pass_context=True)
async def punch(ctx, user: discord.Member):
    """Punches the specified user."""
    embed = discord.Embed(title="Now Punching", description=user.mention, color=0x149900)
    await bot.say(embed=embed)
    embed_2 = discord.Embed(title="You've been punched!", description="By " + ctx.message.author.name, color=0x149900)
    await bot.send_message(user, embed=embed_2)
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True, manage_messages=True)
async def clear(ctx, amount=100):
    """Clear the specified number of messages, default 100 messages."""
    channel = ctx.message.channel
    messages = []
    amount = int(amount) + 1
    async for message in bot.logs_from(channel, limit=amount):
        messages.append(message)
    await bot.delete_messages(messages)
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await bot.send_message(ctx.message.channel, "You do not have permission to use that command.".format(ctx.message.author.mention))
@bot.command(pass_context=True)
async def members(ctx):
    """Return the server member count."""
    embed = discord.Embed(title="Member Count", description=str(len(ctx.message.server.members)), color=0x149900)
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def joke(ctx):
    """Tell a joke."""
    joke = random.choice(jokes)
    embed = discord.Embed(title="Joke", description=joke["body"], color=0x149900)
    embed.set_footer(text="Joke #: " + str(joke["id"]))
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def dm(ctx, user: discord.Member, *, msg: str):
    """Sends a DM message to the specified user."""
    if ctx.message.author.id in authorized_users:
        embed = discord.Embed(title="Now sending message", description=msg, color=0x149900)
        embed.set_footer(text=user.name)
        await bot.say(embed=embed)
        embed_2 = discord.Embed(title="You've received a message!", description=msg, color=0x149900)
        embed_2.set_footer(text=ctx.message.author.name)
        await bot.send_message(user, embed=embed_2)
    else:
        embed = discord.Embed(title="Error", description="You do not have permission to use that command.", color=0x990000)
        await bot.say(embed=embed)
@bot.command(pass_context=True)
async def help(ctx):
    """Show help."""
    embed = discord.Embed(title="Help", description="These are the commands you can use.", color=0x149900)
    embed.add_field(name="?help", value="Show this message.", inline=False)
    embed.add_field(name="?ping", value="Send the bot latency.", inline=False)
    embed.add_field(name="?punch (user)", value="DM punch the user.", inline=False)
    embed.add_field(name="?clear (limit)", value="Clear the specified number of messages.", inline=False)
    embed.add_field(name="?members", value="Send the server member count.", inline=False)
    embed.add_field(name="?joke", value="Send a joke.", inline=False)
    await bot.say(embed=embed)
bot.loop.create_task(change_status())
bot.run(os.getenv("TOKEN"))
