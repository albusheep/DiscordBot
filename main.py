import discord
from discord.ext import commands
import wolframalpha
import urbandictionary
import wikipedia
from googletrans import Translator
import random

HELP = """
```css\n
Welcome to Daddy's Little Bot!\n
Commands\n
.t Translate text to english\n
.w Summary of a Wikipedia article\n
.u Urban dictionary lookup\n
.c Calculator using WolframAlpha\n 
```\n"""

with open('token.txt', 'r') as TK:
    TOKEN = TK.readline().strip()
    WOLFRAM_ID = TK.readline().strip()
COMMAND_PREFIX = "."


# SET UP
bot = commands.Bot(command_prefix=COMMAND_PREFIX)
googleCloud = Translator()
calculator = wolframalpha.Client(WOLFRAM_ID)


# ON READY -> PRINT BOT INFORMATION
@bot.event
async def on_ready():
    print(f"Logged in as:\nUSER: {bot.user.name}\nID: {bot.user.id}\nDiscord V.{discord.__version__}\n")
    await bot.change_presence(game=discord.Game(name='Type .h for help!'))


# BOT COMMANDS
@bot.command(pass_context=True)
async def t(ctx, *, talk: str):
    await bot.say(googleCloud.translate(talk, 'en').text)


@bot.command(pass_context=True)
async def w(ctx, *, talk: str):
    await bot.say(wikipedia.summary(talk))


@bot.command(pass_context=True)
async def evil(ctx, *, talk: str):
    await bot.say(eval(talk))


@bot.command(pass_context=True)
async def c(ctx, *, talk: str):
    res = calculator.query(talk)
    await bot.say(next(res.results).text)


@bot.command(pass_context=True)
async def u(ctx, *, talk: str):
    x = urbandictionary.define(talk)
    num = random.randint(0, len(x) - 1)
    await bot.say(x[num])


@bot.command()
async def h():
    await bot.say(HELP)


def main():
    bot.run(TOKEN)


if __name__ == '__main__':
    main()