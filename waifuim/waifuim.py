from typing import Any, Final

import aiohttp
import discord
import datetime

from datetime import datetime
from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.utils.chat_formatting import box

ICON: Final[str] = "https://avatars.githubusercontent.com/u/91619079?s=200&v=4"

FOOTER_TEXT = "Powered by Waifu.IM API"

class WaifuIM(commands.Cog):
        """
        """

        __version__: Final[str] = "0.1.21"
        __author__: Final[str] = "PhantomNimbi"
        __repo__: Final[str] = "BackRoomCogs"

        def __init__(self, bot):
                self.bot = bot
                self.session: aiohttp.ClientSession = aiohttp.ClientSession()

        async def cog_unload(self) -> None:
                self.session.close()

        def format_help_for_context(self, ctx) -> str:
                pre_processed = super().format_help_for_context(ctx)
                return f"{pre_processed}\n\nAuthor: {self.__author__}\nCog Version: {self.__version__}\nRepo: {self.__repo__}"
                
        async def red_delete_data_for_user(self, **kwargs: Any) -> None:
                return


        
        @commands.hybrid_command(hidden=True)
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def waifu_version(self, ctx) -> None:
                """
                """
                version = self.__version__
                author = self.__author__

                embed = discord.Embed(title="Cog Information", description=box(f"{'Cog Author':<15}: {author}\n{'Cog Version':<15}: {version}\n{'Cog Repo':<15}: {self.__repo__}", lang="yaml"))
                embed.timestamp = datetime.now()
                embed.color = await ctx.embed_color()
                embed.set_footer(text=FOOTER_TEXT, icon_url=ICON)
                await ctx.send(embed=embed)

                           
        @commands.hybrid_command()
        @commands.bot_has_permissions(embed_links=True, send_messages=True)
        @commands.is_nsfw()
        async def waifu(self, ctx):
                """ 
                """
                url = "https://api.waifu.im/search"
                params = {'is_nsfw': 'true', 'included_tags': 'waifu'}

                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.timestamp = datetime.now()
                                        embed.color = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text=FOOTER_TEXT, icon_url=ICON)
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
                """
                """
                url = "https://api.waifu.im/search"
                params = {'is_nsfw': 'true', 'included_tags': 'maid'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.timestamp = datetime.now()
                                        embed.color = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text=FOOTER_TEXT, icon_url=ICON)
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
                """
                """
                url = "https://api.waifu.im/search"
                params = {'is_nsfw': 'true', 'included_tags': 'marin-kiyagawa'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.timestamp = datetime.now()
                                        embed.color = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text=FOOTER_TEXT, icon_url=ICON)
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
                """
                """
                url = "https://api.waifu.im/search"
                params = {'is_nsfw': 'true', 'included_tags': 'mori-calliope'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.timestamp = datetime.now()
                                        embed.color = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text=FOOTER_TEXT, icon_url=ICON)
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
                """
                """
                url = "https://api.waifu.im/search"
                params = {'is_nsfw': 'true', 'included_tags': 'raiden-shogun'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.timestamp = datetime.now()
                                        embed.color = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text=FOOTER_TEXT, icon_url=ICON)
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
                """
                """
                url = "https://api.waifu.im/search"
                params = {'is_nsfw': 'true', 'included_tags': 'oppai'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.timestamp = datetime.now()
                                        embed.color = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text=FOOTER_TEXT, icon_url=ICON)
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
                """
                """
                url = "https://api.waifu.im/search"
                params = {'is_nsfw': 'true', 'included_tags': 'selfies'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.timestamp = datetime.now()
                                        embed.color = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text=FOOTER_TEXT, icon_url=ICON)
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
                """
                """
                url = "https://api.waifu.im/search"
                params = {'is_nsfw': 'true', 'included_tags': 'uniform'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.timestamp = datetime.now()
                                        embed.color = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text=FOOTER_TEXT, icon_url=ICON)
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
                """
                """
                url = "https://api.waifu.im/search"
                params = {'is_nsfw': 'true', 'gif': 'true'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.timestamp = datetime.now()
                                        embed.color = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text=FOOTER_TEXT, icon_url=ICON)
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
                """
                """
                url = "https://api.waifu.im/search"
                params = {'is_nsfw': 'true', 'included_tags': 'ass'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.timestamp = datetime.now()
                                        embed.color = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text=FOOTER_TEXT, icon_url=ICON)
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
                """
                """
                url = "https://api.waifu.im/search"
                params = {'is_nsfw': 'true', 'included_tags': 'hentai'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.timestamp = datetime.now()
                                        embed.color = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text=FOOTER_TEXT, icon_url=ICON)
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
                """
                """
                url = "https://api.waifu.im/search"
                params = {'is_nsfw': 'true', 'included_tags': 'milf'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.timestamp = datetime.now()
                                        embed.color = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text=FOOTER_TEXT, icon_url=ICON)
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
                """
                """
                url = "https://api.waifu.im/search"
                params = {'is_nsfw': 'true', 'included_tags': 'oral'}
                
                async with aiohttp.ClientSession()as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.timestamp = datetime.now()
                                        embed.color = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text=FOOTER_TEXT, icon_url=ICON)
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
                url = "https://api.waifu.im/search"
                params = {'is_nsfw': 'true', 'included_tags': 'paizuri'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.timestamp = datetime.now()
                                        embed.color = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text=FOOTER_TEXT, icon_url=ICON)
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
                url = "https://api.waifu.im/search"
                params = {'is_nsfw': 'true', 'included_tags': 'ecchi'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.timestamp = datetime.now()
                                        embed.color = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text=FOOTER_TEXT, icon_url=ICON)
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
                url = "https://api.waifu.im/search"
                params = {'is_nsfw': 'true', 'included_tags': 'ero'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
                                        embed.timestamp = datetime.now()
                                        embed.color = await ctx.embed_color()
                                        embed.set_image(url=image)
                                        embed.set_footer(text=FOOTER_TEXT, icon_url=ICON)
                                        view = discord.ui.View()
                                        style = discord.ButtonStyle.grey
                                        image = discord.ui.Button(
                                                style=style,
                                                label="Open Image",
                                                url=image,
                                        )
                                        view.add_item(item=image)
                                        await ctx.send(embed=embed, view=view)