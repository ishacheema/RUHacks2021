import discord
from discord.ext import commands
from replit import db
import os
import requests
import json
import random

# client = discord.Client()
client = commands.Bot(command_prefix ='$')

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]
bad_words = ["shut up", "stupid", "dumb", "idiot", "loser"] 

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person"
]


insult_warning = 'Please dont send bad words in the channel!'


# teacher = '837914922872602664'
student = '837915203680600065'

# @client.event
# async def on_message(message):
#     msg = message.content
#     if any(word in msg for word in sad_words):
#       await message.channel.send(random.choice(starter_encouragements))
    
    # if any(word in msg for word in sad_words):
    #   await message.channel.send(insult_warning)
def is_it_me(ctx):
    return ctx.author.id == 400822001930993674

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.command(name = "inspire")
async def inspire(message):
    quote = get_quote()
    await message.channel.send(quote)


@client.event
async def on_ready():
    print("the bot is ready")

@client.event
async def on_message(message):
    await client.process_commands(message)
    msg = message.content
    
    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(starter_encouragements))
    if any(word in msg for word in bad_words):
      await message.channel.send(insult_warning)

    # if message.author.id == 400822001930993674:
    #   if msg.startswith("$new"):
    #     encouraging_message = msg.split("$new ",1)[1]
    #     update_encouragements(encouraging_message)
    #     await message.channel.send("New encouraging message added.")



# @client.command()
# @commands.check(is_it_me)
# async def newencouragement(ctx):
#     encouraging_message = msg.split("$new ",1)[1]
#     update_encouragements(encouraging_message)
#     await message.channel.send("New encouraging message added.")
    


@client.command()
@commands.check(is_it_me)
async def test(ctx):
    await ctx.send(f'hi im {ctx.author}')

@client.command()
@commands.check(is_it_me)
async def mute(ctx):
    for x in ctx.message.guild.members:
        if x in ctx.message.author.voice.channel.members:
            if x == ctx.message.author:
                continue
            await x.edit(mute=True)

@client.command()
@commands.check(is_it_me)
async def unmute(ctx):
    for x in ctx.message.guild.members:
        if x in ctx.message.author.voice.channel.members:
            await x.edit(mute=False)

client.run(os.getenv('TOKEN'))
