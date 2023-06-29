import requests
import json
import discord


async def lowest_bin(interaction: discord.Interaction, item_tag: str):
    link = f"https://sky.coflnet.com/api/auctions/tag/{item_tag}/active/bin"
    request = requests.get(link)
    api_data = request.json()

    for data in api_data:
        price = data.get('startingBid')
        is_bin = data.get('bin')

    if is_bin:
        await interaction.response.send_message(f"{interaction.user.mention}, the lowest bin I found for that item is"
                                                f" ${price}", ephemeral=True)
    else:
        await interaction.response.send_message(f"{interaction.user.mention}, the lowest bin I found for that item is"
                                                f"null", ephemeral=True)


def lowest_bin2(item_tag: str):
    link = f"https://sky.coflnet.com/api/auctions/tag/{item_tag}/active/bin"
    request = requests.get(link)
    api_data = request.json()

    for data in api_data:
        price = data.get('startingBid')
        is_bin = data.get('bin')
        price = str(price)

    if is_bin:
        print(price)
    else:
        print("error")

lowest_bin("FIERY_KUUDRA_CORE")

