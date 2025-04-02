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

@client.command(name="dice")
async def roll_dice(ctx, sides: int):
    # Dicionário com os tipos de dados válidos
    valid_sides = {6, 8, 12, 20}
    
    if sides in valid_sides:
        result = random.randint(1, sides)
        await ctx.send(f"O resultado do dado de {sides} lados foi: {result}")
    else:
        await ctx.send("Escolha um dado de 6, 8, 12 ou 20 lados.")

    

client.run(TOKEN_KEY, log_handler=handler, root_logger=True)
