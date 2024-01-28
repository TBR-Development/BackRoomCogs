

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
        async def purge(self, ctx, num_messages: int):
                """Purge <n> amount of messages from the current channel"""

                channel = ctx.message.channel

                await ctx.message.delete()
                await channel.purge(limit=num_messages)
                return True