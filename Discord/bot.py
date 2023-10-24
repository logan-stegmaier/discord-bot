import discord
import os
import random
from dotenv import load_dotenv

load_dotenv('discord.env')

source_server_id = 1004440666501300224
target_server_id = 1158820053182054510

source_server_channel_id = 1164935614219702343
target_server_channel_id = 1164935756029120532

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "I'm upset", "not pogchamp", "kms", "stressed"]

starter_encouragements = [
    "Cheer up!",
    "Hang in there bestie.",
    "You are a great person!",
    "The horrors are only temporary.",
    "One step at a time, you got this!",
    "I'm proud of you! You're doing the best that you can.",
    "dont kys bestie, that ass is too phat to vanish",
    "Just remember: you have depression because you'd be too OP otherwise."
]

intents = discord.Intents.all()

client = discord.Client(intents=intents)

reaction_emoji = "✅"
role_name = "Code Master"

@client.event
async def on_ready():
    print('Bot is ready')

    channel_id = 1166027276572446760
    channel = client.get_channel(channel_id)

    existing_message = None
    limit = 100  # message count to check

    async for message in channel.history(limit=limit):  # loop through chat history
        if message.author == client.user and "React here to get your Code Master role!" in message.content:
            existing_message = message
            break

    if existing_message:
        print("Reaction role message already exists.")  # reaction msg exists
    else:  # creates
        Text = "React here to get your Code Master role!"
        Moji = await channel.send(Text)
        await Moji.add_reaction(reaction_emoji)
        print("Reaction role message created and sent.")
        
@client.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == reaction_emoji:
        role = discord.utils.get(user.guild.roles, name=role_name)
        await user.add_roles(role)

@client.event
async def on_reaction_remove(reaction, user):
    if reaction.emoji == reaction_emoji:
        role = discord.utils.get(user.guild.roles, name=role_name)
        await user.remove_roles(role)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if message.guild.id == source_server_id and message.channel.id == source_server_channel_id:
        target_guild = client.get_guild(target_server_id)
        target_channel = target_guild.get_channel(target_server_channel_id)

        if target_channel:
            embed = discord.Embed(
                color=discord.Color.blue(),
                title=f'{message.guild.name}',
                description=f'``{message.content}``'
            )

            # set the thumbnail to the user's avatar
            embed.set_thumbnail(url=message.author.avatar)

            embed.timestamp = message.created_at
            embed.set_footer(text=f"Announcement sent by {message.author.display_name}")

            await target_channel.send(embed=embed)

    if message.author.id == 579117588596916244:
        await message.channel.send('L')

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

client.run(os.getenv("DISCORD_TOKEN"))
