import discord
from info import product

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.lower() == "привет":
        await message.channel.send(f'Привет! Я бот который говорит сколько разлагается какой-то материал,\n для помощи напишите слово помощь')
    elif  message.content.lower() == "помощь":
        text = "Доступные материалы:\nпластик ,стекло,метал,резина,другие отходы"
        await message.channel.send(text)
    elif message.content in product.keys():
        text = product[message.content]
        await message.channel.send(text)
    else:
        await message.channel.send("Я такого не знаю")
        
client.run("")
