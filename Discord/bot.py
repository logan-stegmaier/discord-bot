import discord 
import discord.ext
from discord import app_commands
import os 
from dotenv import load_dotenv 

load_dotenv('discord.env') 

server_id = discord.Object(1158820053182054510)

intents = discord.Intents.all() 

client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

# sync the slash command to your server
@client.event
async def on_ready():
    await tree.sync(guild=server_id)
    print("Command is ready")

# make the slash command
@tree.command(name="council", description="The council will decide your fate.")
async def slash_command(interaction: discord.Interaction):    
    await interaction.response.send_message("The council has determined your fate.")

# run the bot
client.run(os.getenv("DISCORD_TOKEN"))