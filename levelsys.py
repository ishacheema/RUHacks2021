import discord
from discord.ext import commands
from pymongo import MongoClient
bot_channel = 838460148766605363
talk_channel = [837895424328859690]

level = ["Good student", "Best student, awesome student"]

levelnum = [5,10,15]

cluster = MongoClient("mongodb+srv://harisz:12345@ruhacks2021bot.g6way.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

levelling = cluster["discord"]["levelling"]

class levelsys(commands.Cog):
  def _init_(self,client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print("ready")

  @commands.Cog.listener()  
  async def on_message(self,message):
    if message.channel.id in talk_channel:
      stats = levelling.find_one({"id" : message.author.id})
      if not message.author.bot:
        if stats is None:
          newuser = {"id" : message.author.id, "xp" : 100}
          levelling.insert_one(newuser)
        else:
          xp = stats["xp"] + 5
          levelling.update_one({"id" : message.author.id}, {"$set" : {"xp" : xp}})
          lvl = 0
          while True:
            if xp < ((50*(lvl**2))+(50*lvl)):
              break
            lvl += 1
          xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
          if (xp == 0):
            await message.channel.send(f"well done {message.author.mention}! You leveled up to **level: {lvl}**!")
            for i in range(len(level)):
              if lvl == levelnum[i]:
                await message.author.add_roles(discord.utils.get(message.author.guild.roles, name = level[i]))
                embed = discord.Embed(decription=f"{message.author.mention} you have gotten role **{level[i]}**!!!")
                embed.set_thumbnail(url=message.author.avatar_url)
                await message.channel.send(embed=embed)
            
  @commands.command()
  async def rank(self,ctx):
    if ctx.channel.id == bot_channel:
      stats = levelling.find_one({"id" : ctx.author.id})
      if stats is None:
        embed = discord.Embed(description = "you havent sent any messages, no rank!!")
        await ctx.channel.send(embed=embed)
      else:
        xp = stats("xp")
        lvl=0
        ranks=0
      while True:
        if xp < ((50*(lvl**2))+(50*lvl)):
          break
        lvl += 1
      xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
      boxes = int((xp/(200*((1/2)*lvl)))*20)
      rankings = levelling.find().sort("xp",-1)
      for x in rankings:
        rank +=1
        if stats["id"] == x["id"]:
          break
      embed = discord.Embed(title= "{}'s level stats'".format(ctx.author.name))
      embed.add_feild(name="Name", value=ctx.author.mention,inline=True)
      embed.add_feild(name="XP", value=f"{xp}/{int(200*((1/2)*lvl))}",inline=True)
      embed.add_feild(name="Rank", value=f"{rank}/{ctx.guild.member_count}",inline=True)
      embed.add_feild(name="Progress Bar {lvl}", value=boxes*":blue_squares:" + (20-boxes)*":white_large_squares:",inline=False)
      await ctx.channel.send(embed=embed)

  @commands.command()
  async def leaderboard(self,ctx):
    if (ctx.channel.id == bot_channel):
      rankings = levelling.find().zort("xp",-1)
      i=1
      embed = discord.Embed(title="Rankings:")
      for x in rankings:
        try:
          temp = ctx.guild.get_member(x["id"])
          tempxp = x["xp"]
          embed.add_feild(name=f"{i}:{temp.name}", value=f"Total XP: {tempxp}", inline=False)
          i +=1
        except:
          pass
        if i==11:
          break
      await ctx.channel.send(embed=embed)

def setup(client):
  client.add_cog(levelsys(client))