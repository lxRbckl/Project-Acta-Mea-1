# Acta Mea by Alex Arbuckle #


# Import <
from discord import utils
from json import load, dump
from discord import Intents
from discord.ext.commands import Bot

# >


# Declaration <
admin = ''
actaMea = Bot(command_prefix = '', intents = Intents.all())
token = ''

# >


async def jsonLoad():
    '''  '''

    with open('actaMea.json', 'r') as fileVariable:

        return load(fileVariable)


async def jsonDump(arg):
    ''' arg : dict '''

    with open('actaMea.json', 'w') as fileVariable:

        dump(arg, fileVariable, indent = 4)


@actaMea.event
async def on_member_join(member):
    ''' member : class '''

    await member.add_roles(utils.get(member.guild.roles, name = 'Admin')) if (str(member) == admin) else (None)


@actaMea.command(aliases = ['get', 'Get'])
async def getServer(ctx, arg):
    ''' arg : str '''

    arg = arg.replace(' ', '-')
    dictVariable = await jsonLoad()

    if (arg in dictVariable.keys() and (admin == str(ctx.author))):

        await ctx.channel.send(await actaMea.get_channel(dictVariable[arg]).create_invite(), delete_after = 60)

    else:

        await ctx.channel.send(f'{arg} does not exist.', delete_after = 60)


@actaMea.command(aliases = ['set', 'Set'])
async def setServer(ctx, arg):
    ''' arg : str '''

    arg = arg.replace(' ', '-')
    dictVariable = await jsonLoad()

    if ((arg in dictVariable.keys()) and (admin == str(ctx.author))):

        await ctx.channel.send(f'{arg} already exists.', delete_after = 60)

    else:

        dictVariable[arg] = int(ctx.channel.id)

        await jsonDump(dictVariable)
        await ctx.channel.send(f'{arg} was added.', delete_after = 60)


@actaMea.command(aliases = ['show', 'Show'])
async def showServer(ctx):
    '''  '''

    dictVariable = await jsonLoad()
    strVariable = '\n'.join(f'{i}' for i in dictVariable.keys())

    await ctx.channel.send(strVariable, delete_after = 60) if (admin in str(ctx.author)) else (None)


@actaMea.command(aliases = ['remove', 'Remove'])
async def removeServer(ctx, arg):
    ''' arg : str '''

    dictVariable = await jsonLoad()

    if ((arg in dictVariable.keys()) and (admin == str(ctx.author))):

        del dictVariable[arg]

        await jsonDump(dictVariable)
        await ctx.channel.send(f'{arg} was removed.', delete_after = 60)

    else:

        await ctx.channel.send(f'{arg} does not exist.', delete_after = 60)


# Main <
if (__name__ == '__main__'):

    actaMea.run(token)

# >
