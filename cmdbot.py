import asyncio, discord, re, subprocess # importing required modules

from discord.ext import commands
from discord.ext.commands import Bot

Client = discord.Client()
cmdbot = commands.Bot(command_prefix="util.", formatter=None)

token = 'BOT TOKEN'


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
			

cmdbot.run(token)