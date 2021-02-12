import discord
from discord import utils

import config


class MyClient(discord.Client):
    async def on_ready(self):
        print('1')

    async def on_message(self, message):
               # to do убрать лишние
        print('2')

        is_add = True
        if (message.content.startswith('Не'))
            is_add = False

        if 
        
        print()

        try:
            role = utils.get(message.guild.roles, id=config.ROLES[message.content])
            print('4')
            if(len([i for i in message.author.roles if i.id not in config.EXCROLES]) <= config.MAX_ROLES_PER_USER):
                await message.author.add_roles(role)
                print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(message.author, role))

        except KeyError as e:
            print('[ERROR] KeyError, no role found for ' + message.content)
        except Exception as e:
            print(repr(e))

# RUN
client = MyClient()
client.run(config.TOKEN)
