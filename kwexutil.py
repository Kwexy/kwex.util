from time import sleep
import discord
import datetime
import sys
import psutil
import subprocess
from discord.ext import commands

bot = commands.Bot(command_prefix="%")
activity = discord.Game(name = "Kwexy Utilities", type=3)
server_isrunning = False

TOKEN = "NICE TRY"

def getCommandInfo(ctx):
    print("COMMAND RECEIVED:", str.upper(ctx.message.content), "from", str(ctx.message.author.name), "on", datetime.datetime.now().strftime("%m/%d/%y @ %H:%M:%S"))

def displayError(errmsg):
    if errmsg != "":
        print("ERROR: ", errmsg, "\n")
    else:
        print("ERROR: Something went wrong. Please try again.\n")

@bot.event
async def on_ready():
    await bot.change_presence(activity=activity)
#    channel = bot.get_channel(1014391874842267658)
#    await channel.send("message goes here")

@bot.command(pass_context=True)
async def start(ctx):
    getCommandInfo(ctx)
    global server_isrunning
    if server_isrunning == False:
        global p
        p = subprocess.Popen("java -jar" + "SERVER PATH GOES HERE")
        server_isrunning = True
    else:
        displayError("Something went wrong. Is the server already open?")

@bot.command(pass_context=True)
async def close(ctx):
    getCommandInfo(ctx)
    global server_isrunning
    try:
        children = psutil.Process(p.pid).children(recursive=True)
        for child in children:
            child.terminate()
            server_isrunning = False
            print("Server has been closed.")
    except:
        displayError("Something went wrong. Make sure the server is open before trying to close it.")

@bot.command()
async def restart(ctx):
    getCommandInfo(ctx)
    global server_isrunning
    if server_isrunning == True:
        await close(ctx)
        sleep(10)
        await start(ctx)
    else:
        displayError("Something went wrong. Make sure the server is open before trying to restart it.")

@bot.command()
async def kill(ctx):
    getCommandInfo(ctx)
    bot.close()
    print("Shutting Down...")
    sleep(2)
    sys.exit()

bot.run(TOKEN)
