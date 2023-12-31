import discord
import random
import requests
from discord import app_commands
from discord.ext import commands
import randfacts
import json



def handle_response(message) -> str:
    p_message = message.content.lower()

    if p_message == "hello":
        return "Axe non"

    if p_message == "!rand":
        return str(random.randrange(1, 7))


async def send_message(message, response):
    try:
        if isinstance(message.channel, discord.DMChannel):
            await message.author.send(response)
        else:
            await message.channel.send(response)
    except Exception as e:
        print(e)


def run_bot():
    with open("token.json") as file:
        data = json.load(file)
        token = data["token"]

    client = commands.Bot(command_prefix="/", intents=discord.Intents.all())

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')
        try:
            synced = await client.tree.sync()
            print(f"synced {len(synced)} command(s)")
        except Exception as e:
            print(e)

    @client.event
    async def on_message(message):
        # Ignore messages sent by the bot itself to prevent a loop
        if message.author == client.user:
            return

        # Call the handle_response() function to generate a response
        response = handle_response(message)
        if response:
            await send_message(message, response)

    @client.tree.command(name="random_ass_fact", description="get a random ahhh fact")
    async def fact(interaction: discord.Interaction):
        randfact = randfacts.get_fact()
        await interaction.response.send_message(f"hey{interaction.user.mention}! Here is a random ass fact, {randfact}",
                                                ephemeral=True)

    @client.tree.command(name="say", description="say something")
    @app_commands.describe(thing_to_say="what should I say?")
    async def say(interaction: discord.Interaction, thing_to_say: str):
        await interaction.response.send_message(f"{interaction.user.name} said: 'thing_to_say")

    @client.tree.command(name="axe-non", description="Lucas is an axe non")
    async def send_file(ctx: commands.Context):
        with open("lucas.mp3", "rb") as f:
            file = discord.File(f)

        await ctx.response.send_message(file=file)

    @client.tree.command(name="we-live-in-a-society", description="BATMAN, We live in a society whe-")
    async def society(interaction: discord.Interaction):

        await interaction.response.send_message(f"We live in a society where... dave plays minecraft in class"
                                                , ephemeral=True)

    @client.tree.command(name="embed", description="embed a message")
    async def embed(interaction: discord.Interaction, embed_title: str, embed_description: str):
        embed_message = discord.Embed(title=embed_title, description=embed_description)
        await interaction.response.send_message(embed=embed_message)

    @client.tree.command(name="lowest-bin", description="find the lowest BIN price of an item on the ah")
    async def lowest_bin(interaction: discord.Interaction, item_tag: str):
        link = f"https://sky.coflnet.com/api/auctions/tag/{item_tag}/active/bin"
        request = requests.get(link)
        api_data = request.json()

        for data in api_data:
            price = data.get('startingBid')
            is_bin = data.get('bin')

        if is_bin:
            await interaction.response.send_message(
                f"{interaction.user.mention}, the lowest bin I found for that item is"
                f" ${price}", ephemeral=True)
        else:
            await interaction.response.send_message(
                f"{interaction.user.mention}, the lowest bin I found for that item is"
                f"null", ephemeral=True)

    client.run(token)
 