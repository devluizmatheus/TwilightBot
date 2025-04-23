from key_token import TOKEN_KEY
from discord.ext import commands
import random
import discord
import logging

# Configurações e ConexãoBot
PREFIX = "$"

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix=PREFIX, intents=intents)
handler = logging.FileHandler(filename='main.py', encoding='utf-8', mode='w')

@client.event
async def on_ready():
    print(f'Logado!! {client.user}')

@client.command(name="hello")
async def ping(ctx):
    await ctx.send("Olá sou o Bot do RPG")

@client.command(name="roll")
async def roll_dices(ctx, sides: str):
    result = await dices(ctx, sides)
    if result:
        await ctx.send(f"O resultado do lançamento foi: {result}")

async def dices(ctx, sides: str):

    dices = {'d4', 'd6', 'd8', 'd10', 'd12', 'd20', 'd100'}

    try:
        if sides[1:] in dices:
            numero_dados = int(sides[0])

            if sides[1:] == 'd4':
                result = numero_dados * (random.randint(1, 4))
                return result
            elif sides[1:] == 'd6':
                result = numero_dados * (random.randint(1, 6))
                return result
            elif sides[1:] == 'd8':
                result = numero_dados * (random.randint(1, 8))
                return result
            elif sides[1:] == 'd10':
                result = numero_dados * (random.randint(1, 12))
                return result
            elif sides[1:] == 'd12':
                result = numero_dados * (random.randint(1, 12))
                return result
            elif sides[1:] == 'd20':
                result = numero_dados * (random.randint(1, 20))
                return result
            elif sides[1:] == 'd100':
                result = numero_dados * (random.randint(1, 100))
                return result
        else:
            await ctx.send("Esse dado não está disponível use: d4, d6, d8, d10, d12, d20, d100")
            return None

    except ValueError:
        await ctx.send("Digite o número de dados que será rolado")
        return None


client.run(TOKEN_KEY, log_handler=handler, root_logger=True)
