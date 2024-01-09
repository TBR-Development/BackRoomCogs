from typing import Any, Dict, Final, Optional

import aiohttp
import discord
import orjson
from redbot.core import commands
from redbot.core.bot imort Red
from redbot.core.utils.chat_formatting import box
        
WAIFU_IM: Final[str] = "https://api.waifu.im/search"
ICON: Final[str] = "https://avatars.githubusercontent.com/u/91619079?s=200&v=4"

async def api_call(
                self, ctx, endpoint: str
) -> Optional[Dict[str, Any]]:
        await ctx.typing()
        async with self.session.get(WAIFU_IM + endpoint) as response:
                if response.status != 200:
                        await ctx.send(
                                "Something went wrong while trying to contact the API."
                        )
                        return
                data = await response.read()
                url = orjson.loads(data)
                return url

async def embedgen(
                ctx, url: Dict[str, Any], endpoint: str
) -> None:
        result = url["results"][0]
        artist_name = result["artist_name"]
        source_url = result["source_url"]
        artist_href = result["artist_href"]
        image = result["url"]

        embed = discord.Embed(
                title=f"Here's a picture of a {endpoint}",
                description=f"**Artist:** [{artist_name}]({artist_href})\n**Source:** {source_url}",
                )
        embed.colour = await ctx.embed_color()
        embed.set_image(url=image)
        embed.set_footer(text="Powered byWaifu.IM", icon_url=ICON)
        view = discord.ui.View()
        style = discord.ButtonStyle.grey
        artist = discord.ui.Button(
                style=style,
                label="Artist",
                url=artist_href,
                )
        source = discord.ui.Button(
                style=style,
                label="Source",
                url=source_url,
                )
        image = discord.ui.Button(
                style=style,
                label="Open Image",
                url=image,
                )
        view.add_item(item=artist)
        view.add_item(item=source)
        view.add_item(item=image)
        await ctx.send(embed=embed, view=view)


class Waifus(commands.Cog):
        """
        Sends random images by tag from Waifu.IM
        """

        __version__: Final[str] = "0.1.20"
        __author__: Final[str] = "TBR Development"

        def __init__(self, bot):
                self.bot = bot
                self.session: aiohttp.ClientSession = aiohttp.ClientSession()

        async def cog_unload(self) -> None:
                self.session.close()

        def format_help_for_context(self, ctx) -> str:
                pre_processed = super().format_help_for_context(ctx)
                return f"{pre_processed}\n\nAuthor: {self.__author__}\nCog Version: {self.__version__}"
                
        async def red_delete_data_for_user(self, **kwargs: Any) -> None:
                return

        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.command(name="waifusversion", aliases=["waifusv"], hidden=True)
        async def waifus_version(self, ctx) -> None:
                """Shows the version of the cog"""
                version = self.__version__
                author = self.__author__

                embed = discord.Embed(
                        title="Cog Information",
                        description=box(
                                f"{'Cog Author':<11}: {author}\n{'Cog Version':<10}: {version}",
                                lang="yaml",
                        ),
                        color=await ctx.embed_color(),
                )
                await ctx.send(embed=embed)
                           
        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def waifu(self, ctx):
                """Send a random waifu image"""
                params = {'is_nsfw': 'true', 'included_tags': 'waifu'}

                url = await api_call(self, ctx, params)
                await embedgen(ctx, url, params)


        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def maid(self, ctx):
                """Send a random maid image"""
                params = {'is_nsfw': 'true', 'included_tags': 'maid'}

                url = await api_call(self, ctx, params)
                await embedgen(ctx, url, params)

        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def marin(self, ctx):
                """Send a random marin kitagawa image"""
                params = {'is_nsfw': 'true', 'included_tags': 'marin-kiyagawa'}

                url = await api_call(self, ctx, params)
                await embedgen(ctx, url, params)


        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def mori(self, ctx):
                """Send a random mori calliope image"""
                params = {'is_nsfw': 'true', 'included_tags': 'mori-calliope'}

                url = await api_call(self, ctx, params)
                await embedgen(ctx, url, params)

        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def raiden(self, ctx):
                """Send a random raiden shogun image"""
                params = {'is_nsfw': 'true', 'included_tags': 'raiden-shogun'}

                url = await api_call(self, ctx, params)
                await embedgen(ctx, url, params)


        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def oppai(self, ctx):
                """Send a random oppai image"""
                params = {'is_nsfw': 'true', 'included_tags': 'oppai'}

                url = await api_call(self, ctx, params)
                await embedgen(ctx, url, params)


        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def selfies(self, ctx):
                """Send a random selfies image"""
                params = {'is_nsfw': 'true', 'included_tags': 'selfies'}

                url = await api_call(self, ctx, params)
                await embedgen(ctx, url, params)

        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def uniform(self, ctx):
                """Send a random uniform image"""
                params = {'is_nsfw': 'true', 'included_tags': 'uniform'}

                url = await api_call(self, ctx, params)
                await embedgen(ctx, url, params)


        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def gif(self, ctx):
                """Send a random gif"""
                params = {'is_nsfw': 'true', 'gif': 'true'}

                url = await api_call(self, ctx, params)
                await embedgen(ctx, url, params)



        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def ass(self, ctx):
                """Send a random ass image"""
                params = {'is_nsfw': 'true', 'included_tags': 'ass'}

                url = await api_call(self, ctx, params)
                await embedgen(ctx, url, params)


        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def hentai(self, ctx):
                """Send a random hentai image"""
                params = {'is_nsfw': 'true', 'included_tags': 'hentai'}

                url = await api_call(self, ctx, params)
                await embedgen(ctx, url, params)



        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def milf(self, ctx):
                """Send a random milf image"""
                params = {'is_nsfw': 'true', 'included_tags': 'milf'}

                url = await api_call(self, ctx, params)
                await embedgen(ctx, url, params)



        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def oral(self, ctx):
                """Send a random oral image"""
                params = {'is_nsfw': 'true', 'included_tags': 'oral'}

                url = await api_call(self, ctx, params)
                await embedgen(ctx, url, params)

        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def paizuri(self, ctx):
                """Send a random paizuri image"""
                params = {'is_nsfw': 'true', 'included_tags': 'paizuri'}

                url = await api_call(self, ctx, params)
                await embedgen(ctx, url, params)



        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def ecchi(self, ctx):
                """Send a random ecchi image"""
                params = {'is_nsfw': 'true', 'included_tags': 'ecchi'}

                url = await api_call(self, ctx, params)
                await embedgen(ctx, url, params)



        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def ero(self, ctx):
                """Send a random ero image"""
                params = {'is_nsfw': 'true', 'included_tags': 'ero'}

                url = await api_call(self, ctx, params)
                await embedgen(ctx, url, params)