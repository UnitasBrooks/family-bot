#!/usr/bin/env python3
import discord
import random
from os import environ
from datetime import *
TOKEN = environ.get("DISCORD_TOKEN")
MESSAGES = [
    "Punching mom in the bladder.",
    "Sleeping.",
    "Practicing karate.",
    "Loving her parents and never doing anything wrong.",
    "Being roughly the size of a mango or larger",
    "Preparing her nobel prize acceptance speech",
    "Somersaults.",
    "Making cute faces.",
    "Gulpin' down fluids for practice",
    "Smashing the patriarchy",
    "Making a tiny little fist",
    "Punching mom in uterine wall",
    "Scrunching her little face and pouting",
    "Craving spicey food",
    "Playing the drums on Mom's uterus",
    "Eating through her belly button, but it's cute, forreal",
    "Listening to Dad rant about something, while rolling her tiny eyes",
    "Depriving mom of wine",
    "Depriving mom of Yoko's sushi",
    "Not giving a hoot about anything other than her uterhome",
    "Contemplating her existence, one second she wasn't and now she be?",
    "Patting herself on the back for winning the sperm race",
    "Getting stepped on by Dexter",
    "Wishing she had an iPad in her belly home",
    "Counting her tiny fingers and toes",
    "Eating her twin",
    "Wondering what Talia will eat next, so she can also eat it",
    "Swimmin' laps"
]


class ShoppingList:
    def __init__(self):
        self.shopping_list = []

    def handle(self, message):
        if "!shop add" in message:
            new_message = message.replace("!shop add", "")
            return self.add(new_message)

        if "!shop list" in message:
            new_message = message.replace("!shop list", "")
            return self.list(new_message)

        if "!shop clear" in message:
            return self.clear()

    def add(self, message):
        self.shopping_list.append(message)
        return f"added {message}!"

    def list(self, message):
        our_list = "Shopping list:\n"
        for item in self.shopping_list:
            our_list += item + "\n"

        return our_list

    def clear(self):
        self.shopping_list = []
        return "Cleared!"


client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!what is ellie') or message.content.startswith("!what's ellie"):
        msg = random.choice(MESSAGES)
        await client.send_message(message.channel, msg)

    if message.content.startswith("!days till"):
        today = date.today()
        future = date(2019, 9, 4)
        msg = str((future - today).days)
        await client.send_message(message.channel, msg)

    if message.content.startswith("!shop"):
        await client.send_message(message.channel, shopping_list.handle(message.content))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

shopping_list = ShoppingList()

client.run(TOKEN)
