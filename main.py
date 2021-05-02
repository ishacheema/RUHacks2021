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

#inspirational quote
@client.command(name = "inspire")
async def inspire(message):
    quote = get_quote()
    await message.channel.send(quote)


@client.event
async def on_ready():
    print("the bot is ready")

#sad words and bad words command
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
    
    if message.content.startswith('$resources'):
      await message.channel.send('**Please use the following commands to find your specified resource.**\n◦📈 `mathhelp` : Mathematics help.\n◦🧪 `chemhelp` : Chemistry help\n◦🧬 `biohelp` : Biology help.\n◦🧲 `physicshelp` : Physics help.\n◦ 📍`geohelp`: Geography help.\n◦ 📜 `historyhelp` : History help.\n')
    elif message.content.startswith('$mathhelp'):
        await message.channel.send('1. https://mathworld.wolfram.com \n2. https://www.desmos.com \n3. https://www.symbolab.com')
    elif message.content.startswith('$chemhelp'):
        await message.channel.send('1. https://pubchem.ncbi.nlm.nih.gov/ \n2. http://www.chemcollective.org/ \n3. https://www.khanacademy.org/science/chemistry')
    elif message.content.startswith('$biohelp'):
        await message.channel.send('1. https://www.khanacademy.org/science/biology \n2. https://www.biologycorner.com/ \n3. https://www.nsf.gov/news/classroom/biology.jsp')
    elif message.content.startswith('$physicshelp'):
        await message.channel.send('1. https://www.physicsclassroom.com/ \n2. https://www.khanacademy.org/science/physics')
    elif message.content.startswith('$geohelp'):
        await message.channel.send('1. https://www.nationalgeographic.org/encyclopedia/geography/ \n2. https://www.google.com/maps')
    elif message.content.startswith('$historyhelp'):
        await message.channel.send('1. https://support.history.com/hc/en-us \n2. https://www.historians.org/')
    
     #reminders
    if message.content.startswith('$reminders'):
      await message.channel.send('**Please use the following commands to find your specified reminder.\n**\n◦ 📅`upcomingevents`: Stay updated about any important events happening this month.\n\n◦🔔`upcomingdeadlines` : Remember any important due dates for assignments, quizzes and tests.\n')
    elif message.content.startswith('$upcomingevents'):
        await message.channel.send('**SCIENCE FAIR:**```\nDate: Thursday, May 6, 2021\nTime: 1:00pm - 3:00 pm\nAdditional Note: Please be on time and do not forget your science textbooks!```\n**MATH CONTEST:**```\nDate: Saturday May 15, 2021 \nTime: 9:00am to 11:00 am \n Additional Note: Bring a pencil, calculator and a positive mindset! Dont be late! ```')
    elif message.content.startswith('$upcomingdeadlines'):
        await message.channel.send('**BIOLOGY TEST:** ```\nDate: Wednesday, May 12, 2021\nTime: 1:30pm - 2:30 pm\nAdditional Note: Please be on time!```\n**ENGLISH ESSAY:**```\nDue Date: Friday May 28, 2021 \nTime: 11:59 pm \nAdditional Note: No late submissions will be accepted! ```')

    #icebreakers
    if message.content.startswith('$icebreaker'):

      randomNumber = random.randint(1,7)

    if randomNumber == 1:
      await message.channel.send("If you were a vegetable, what vegetable would you be?")
    elif randomNumber == 2:
      await message.channel.send("Have you ever completed anything on your “bucket list”?")
    elif randomNumber == 3:
      await message.channel.send("If you were stranded on a desert island, what three items would you want to have with you?")
    elif randomNumber == 4:
      await message.channel.send("If you could hang out with any cartoon character, who would you choose and why?")
    elif randomNumber == 5:
      await message.channel.send("What book or movie have you read/seen recently that you would recommend and why?")
    elif randomNumber == 6:
      await message.channel.send("What’s your favorite tradition or holiday?")
    elif randomNumber == 7:
      await message.channel.send("If you could live in one fictional universe, which one would you choose?")



# @client.command()
# @commands.check(is_it_me)
# async def newencouragement(ctx):
#     encouraging_message = msg.split("$new ",1)[1]
#     update_encouragements(encouraging_message)
#     await message.channel.send("New encouraging message added.")
    
#test
@client.command()
@commands.check(is_it_me)
async def test(ctx):
    await ctx.send(f'hi im {ctx.author}')

#mute
@client.command()
@commands.check(is_it_me)
async def mute(ctx):
    for x in ctx.message.guild.members:
        if x in ctx.message.author.voice.channel.members:
            if x == ctx.message.author:
                continue
            await x.edit(mute=True)

#unmute
@client.command()
@commands.check(is_it_me)
async def unmute(ctx):
    for x in ctx.message.guild.members:
        if x in ctx.message.author.voice.channel.members:
            await x.edit(mute=False)

client.run(os.getenv('TOKEN'))
