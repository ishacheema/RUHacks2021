import discord
from discord.ext import commands
import os
import random
import json
import levelsys
import requests
import time
# client = discord.Client()
client = commands.Bot(command_prefix ='$')

# client = discord.Client()
client = commands.Bot(command_prefix ='$', intents=discord.Intents.all())

# teacher = '837914922872602664'
# student = '837915203680600065'
client.remove_command('help')



@client.event
async def on_ready():
    print("the bot is ready")

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]
bad_words = ["shut up", "stupid", "dumb", "idiot", "loser"] 

starter_encouragements = ["Cheer up!","Hang in there.", "You are a great person"]
insult_warning = 'Please dont send bad words in the channel!'

mentalhealthcheck = ["https://imgur.com/yZhyHnt"]
memes = ["https://imgur.com/a/G4u1wYx", "https://imgur.com/a/TbCHP8x", "https://imgur.com/a/gRi7g8l"]
starter_birthday = ['https://gph.is/g/ZyDkN2W','https://gph.is/g/4DBzNNB','https://gph.is/g/Zn6Gqv1']  
birthday_words = ["happy birthday"]  
random_music = [
    'https://open.spotify.com/playlist/4ci7ApVX6rfZrWvxLxuyKN?si=s6w0YsqARqCPcvPXmXOZFQ', 
    'https://open.spotify.com/playlist/471N195f5jAVs086lzYglw?si=zR3NXhj5QWKFG1CEi4zfEA',
    'https://open.spotify.com/playlist/3EeFSwtn0raqym85onHx3m?si=bJffd2iASPOTEjKOOUNfXQ',
    'https://open.spotify.com/playlist/1a8x5YMzKqAUbVuvatX0zN?si=YhZ_OaaQTVy4eDziF9gw4w',
    'https://open.spotify.com/playlist/2shCyIBFVF2nTUhCTGr6m0?si=u_-anTj4TV6ZPeuTrEhwdw',
    'https://open.spotify.com/playlist/3UTeUqSzaT1FMJtgw6hmRp?si=I5yMloTjQIWLXfDzcrdoXA',
    'https://open.spotify.com/playlist/0efhUK2KWCam94xnaaL1OK?si=7Pg7767aS16NlnpcUJF0cA', 
    'https://open.spotify.com/playlist/56GOn9QQ8kpbGv0vBjH6Ms?si=aicB9aD5Sw6--Lyl_BOheA']



# teacher = '837914922872602664'
# student = '837915203680600065'

# @client.event
# async def on_message(message):
#     msg = message.content
#     if any(word in msg for word in sad_words):
#       await message.channel.send(random.choice(starter_encouragements))
    
    # if any(word in msg for word in sad_words):
    #   await message.channel.send(insult_warning)
def is_it_me(ctx):
    return ctx.author.id == 599492681281830912

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
    
    if message.content.startswith('$resources'):
      await message.channel.send('**Please use the following commands to find your specified resource.**\n◦📈 mathhelp : Mathematics help.\n◦🧪 chemhelp : Chemistry help\n◦🧬 biohelp : Biology help.\n◦🧲 physicshelp : Physics help.\n◦ 📍`geohelp`: Geography help.\n◦ 📜 historyhelp : History help.\n')
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
        await message.channel.send('*BIOLOGY TEST:* ```\nDate: Wednesday, May 12, 2021\nTime: 1:30pm - 2:30 pm\nAdditional Note: Please be on time!```\n**ENGLISH ESSAY:**```\nDue Date: Friday May 28, 2021 \nTime: 11:59 pm \nAdditional Note: No late submissions will be accepted! ```')

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
    
    #memes and mental health check
    if message.content.startswith('$memes'):
      await message.channel.send(random.choice(memes))
    elif message.content.startswith('$mentalhealthcheck'):
      await message.channel.send(random.choice(mentalhealthcheck))
   
    #birthday
    msg = message.content

    if any(word in msg for word in birthday_words):
      await message.channel.send(random.choice(starter_birthday))  
    
    #calendar
    if message.content.startswith('$calendar'):
      await message.channel.send('**CALENDAR   **\n\n**Monday** - May 03\n```\n06:00 PM - 11:00 PM | Chemistry Tutor Session```\n**Tuesday** - May 04\n```\n02:00 PM - 4:00 PM  | RU Hacks```\n**Wednesday** - May 05\n```\n03:00 PM - 5:00 PM  | Face Paint and Activities Night\n09:00 PM - 12:00 AM | Movie Night```\n**Thursday** - May 05\n```\n02:00 PM - 7:00 PM  | Coding Competition\n08:00 PM - 9:00 PM  | Math Tutor Session\n09:00 PM - 10:00 PM | Biology Tutor Session```\n**Friday** - May 06\n```\n04:00 PM - 5:00 PM  | Mental Health Panel```\n**Saturday** - May 07\n```\n                          ```\n**Sunday** - May 08\n```\n04:00 PM - 5:00 PM | History Game Night```\n')
      
    #geoactivity
    geoactivity = ["https://imgur.com/iXJcvjj"]
    if message.content.startswith('$geoactivity'):
      await message.channel.send(random.choice(geoactivity))

    if message.content.startswith('$help'):
      await message.channel.send('**Here is a list of the possible commands you can use on this server.**\n◦ mathhelp.\n◦ chemhelp \n◦ biohelp\n◦ physicshelp\n◦ geohelp\n◦ historyhelp\n ◦ geoactivity\n ◦ inspire\n ◦ icebreaker\n ◦ reminders\n ◦ upcomingevents\n ◦ upcomingdeadlines\n ◦ calendar\n ◦ memes\n ◦ mentalhealthcheck\n ◦ poll\n ◦ music\n')

