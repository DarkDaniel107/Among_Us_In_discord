import discord
from PIL import Image
from discord.ext import commands
from PIL import *
import pickle
import render
import random
import asyncio
from DiscordGameEngine import collision

TOKEN = "NzY2NzIxMTU4MTU3Njk3MDU0.X4neuQ.upvwcJVs2sNauP83cV4CLTBjK1A"
intents = discord.Intents(members=True, messages=True, guilds=True, reactions=True)
bot = commands.Bot(command_prefix=',', intents=intents)

LetterList = ["A",
              "B",
              "C",
              "D",
              "E",
              "F",
              "G",
              "H",
              "I",
              "J",
              "K",
              "L",
              "M",
              "N",
              "O",
              "P",
              "Q",
              "R",
              "S",
              "T",
              "U",
              "V",
              "W",
              "X",
              "Y",
              "Z",
              ]

Messages = {
    "Host_gameend": "Forcefully disconnected from the server.\nHost requested a forceful Game End."

}

waitperframe = 0.5
Speed = 200

"""
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("I couldn't find the command you were looking for!")
    elif isinstance(error, commands.MissingPermissions):
        pass
    else:
        await ctx.send("Uh oh, a error occered!")
        await ctx.send("```" + str(error) + "```")
"""

try:
    savegame = pickle.load(open("savegame.bin", "rb"))
except EOFError:
    savegame = [[], []]


@bot.event
async def on_ready():
    print("CONNECTION")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=" over games..."))
    while True:
        for m in range(0, len(savegame[0])):
            for y in range(0, len(savegame[0][m][1])):
                if not savegame[0][m][1][y][1]:
                    Creater = bot.get_user(id=savegame[0][m][1][0][0])
                    await Creater.send(bot.get_user(id=savegame[0][m][1][y][0]).name + " has joined the game")
                    savegame[0][m][1][y][1] = True
        await asyncio.sleep(1)


@bot.command()
async def creategame(ctx):
    CODE = LetterList[random.randint(0, len(LetterList) - 1)] + \
           LetterList[random.randint(0, len(LetterList) - 1)] + \
           LetterList[random.randint(0, len(LetterList) - 1)] + \
           LetterList[random.randint(0, len(LetterList) - 1)] + \
           LetterList[random.randint(0, len(LetterList) - 1)] + \
           LetterList[random.randint(0, len(LetterList) - 1)]
    await ctx.author.send("Your code is: " + CODE)
    #            SERVER CODE,   Id, Is In?, Pos, Tasks
    savegame[0].append([CODE, [[ctx.author.id, True, 0, 0, []]], [False]])
    savegame[1].append([ctx.author.id, CODE])

    code = CODE
    index = -1
    for m in range(0, len(savegame[0])):
        if savegame[0][m][0] == code:
            index = m

    userindex = -1
    for m in range(0, len(savegame[0][index][1])):
        if savegame[0][index][1][m][0] == ctx.author.id:
            userindex = m

    while not savegame[0][index][2][0]:
        await asyncio.sleep(0.1)
    while True:
        await asyncio.sleep(waitperframe)
        render.Render(ctx, savegame[0][index][1][userindex][2], savegame[0][index][1][userindex][3], "VIEW")
        with open("./TEMP/" + str(ctx.author.id) + "GETMAPTESTTEMP.png", 'rb') as fp:
            await ctx.author.send(file=discord.File(fp, 'FullShipget.jpg'))
        if savegame[0][index][2][0]:
            break
    await ctx.author.send(Messages["Host_gameend"])


@bot.command()
async def join(ctx, code=None):
    index = -1
    for m in range(0, len(savegame[0])):
        if savegame[0][m][0] == code:
            index = m
    if index == -1:
        await ctx.author.send("Please enter a valid code.")
    else:
        savegame[0][index][1].append([ctx.author.id, False, 0, 0, []])
        savegame[1].append([ctx.author.id, code])
        await ctx.author.send("The game will start shortly")
        userindex = -1
        for m in range(0, len(savegame[0][index][1])):
            if savegame[0][index][1][m][0] == ctx.author.id:
                userindex = m
        while not savegame[0][index][2][0]:
            await asyncio.sleep(0.1)
        while True:
            await asyncio.sleep(waitperframe)
            render.Render(ctx, savegame[0][index][1][userindex][2], savegame[0][index][1][userindex][3], "VIEW")
            with open("./TEMP/" + str(ctx.author.id) + "GETMAPTESTTEMP.png", 'rb') as fp:
                await ctx.author.send(file=discord.File(fp, 'FullShipget.jpg'))
            if savegame[0][index][2][0]:
                break
        await ctx.author.send(Messages["Host_gameend"])


