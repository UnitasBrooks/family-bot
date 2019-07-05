#!/usr/bin/env python3
import discord
import random
from os import environ, path
from datetime import *
from time import sleep
TOKEN = environ.get("DISCORD_TOKEN")
client = discord.Client()
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

LIST_FILE = environ.get("LIST_FILE", "shop_list.txt")


class ShoppingList:
    def __init__(self):
        open(LIST_FILE, 'a+').close()

    def handle(self, message):
        if "!shop add" in message:
            new_message = message.replace("!shop add", "")
            return self.add(new_message)

        if "!shop list" in message:
            return self.list()

        if "!shop clear" in message:
            return self.clear()

    @staticmethod
    def add(message):
        with open(LIST_FILE, "a") as shop_list:
            shop_list.write(message + "\n")
        return f"added {message}!"

    @staticmethod
    def list():
        our_list = "Shopping list:\n"
        with open(LIST_FILE, "r") as shop_list:
            for item in shop_list.readline():
                our_list += item

        return our_list

    @staticmethod
    def clear():
        with open(LIST_FILE, "w") as shop_list:
            shop_list.truncate(0)
        return "Cleared!"


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

while True:
    try:
        client.loop.run_until_complete(client.start(TOKEN))
    except Exception as e:
        print(e)
    sleep(3)
