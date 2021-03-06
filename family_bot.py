#!/usr/bin/env python3
import discord
import random
from os import environ
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
RECIPES_FILE = environ.get("RECIPES_FILE", "recipes.txt")


class ShoppingList:
    def __init__(self):
        open(LIST_FILE, 'a+').close()
        open(RECIPES_FILE, 'a+').close()

    def handle(self, message):
        if "!shop add" in message:
            new_message = message.replace("!shop add ", "")
            return self.add(new_message)

        if "!shop list" in message:
            return self.list()

        if "!shop clear" in message:
            return self.clear()

        if "!shop remove" in message:
            message = message.replace("!shop remove ", "")
            return self.remove(message)

        if "!recipe add" in message:
            message = message.replace("!recipe add ", "")
            message = "++ " + message.replace('\n', ' ++', 1)
            return self.add(message, RECIPES_FILE)

        if "!recipe list" in message:
            return self.recipe_list()

        if "!recipe remove" in message:
            message = message.replace("!recipe remove ", "")
            self.recipe_remove(message)

        if "!recipe get" in message:
            message = message.replace("!recipe get ", "")
            self.recipe_get(message)

    @staticmethod
    def add(message, file_handler=LIST_FILE):
        with open(file_handler, "a") as shop_list:
            shop_list.write(message + "\n")
        return f"added {message}!"

    @staticmethod
    def recipe_list():
        items = "Recipes:\n"
        with open(RECIPES_FILE, "r") as recipe_list:
            for item in recipe_list.readlines():
                if "++" in item:
                    items += item
        return items

    @staticmethod
    def recipe_get(recipe_name):
        items = "Recipes:\n"
        seeking = False
        with open(RECIPES_FILE, "r") as recipe_list:
            for item in recipe_list.readlines():
                if seeking is True and "++" in item:
                    break
                if seeking is True:
                    items += item
                if "++" in item and recipe_name in item:
                    seeking = True
        return items

    @staticmethod
    def recipe_remove(recipe_name):
        seeking = False
        with open(RECIPES_FILE, "r+") as recipe_list:
            lines = recipe_list.readlines()
            recipe_list.seek(0)
            for line in lines:
                if seeking is True and "++" in line:
                    break
                if seeking is True:
                    continue
                if "++" in line and recipe_name in line:
                    seeking = True
                    continue
                recipe_list.write(line)
            recipe_list.truncate()

        if seeking is True:
            return f"Removed {recipe_name} from the list!"
        else:
            return f"Could not find {recipe_name} in the list"
        
    @staticmethod
    def list():
        our_list = "Shopping list:\n"
        with open(LIST_FILE, "r") as shop_list:
            for item in shop_list.readlines():
                our_list += item
        return our_list

    @staticmethod
    def remove(message):
        found = False
        with open(LIST_FILE, "r+") as shop_list:
            lines = shop_list.readlines()
            shop_list.seek(0)
            for line in lines:
                if line != "{message}\n":
                    shop_list.write(line)
                else:
                    found = True
            shop_list.truncate()

        if found is True:
            return f"Removed f{message} from the list!"
        else:
            return f"Could not find {message} in the list"

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

    if message.content.startswith("!shop") or message.content.startswith("!recipe"):
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
        client.close()
        print(e)
    sleep(3)
