# Acta Mea by Alex Arbuckle #


from json import load, dump
from discord import Intents
from discord.ext.commands import Bot


actaMea = Bot(command_prefix = '', intents = Intents.all())
token = ''

@actaMea.command()
async def getServer(ctx, arg):
    ''' arg : string, server name '''

    # if user
    if ('Germx5000' in str(ctx.author)[:-5]):

        # load data
        with open('actaMea.json', 'r') as fileVariable:

            dictVariable = load(fileVariable)

        # if server exists
        if (arg in dictVariable.keys()):

            await ctx.send(await actaMea.get_channel(dictVariable[arg]).create_invite(),
                           delete_after = 60.0)

        else:

            await ctx.channel.send('{} does not exist.'.format(arg),
                                   delete_after = 60.0)


@actaMea.command()
async def setServer(ctx, arg):
    ''' arg : string, server name '''

    # if user
    if ('Germx5000' in str(ctx.author)[:-5]):

        # load data
        with open('actaMea.json', 'r') as fileVariable:

            dictVariable = load(fileVariable)

        # if server exists
        if (int(ctx.channel.id) in dictVariable.values()):

            await ctx.channel.send('{} already exists.'.format(arg),
                                   delete_after = 60.0)

        else:

            # add server
            dictVariable[arg] = int(ctx.channel.id)

            await ctx.channel.send('{} was added.'.format(arg))

        # dump data
        with open('actaMea.json', 'w') as fileVariable:

            dump(dictVariable,
                 fileVariable,
                 indent = 4)


actaMea.run(token)