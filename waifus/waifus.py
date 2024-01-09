from typing import Any, Final, Optional

import aiohttp
import discord
import orjson
from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.utils.chat_formatting import box
        
WAIFU_IM: Final[str] = "https://api.waifu.im/search"
ICON: Final[str] = "https://avatars.githubusercontent.com/u/91619079?s=200&v=4"

async def api_call(
                self, ctx
):
        await ctx.typing()
        async with self.session.get(WAIFU_IM) as response:
                if response.status != 200:
                        await ctx.send(
                                "Something went wrong while trying to contact the API."
                        )
                        return
                data = await response.json()
                for image in data['images']:
                        image = image['url']

async def embedgen(ctx) -> None:

        


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
                url = WAIFU_IM
                params = {'is_nsfw': 'true', 'included_tags': 'waifu'}

                async with self.session as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.colour = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text="Powered by waifu.im", icon_url=ICON)
                                        view = discord.ui.View()
                                        style = discord.ButtonStyle.grey
                                        image = discord.ui.Button(
                                                style=style,
                                                label="Open Image",
                                                url=image,
                                        )
                                        view.add_item(item=image)
                                        await ctx.send(embed=embed, view=view)


        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def maid(self, ctx):
                """Send a random maid image"""
                url = WAIFU_IM
                params = {'is_nsfw': 'true', 'included_tags': 'maid'}
                
                async with self.session as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.colour = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text="Powered by waifu.im", icon_url=ICON)
                                        view = discord.ui.View()
                                        style = discord.ButtonStyle.grey
                                        image = discord.ui.Button(
                                                style=style,
                                                label="Open Image",
                                                url=image,
                                        )
                                        view.add_item(item=image)
                                        await ctx.send(embed=embed, view=view)

        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def marin(self, ctx):
                """Send a random marin kitagawa image"""
                url = WAIFU_IM
                params = {'is_nsfw': 'true', 'included_tags': 'marin-kiyagawa'}
                
                async with self.session as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.colour = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text="Powered by waifu.im", icon_url=ICON)
                                        view = discord.ui.View()
                                        style = discord.ButtonStyle.grey
                                        image = discord.ui.Button(
                                                style=style,
                                                label="Open Image",
                                                url=image,
                                        )
                                        view.add_item(item=image)
                                        await ctx.send(embed=embed, view=view)


        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def mori(self, ctx):
                """Send a random mori calliope image"""
                url = WAIFU_IM
                params = {'is_nsfw': 'true', 'included_tags': 'mori-calliope'}
                
                async with self.session as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.colour = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text="Powered by waifu.im", icon_url=ICON)
                                        view = discord.ui.View()
                                        style = discord.ButtonStyle.grey
                                        image = discord.ui.Button(
                                                style=style,
                                                label="Open Image",
                                                url=image,
                                        )
                                        view.add_item(item=image)
                                        await ctx.send(embed=embed, view=view)

        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def raiden(self, ctx):
                """Send a random raiden shogun image"""
                url = WAIFU_IM
                params = {'is_nsfw': 'true', 'included_tags': 'raiden-shogun'}
                
                async with self.session as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.colour = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text="Powered by waifu.im", icon_url=ICON)
                                        view = discord.ui.View()
                                        style = discord.ButtonStyle.grey
                                        image = discord.ui.Button(
                                                style=style,
                                                label="Open Image",
                                                url=image,
                                        )
                                        view.add_item(item=image)
                                        await ctx.send(embed=embed, view=view)


        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def oppai(self, ctx):
                """Send a random oppai image"""
                url = WAIFU_IM
                params = {'is_nsfw': 'true', 'included_tags': 'oppai'}
                
                async with self.session as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.colour = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text="Powered by waifu.im", icon_url=ICON)
                                        view = discord.ui.View()
                                        style = discord.ButtonStyle.grey
                                        image = discord.ui.Button(
                                                style=style,
                                                label="Open Image",
                                                url=image,
                                        )
                                        view.add_item(item=image)
                                        await ctx.send(embed=embed, view=view)


        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def selfies(self, ctx):
                """Send a random selfies image"""
                url = WAIFU_IM
                params = {'is_nsfw': 'true', 'included_tags': 'selfies'}
                
                async with self.session as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.colour = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text="Powered by waifu.im", icon_url=ICON)
                                        view = discord.ui.View()
                                        style = discord.ButtonStyle.grey
                                        image = discord.ui.Button(
                                                style=style,
                                                label="Open Image",
                                                url=image,
                                        )
                                        view.add_item(item=image)
                                        await ctx.send(embed=embed, view=view)

        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def uniform(self, ctx):
                """Send a random uniform image"""
                url = WAIFU_IM
                params = {'is_nsfw': 'true', 'included_tags': 'uniform'}
                
                async with self.session as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.colour = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text="Powered by waifu.im", icon_url=ICON)
                                        view = discord.ui.View()
                                        style = discord.ButtonStyle.grey
                                        image = discord.ui.Button(
                                                style=style,
                                                label="Open Image",
                                                url=image,
                                        )
                                        view.add_item(item=image)
                                        await ctx.send(embed=embed, view=view)


        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def gif(self, ctx):
                """Send a random gif"""
                url = WAIFU_IM
                params = {'is_nsfw': 'true', 'gif': 'true'}
                
                async with self.session as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.colour = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text="Powered by waifu.im", icon_url=ICON)
                                        view = discord.ui.View()
                                        style = discord.ButtonStyle.grey
                                        image = discord.ui.Button(
                                                style=style,
                                                label="Open Image",
                                                url=image,
                                        )
                                        view.add_item(item=image)
                                        await ctx.send(embed=embed, view=view)



        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def ass(self, ctx):
                """Send a random ass image"""
                url = WAIFU_IM
                params = {'is_nsfw': 'true', 'included_tags': 'ass'}
                
                async with self.session as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.colour = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text="Powered by waifu.im", icon_url=ICON)
                                        view = discord.ui.View()
                                        style = discord.ButtonStyle.grey
                                        image = discord.ui.Button(
                                                style=style,
                                                label="Open Image",
                                                url=image,
                                        )
                                        view.add_item(item=image)
                                        await ctx.send(embed=embed, view=view)
                await ctx.send(embed=embed, view=view)


        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def hentai(self, ctx):
                """Send a random hentai image"""
                url = WAIFU_IM
                params = {'is_nsfw': 'true', 'included_tags': 'hentai'}
                
                async with self.session as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.colour = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text="Powered by waifu.im", icon_url=ICON)
                                        view = discord.ui.View()
                                        style = discord.ButtonStyle.grey
                                        image = discord.ui.Button(
                                                style=style,
                                                label="Open Image",
                                                url=image,
                                        )
                                        view.add_item(item=image)
                                        await ctx.send(embed=embed, view=view)



        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def milf(self, ctx):
                """Send a random milf image"""
                url = WAIFU_IM
                params = {'is_nsfw': 'true', 'included_tags': 'milf'}
                
                async with self.session as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.colour = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text="Powered by waifu.im", icon_url=ICON)
                                        view = discord.ui.View()
                                        style = discord.ButtonStyle.grey
                                        image = discord.ui.Button(
                                                style=style,
                                                label="Open Image",
                                                url=image,
                                        )
                                        view.add_item(item=image)
                                        await ctx.send(embed=embed, view=view)



        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def oral(self, ctx):
                """Send a random oral image"""
                url = WAIFU_IM
                params = {'is_nsfw': 'true', 'included_tags': 'oral'}
                
                async with self.session as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.colour = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text="Powered by waifu.im", icon_url=ICON)
                                        view = discord.ui.View()
                                        style = discord.ButtonStyle.grey
                                        image = discord.ui.Button(
                                                style=style,
                                                label="Open Image",
                                                url=image,
                                        )
                                        view.add_item(item=image)
                                        await ctx.send(embed=embed, view=view)

        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def paizuri(self, ctx):
                """Send a random paizuri image"""
                url = WAIFU_IM
                params = {'is_nsfw': 'true', 'included_tags': 'paizuri'}
                
                async with self.session as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.colour = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text="Powered by waifu.im", icon_url=ICON)
                                        view = discord.ui.View()
                                        style = discord.ButtonStyle.grey
                                        image = discord.ui.Button(
                                                style=style,
                                                label="Open Image",
                                                url=image,
                                        )
                                        view.add_item(item=image)
                                        await ctx.send(embed=embed, view=view)



        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def ecchi(self, ctx):
                """Send a random ecchi image"""
                url = WAIFU_IM
                params = {'is_nsfw': 'true', 'included_tags': 'ecchi'}
                
                async with self.session as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.colour = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text="Powered by waifu.im", icon_url=ICON)
                                        view = discord.ui.View()
                                        style = discord.ButtonStyle.grey
                                        image = discord.ui.Button(
                                                style=style,
                                                label="Open Image",
                                                url=image,
                                        )
                                        view.add_item(item=image)
                                        await ctx.send(embed=embed, view=view)



        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def ero(self, ctx):
                """Send a random ero image"""
                url = WAIFU_IM
                params = {'is_nsfw': 'true', 'included_tags': 'ero'}
                
                async with self.session as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.colour = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text="Powered by waifu.im", icon_url=ICON)
                                        view = discord.ui.View()
                                        style = discord.ButtonStyle.grey
                                        image = discord.ui.Button(
                                                style=style,
                                                label="Open Image",
                                                url=image,
                                        )
                                        view.add_item(item=image)
                                        await ctx.send(embed=embed, view=view)