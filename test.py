import discord
import re
from discord.ext.commands import Bot
from discord import utils

import config

class MyClient(discord.Client):
    async def on_ready(self):
        print('I am ready to kill\'s')
        print('Available commands:\nХочу роль (Название роли)\nУбрать роль (Название роли)')
        
    async def on_message(self, message):
        if (message.author.id == 787636281831850034):
            return

        role_c = utils.get(message.guild.roles, id=config.ROLES['главарь'])
        is_boss = role_c in message.author.roles   
    
        give_pattern = re.compile(r'^Хочу роль (\w+)$')
        remove_pattern = re.compile(r'^Убрать роль (\w+)$')    
        try:
            if (re.match(give_pattern, message.content) is not None):
                if (not is_boss):
                    await message.channel.send('Пососи, у тебя нет прав')
                    return
                result = re.match(give_pattern, message.content)
                print(result.group(1))
                role = utils.get(message.guild.roles, id=config.ROLES[result.group(1)])
                await message.author.add_roles(role)
                print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(message.author, role))
                return
            elif (re.match(remove_pattern, message.content) is not None):
                if (not is_boss):
                    await message.channel.send('Пососи, у тебя нет прав')
                    return
                result = re.match(remove_pattern, message.content)
                role = utils.get(message.guild.roles, id=config.ROLES[result.group(1)])
                if (i for i in message.author.roles if i.id is role.id):
                    await message.author.remove_roles(role)
                    print('[SUCCESS] Role {1.name} removed from user {0.display_name}'.format(message.author, role))
                    return
            else: print('Сommand %s is not available' %message.content)
        except KeyError as e:
                print('[ERROR] KeyError, no role found for ' + message.content)
        except Exception as e:
                print(repr(e))


# RUN
client = MyClient()
client.run(config.TOKEN)
