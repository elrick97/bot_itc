import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "!")

queue = []

@client.event
async def on_ready():
    print("Bot ready")

@client.command()
async def hey(ctx):
    embed.add_field(name="Field1", value="hi", inline=False)
    embed.add_field(name="Field2", value="hi2", inline=False)
    await ctx.channel.send(embed=embed)
   
#TODO add admin only to clear

@client.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)


@client.command()
async def join(ctx):
    queue.append(ctx.message.author)
    embed = discord.Embed(title="Lista de Espera", description="Ayuda Inscripciones", color=0x00ff00)
    embed.set_footer(text="insertael comando `-join`")
    for i,student in enumerate(queue):
        embed.add_field(name=i+1 , value=student.mention, inline=False)
    await ctx.send(embed=embed)

@client.command()
async def leave(ctx):
    queue.remove(ctx.message.author)
    embed = discord.Embed(title="Lista de Espera", description="Ayuda Inscripciones", color=0x00ff00)
    embed.set_footer(text="insertael comando `-join`")
    for i,student in enumerate(queue):
        embed.add_field(name=i+1 , value=student.mention, inline=False)
    await ctx.send(embed=embed)

@client.command()
async def next(ctx, channel):
    user = queue[0]
    await user.move_member(channel)

client.run("NzI1MDY1OTM2NDk4OTgyOTEy.XvJauQ.4OMdWimq5UnwyeTNM8xT-rtpfsU")
