# bot.py
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord import Guild
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='fact', help='Những kiến thức bổ ích của thầy Huấn')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'Manh Hung la mot con cho.',
        'Nhat dep trai vl.'
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='dm', help='Những kiến thức bổ ích của thầy Huấn')
async def n2_nine(ctx):
    brooklyn_99_quotes = [
        'Manh Hung sua gau gau.'
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='handsome', help='Thu do dep trai cua ban.')
async def _bot(ctx):
    await ctx.send('Lai chang dep trai vl.')

# Basic Calculation
@bot.command(name='sub')
async def sub(ctx, x1: float, x2: float):
    """Subtract two numbers."""
    await ctx.send(x1 - x2)

@bot.command(name='mul')
async def mul(ctx, x1: float, x2: float):
    """Multiply two numbers.."""
    await ctx.send(x1 * x2)

@bot.command(name='add')
async def add(ctx, x1: float, x2: float):
    """Adds two numbers together."""
    await ctx.send(x1 + x2)

@bot.command(name='div')
async def div(ctx, x1: float, x2: float):
    if x2==0:
        await ctx.send('Chia con cac.')
    else:
        await ctx.send(x1 / x2)

@bot.command(name='bonk')
async def bonk(ctx):
    await ctx.send(file=discord.File('React/bonk.jpg'))

@bot.command(name='spam')
async def repeat(ctx, times: int):
    content = '{0} dep trai qua.'.format(ctx.author.name)
    if times<6:
        for _ in range(times):
            await ctx.send(content)



@bot.command(name='getter')



async def emoji_info(ctx):
    id = ctx.message.guild.id
    guild = bot.get_guild(id)
    emojiList = guild.emojis
    for e in emojiList:
        emojiString = ':'+e.name+':' + ''
        await ctx.send(emojiString)
bot.run(TOKEN)