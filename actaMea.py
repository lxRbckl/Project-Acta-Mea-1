# Acta Mea by Alex Arbuckle #


from discord import utils
from json import load, dump
from discord import Intents
from discord.ext.commands import Bot


actaMea = Bot(command_prefix = '', intents = Intents.all())
token = ''


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

    if ('Germx5000' in str(member)[:-5]):

        await member.add_roles(utils.get(member.guild.roles, name = 'Admin'))


@actaMea.command(aliases = ['get', 'Get'])
async def getServer(ctx, arg):
    ''' arg : str '''

    if ('Germx5000' in str(ctx.author)[:-5]):

        dictVariable = await jsonLoad()

        if (arg in dictVariable.keys()):

            await ctx.send(await actaMea.get_channel(dictVariable[arg]).create_invite(), delete_after = 60)

        else:

            await ctx.channel.send('{} does not exist.'.format(arg), delete_after = 60)


@actaMea.command()
async def setServer(ctx, arg):
    ''' arg : str '''

    if ('Germx5000' in str(ctx.author)[:-5]):

        dictVariable = await jsonLoad()

        if (int(ctx.channel.id) in dictVariable.values()):

            del dictVariable[arg]

        dictVariable[arg] = int(ctx.channel.id)
        await jsonDump(dictVariable)

        await ctx.channel.send('{} was added.'.format(arg))


@actaMea.command(aliases = ['show', 'Show'])
async def showServer(ctx):
    '''  '''

    if ('Germx5000' in str(ctx.author)[:-5]):

        dictVariable = await jsonLoad()
        strVariable = ''.join('{}\n'.format(i) for i in dictVariable.keys())

        await ctx.channel.send(strVariable, delete_after = 60)


@actaMea.command(aliases = ['remove', 'Remove'])
async def removeServer(ctx, arg):
    ''' arg : str '''

    if ('Germx5000' in str(ctx.author)[:-5]):

        dictVariable = await jsonLoad()

        if (arg not in dictVariable.keys()):

            await ctx.channel.send('{} does not exist.'.format(arg), delete_after = 60)

        else:

            del dictVariable[arg]
            await jsonDump(dictVariable)

            await ctx.channel.send('{} was removed.'.format(arg), delete_after = 60)


actaMea.run(token)