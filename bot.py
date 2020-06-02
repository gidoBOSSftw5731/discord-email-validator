# bot.py
import os
import random
import asyncio
import re

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

validation_tokens = {} # TODO: use a DB

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Send me your .edu email address to get a role'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel != message.author.dm_channel:
        return

    if 'token' in message.content:
        split = message.content.split(" ")
        if len(split) == 2 and split[0] == "token":
            check_token_and_give_role(message.author, split[1])
            return
    else:
        await parse_email_message(message)


    await message.author.dm_channel.send("Bad message")

def randomString(stringLength=40):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def get_role_for_domain(domain):
    # probably just want a map from domain to role,
    # loaded as json on start or something
    if domain == "osu.edu":
        return "The Ohio State University"
    else:
        return None

async def check_token_and_give_role(user, token):
    if user not in validation_tokens:
        await user.dm_channel.send("No awaiting validation")

    if validation[user][0] == token:
        # Valid token
        role = discord.utils.get(user.server.roles, name=validation[user][1])
        await client.add_roles(user, role)
        await user.dm_channel.send("done")
    else:
        await user.dm_channel.send("bad token")

async def parse_email_message(message):
    email_regex = re.compile("^[A-Za-z0-9\.\-\_]+@[A-Za-z\.\-]+.edu$")
    email_split = message.content.split("@")
    if not email_regex.match(message.content) or len(email_split) != 2:
        await message.author.dm_channel.send("invalid email")
        return

    domain = email_split[1]
    role = get_role_for_domain(domain)
    if role:
        random_token = randomString()
        validation_token[message.author.id] = (random_token, role)
        # TODO: Send email


        # TODO: Add rate limit for sending email
    else:
        await message.author.dm_channel.send("email domain is not known. message admins for help.")
        return



client.run(TOKEN)
