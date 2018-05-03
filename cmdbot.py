import asyncio, discord, re, subprocess # importing required modules

from discord.ext import commands
from discord.ext.commands import Bot

Client = discord.Client()
cmdbot = commands.Bot(command_prefix="util.", formatter=None)

token = 'BOT TOKEN'

cmdbot.remove_command('help')

@cmdbot.command(pass_context=True)
async def help(ctx): #main help command
    if ctx.message.author.id == "YOUR ID":
        embed = discord.Embed(title="CMD-Bot", color=0xfff542) # formatting help embed message
        embed.add_field(name="```util.cmd <command>```", value="Will execute CMD command.", inline=False) # formatting help embed message 2
        embed.add_field(name="```util.help```", value="Will show help embed message.", inline=False) # formatting help embed message 3
        await cmdbot.send_message(ctx.message.channel, embed=embed) # sending embed message
    elif ctx.message.author.id != "YOUR ID":
        embed = discord.Embed(title="CMD-Bot", color=0xFF0000) # formatting embed message
        embed.add_field(name="You are not allowed to execute cmd.util command.", value="Only bot's owner is able to do this.", inline=True) # formatting embed message 2
        await cmdbot.send_message(ctx.message.channel, embed=embed) # sending embed message



@cmdbot.command(pass_context=True)
async def cmd(ctx): # bot command
    if ctx.message.author.id == "YOUR ID": # check message author id before executing cmd command
        command = ''.join(re.findall('util.cmd (.*)', ctx.message.content)) # find all util.cmd <message content> and write it to variable
        try: # try this stuff
            byte_data=subprocess.check_output(command,shell=True) # check output of cmd.exe
            str_data = byte_data.decode('866', errors='ignore') # cyrillic support and decoding errors ignoring
            data_arr=str_data.split() # split data
            if str_data != "": # check if string data is empty
                await cmdbot.send_message(ctx.message.channel, '```'+str_data+'```') # finally send message
        except Exception as ex: # excepting exceptions as ex...
            template = "An exception of type {0} occurred. Arguments:\n{1!r}" # template message of exception type and args
            message = template.format(type(ex).__name__, ex.args) # formatting template
            await cmdbot.send_message(ctx.message.channel, '```'+message+'```') # send exception message
    elif ctx.message.author.id != "YOUR ID": # if somebody is executing CMD-Bot command
        embed = discord.Embed(title="CMD-Bot", color=0xFF0000) # formatting embed message
        embed.add_field(name="You are not allowed to execute cmd.util command.", value="Only bot's owner is able to do this.", inline=True) # formatting embed message 2
        await cmdbot.send_message(ctx.message.channel, embed=embed) # sending embed message
			

cmdbot.run(token)
