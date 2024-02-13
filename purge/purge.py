

import discord
import asyncio

from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.utils.chat_formatting import box

class Purge(commands.Cog):
        """
        Simple purge command for Red DiscordBot
        """

        def __init__(self, bot):
                self.bot = bot


        
        @commands.command()
        @commands.bot_has_permissions(manage_messages=True, send_messages=True)
        @commands.has_permissions(manage_messages=True)
        async def purge(self, ctx, num_messages: int):
                """
                Purge <n> amount of messages from the current channel
                """
                
                channel = ctx.message.channel
                messages = await channel.purge(limit=num_messages)
                total_deleted = len(messages)
#                bot_deleted = await
#                user_deleted = await 
                
                embed = new discord.Embed()
                embed.title('Success')
                embed.description(f'**Messsges Deleted**: {total_deleted}')
                embed.add_field(name='Total', value: len(messages), inline=True)
#                embed.add_field(name='Bot', value=len(bot_deleted), inline=True)
#                embed.add_field(name='User', value=len(user_deleted), inline=True)
                  

                await ctx.message.delete()
                await asyncio.sleep(1)
                await channel.purge(limit=num_messages)
                await asyncio.sleep(2)
                return await ctx.send(embed=embed)