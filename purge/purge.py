

import discord

from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.utils.chat_formatting import box

class Purge(commands.Cog):
        """
        """

        __version__: Final[str] = "0.0.1"
        __author__: Final[str] = "PhantomNimbi"
        __repo__: Final[str] = "BackRoomCogs"

        def __init__(self, bot):
                self.bot = bot


        
        @commands.command(name="purge")
        @commands.bot_has_permissions(manage_messages=True, send_messages=True, embed_links=True)
        async def purge_amount(self, ctx, num_messages: int):
                """Purge <n> amount of messages from the current channel"""

                channel = ctx.message.channel

                await ctx.message.delete()
                await channel.purge(limit=num_messages)
                return True
        