@bot.command()
async def getmap(ctx):
    Map = Image.open("FullShip.png")
    # 1540x865
    # 770x430
    mutiplyer = 3.5
    Map = Map.resize((int(1540 * mutiplyer), int(865 * mutiplyer)))
    im1 = Map.save("GETMAPTESTTEMP.png", fb="/TEMP")
    with open('GETMAPTESTTEMP.png', 'rb') as fp:
        await ctx.send(file=discord.File(fp, 'FullShipget.jpg'))


@bot.command()
async def viewmap(ctx, x, y):
    render.Render(ctx, int(x), int(y), "VIEW")
    with open("./TEMP/" + str(ctx.author.id) + "GETMAPTESTTEMP.png", 'rb') as fp:
        await ctx.send(file=discord.File(fp, 'FullShipget.jpg'))


@bot.command()
async def w(ctx):
    Index = -1
    for m in range(0, len(savegame[1])):
        if savegame[1][m][0] == ctx.author.id:
            CODE = savegame[1][m][1]
            for y in range(0, len(savegame[0])):
                print(savegame[0][y][0])
                if savegame[0][y][0] == CODE:
                    Index = y
    if Index == -1:
        await ctx.send("Make sure you are in a game first!")
    else:
        for m in range(0, len(savegame[0][Index][1])):
            if savegame[0][Index][1][m][0] == ctx.author.id:
                # x = 2
                # y = 3
                savegame[0][Index][1][m][3] -= Speed


@bot.command()
async def a(ctx):
    Index = -1
    for m in range(0, len(savegame[1])):
        if savegame[1][m][0] == ctx.author.id:
            CODE = savegame[1][m][1]
            for y in range(0, len(savegame[0])):
                if savegame[0][y][0] == CODE:
                    Index = y
    if Index == -1:
        await ctx.send("Make sure you are in a game first!")
    else:
        for m in range(0, len(savegame[0][Index][1])):
            if savegame[0][Index][1][m][0] == ctx.author.id:
                # x = 2
                # y = 3
                savegame[0][Index][1][m][2] -= Speed


@bot.command()
async def s(ctx):
    Index = -1
    for m in range(0, len(savegame[1])):
        if savegame[1][m][0] == ctx.author.id:
            CODE = savegame[1][m][1]
            for y in range(0, len(savegame[0])):
                if savegame[0][y][0] == CODE:
                    Index = y
    if Index == -1:
        await ctx.send("Make sure you are in a game first!")
    else:
        for m in range(0, len(savegame[0][Index][1])):
            if savegame[0][Index][1][m][0] == ctx.author.id:
                # x = 2
                # y = 3
                savegame[0][Index][1][m][3] += Speed


@bot.command()
async def d(ctx):
    Index = -1
    for m in range(0, len(savegame[1])):
        if savegame[1][m][0] == ctx.author.id:
            CODE = savegame[1][m][1]
            for y in range(0, len(savegame[0])):
                if savegame[0][y][0] == CODE:
                    Index = y
    if Index == -1:
        await ctx.send("Make sure you are in a game first!")
    else:
        for m in range(0, len(savegame[0][Index][1])):
            if savegame[0][Index][1][m][0] == ctx.author.id:
                # x = 2
                # y = 3
                savegame[0][Index][1][m][2] += Speed


@bot.command()
async def start(ctx):
    Index = -1
    for m in range(0, len(savegame[1])):
        if savegame[1][m][0] == ctx.author.id:
            CODE = savegame[1][m][1]
            for y in range(0, len(savegame[0])):
                if savegame[0][y][0] == CODE:
                    Index = y
    savegame[0][Index][2][0] = True


@bot.command()
async def endgame(ctx):
    Index = -1
    for m in range(0, len(savegame[1])):
        if savegame[1][m][0] == ctx.author.id:
            CODE = savegame[1][m][1]
            for y in range(0, len(savegame[0])):
                if savegame[0][y][0] == CODE:
                    Index = y
    savegame[0][Index][2][0] = False


bot.run(TOKEN)
