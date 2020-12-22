# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')



@bot.command(name='Fact', help='Những kiến thức bổ ích của thầy Huấn')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'Manh Hung la mot con cho.',
        'Nhat dep trai vl.'
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

bot.run(TOKEN)