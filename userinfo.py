import discord
import time
import datetime
import random
import typing
from discord.ext import commands
bot = commands.Bot(command_prefix='<custom-prefix>')
token = '<your token>'
bot.remove_command('help')
@bot.event
async def on_ready():
    print('-------') 
    print('im ready')
    print(bot.user.name)
    print(bot.user.id)
    print('-------')

@bot.command(name='userinfo')
async def userinfo(ctx, member: discord.Member):
    embed = discord.Embed(title= f'{member}', description=f'{member.mention}', color=0xedfb28)
    embed.add_field(name='**Username:**', value=member.name, inline=False)
    embed.add_field(name='**Discriminator:**', value=member.discriminator, inline=False)
    embed.add_field(name='**ID:**', value=member.id, inline=False)
    embed.add_field(name='**Status:**', value=member.status, inline=False)
    embed.add_field(name="**Highest Role:**", value=member.top_role, inline=False)
    embed.add_field(name='**Account Created:**', value=member.created_at.__format__('%A, %d. %B %Y | %H:%M:%S'), inline=False)
    embed.add_field(name='**Server Join Date:**', value=member.joined_at.__format__('%A, %d. %B %Y | %H:%M:%S'), inline=False)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text='©Role Adder')
    await ctx.send(content=None, embed=embed)

bot.run(token)