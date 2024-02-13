

import discord

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
        async def purge(self, ctx, num: int):
                """
                Purge <n> amount of messages from the current channel
                """
                
                channel = ctx.message.channel
                messages = await ctx.channel.purge(limit=num)
                total_deleted = len(messages)
                
                embed = new discord.Embed()
                embed.title('Success')
                embed.description('Purge completed successfully'.')
                embed.add_field(name='Total', value=f'{total_deleted}'', inline=True)
                  

                await ctx.message.delete()
                await channel.purge(limit=num)
                return await ctx.send(embed=embed)