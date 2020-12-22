# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

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
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'Manh Hung sua gau gau.'
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='handsome', help='Thu do dep trai cua ban.')
async def _bot(ctx):
    """Bot co dep trai khong?"""
    await ctx.send('Lai chang dep trai vl.')

@bot.command(name='add')
async def add(ctx, x1: int, x2: int):
    """Adds two numbers together."""
    await ctx.send(x1 + x2)

@bot.command(name='spam')
async def repeat(ctx, times: int):
    content = 'Nhat dep trai qua <3'
    for i in range(times):
        await ctx.send(content)

bot.run(TOKEN)