#test
@client.command()
@commands.check(is_it_me)
async def test(ctx):
    await ctx.send(f'hi im {ctx.author}')

@test.error
async def test(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('You dont need have permission to access this command. Sorry bud!')
#mute
@client.command()
@commands.check(is_it_me)
async def mute(ctx):
    for x in ctx.message.guild.members:
        if x in ctx.message.author.voice.channel.members:
            if x == ctx.message.author:
                continue
            await x.edit(mute=True)

@mute.error
async def test(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('You dont need have permission to access this command. Sorry bud!')

#unmute
@client.command()
@commands.check(is_it_me)
async def unmute(ctx):
    for x in ctx.message.guild.members:
        if x in ctx.message.author.voice.channel.members:
            await x.edit(mute=False)
@unmute.error
async def test(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('You dont need have permission to access this command. Sorry bud!')

@client.command()
async def poll(ctx,*, message):
    emb=discord.Embed(title = " POLL ❓", description=f"{message}")
    msg=await ctx.channel.send(embed=emb)
    await msg.add_reaction('1️⃣')
    await msg.add_reaction('2️⃣')
# @client.command()
# async def poll(ctx, title=None, option1=None, option2=None, option3=None):
#     em = discord.Embed(title=f"📊{title}", description="")
#     em.add_field(name="nothing", value=f"{option1} \n {option2} \n {option3}")
#     await ctx.send(embed=em)
@client.command(pass_context=True)
async def music(ctx, *args):
    await ctx.send("*Music:* \nEnjoy the tunes! \n" + random.choice(random_music))

# @client.event
# async def on_member_join(member):
#   with open('users.json', 'r') as f:
#       users = json.load(f)

#   await update_data(users, member)
  
#   with open('users.json', 'w') as f:
#     json.dump(users,f)

# @client.event
# async def on_message(message):
#     # if message.author == client.user:
#     #     return

#     with open('users.json', 'r') as f:
#         users = json.load(f)
    
#     await update_data(users, message.author)
#     await add_expereince(users, message.author,5)
#     await level_up(users, message.author, message.channel)

#     with open('users.json', 'w') as f:
#         json.dump(users,f)

# async def update_data(users,user):
#   if not user.id in users:
#     users[user.id] = {}
#     users[user.id]['experience'] = 0
#     users[user.id]['level'] = 1

# async def add_expereince(users,user,exp):
#     users[user.id]['experience'] += exp

# async def level_up(users,user,channel):
#   experience = users[user.id]['experience']
#   lvl_start = users[user.id]['level']
#   lvl_end = int(experience**(1/4))

#   if lvl_start < lvl_end:
#     await client.channel.send(channel, '{} has leveled up to {}'.format(user.mention, lvl_end))
#     users[user.id]['level'] = lvl_end


cogs = [levelsys]

for i in range(len(cogs)):
    cogs[i].setup(client)

# @client.command()
# @commands.check(is_it_me)
# async def mute(ctx):
#     for x in ctx.message.guild.members:
#         if x in ctx.message.author.voice.channel.members:
#             if x == ctx.message.author:
#                 continue
#             await x.edit(mute=True)

    # if message.content.startswith('$memes'):
    #   await message.channel.send(random.choice(memes))
    # elif message.content.startswith('$VirtualEscape'):
    #   await message.channel.send(random.choice(vescape))

# async def on_message(message):
  #   if message.content.startswith('!member'):

@client.command()
async def attendance(ctx):
 channel = client.get_channel(837895424328859691) #gets the channel you want to get the list from
 members = channel.members #finds members connected to the channel
 memids = [] #(list)
 for member in members:
   memids.append(client.get_user(member.id))
 f = open('attendees.txt', 'w')
 for i in range(len(memids)):
    j = memids[i]
    f.write(str(j))
    f.write('\n')

client.run('ODM3ODkyODc0MTE1NzQzNzc1.YIzKjA.nzRfh304FD9KS844CswpqTTyX0I')