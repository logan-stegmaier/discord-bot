import discord 
import os 
from dotenv import load_dotenv 

load_dotenv('discord.env') 

source_server_id = 1004440666501300224  
target_server_id = 1158820053182054510  

source_server_channel_id = 1164935614219702343  
target_server_channel_id = 1164935756029120532  

intents = discord.Intents.all() 

list_of_other_channels = 1164935756029120532

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_message(message):
    if message.guild.id == source_server_id and message.channel.id == source_server_channel_id:
        target_guild = client.get_guild(target_server_id)
        target_channel = target_guild.get_channel(target_server_channel_id)

        if target_channel:
            embed = discord.Embed( 
                color=discord.Color.blue(),
                title=f'Server: {message.guild.name}',
                description=f'{message.content}'
            )

            embed.set_footer(text=f"{message.author.display_name} | Announcement")

            await target_channel.send(embed=embed)


client.run(os.getenv("DISCORD_TOKEN"))