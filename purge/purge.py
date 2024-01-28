

from typing import Any, Final, Optional
from datetime import datetime, timedelta
from discord import errors, User, Forbidden, TextChannel, Embed

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

        def format_help_for_context(self, ctx) -> str:
                pre_processed = super().format_help_for_context(ctx)
                return f"{pre_processed}\n\nAuthor: {self.__author__}\nCog Version: {self.__version__}\nRepo: {self.__repo__}"
                
        async def red_delete_data_for_user(self, **kwargs: Any) -> None:
                return
        

        @commands.Group(invoke_without_commands=True)
        @commands.bot_has_permissions(manage_messages=True, send_messages=True, embed_links=True)
        async def purge(self, ctx):

                if ctx.subcommand_passed is None:
                        await ctx.send_help(ctx.command)
                elif ctx.invoked_subcommand is None:
                        await ctx.send(f"The subcommand {ctx.subcommand_passed} does not exist.")

        
        @purge.command(hidden=True)
        @commands.bot_has_permissions(manage_messages=True, send_messages=True, embed_links=True)
        async def version(self, ctx):

                version = self.__version__
                author = self.__author__

                embed = Embed(title="Cog Information", description=box(f"{'Cog Author':<15}: {author}\n{'Cog Version':<15}: {version}\n{'Cog Repo':<15}: {self.__repo__}", lang="yaml"))
                embed.timestamp = datetime.now()
                embed.color = await ctx.embed_color()
                await ctx.send(embed=embed)

        
        @purge.command()
        @commands.bot_has_permissions(manage_messages=True, send_messages=True, embed_links=True)
        async def purge(self, ctx, num_messages: int):

                channel = ctx.message.channel

                await ctx.message.delete()
                await channel.purge(limit=num_messages)
                return True
        
        @purge.command()
        @commands.bot_has_permissions(manage_messages=True, send_messages=True, embed_links=True)
        async def purge_until(self, ctx, message_id: int):

                channel = ctx.message.channel

                try:
                        message = await channel.fetch(message_id)
                except errors.NotFound:
                        await ctx.send('Message could not be found in this channel')
                
                await ctx.message.delete()
                await channel.purge(after=message)
                return True

        @purge.command()
        @commands.bot_has_permissions(manage_messages=True, send_messages=True, embed_links=True)
        async def purge_user(self, ctx, User: User, num_minutes: Optional[int] = 5):

                after = ctx.message.created_at - timedelta(minutes=num_minutes)

                def check(msg):
                        return msg.author.id == User.ID
                
                for channel in await ctx.guild.fetch_channels():
                        if type(channel) is TextChannel:
                                try:
                                        await channel.purge(limit=10*num_minutes, check=check, after=after)
                                except Forbidden:
                                        continue