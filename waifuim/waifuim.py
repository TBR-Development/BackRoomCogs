from typing import Final

import aiohttp
import discord

from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.utils.chat_formatting import box

ICON: Final[str] = "https://avatars.githubusercontent.com/u/91619079?s=200&v=4"

BANNER: Final[str] = "https://www.waifu.im/preview/7892/"

FOOTER_TEXT = "Powered by Waifu.IM API"

SFW_COMMANDS: Final[str] = "waifu, maid, marin, mori, raiden, selfies, uniform, gif"
  
NSFW_COMMANDS: Final[str] = "nwaifu, nmaid, nmarin, nmori, nraiden, nselfies, nuniform, ngif, ass, hentai, milf, oral, paizuri, ecchi, ero, oppai"

class Waifu(commands.Cog):
        """
        Get images from Waifu.IM API
        """

        def __init__(self, bot):
                self.bot = bot
                self.session: aiohttp.ClientSession = aiohttp.ClientSession()

        async def cog_unload(self) -> None:
                self.session.close()
        


        @commands.group()
        @commands.bot_has_permissions(send_messages=True, embed_links=True)
        async def waifuim(self, ctx):
          if ctx.invoked_subcommand is None:
            
            embed = new discord.Embed()
            embed.title('WaifuIM')
            embed.description('Get waifu images from Waifu.IM API.')
            embed.add_field(name='SFW Commands', value=SFW_COMMANDS, inline=False)
            embed.add_field(name='NSFW Commands', value=NSFW_COMMANDS, inline=False)
            embed.set_thumbnail(url=ICON)
            embed.set_image(url=BANNER)
            embed.color = await ctx.embed_color()
            embed.set_footer(text=FOOTER_TEXT, icon_url=ICON)
            await ctx.send(embed=embed)

        @waifuim.command()
        async def waifu(self, ctx):
                """Get a random waifu image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'waifu'}

                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
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


        @waifuim.command()
        async def maid(self, ctx):
                """Get a random maid image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'maid'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
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

        @waifuim.command()
        async def marin(self, ctx):
                """Get a random Marin Kitagawa image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'marin-kitagawa'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
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


        @waifuim.command()
        async def mori(self, ctx):
                """Get a random Mori Calliope image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'mori-calliope'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
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

        @waifuim.command()
        async def raiden(self, ctx):
                """Get a random Raiden Shogun image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'raiden-shogun'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
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



        @waifuim.command()
        async def selfies(self, ctx):
                """Get a random selfies image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'selfies'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
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

        @waifuim.command()
        async def uniform(self, ctx):
                """Get a random uniform image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'uniform'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
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


        @waifuim.command()
        async def gif(self, ctx):
                """Get a random gif image"""
                
                url = "https://api.waifu.im/search"
                params = {'gif': 'true'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
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



        @waifuim.command()
        @commands.is_nsfw()
        async def ass(self, ctx):
                """Get a random ass image"""
                
                url = "https://api.waifu.im/search"
                params = {'is_nsfw': 'true', 'included_tags': 'ass'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
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


        @waifuim.command()
        @commands.is_nsfw()
        async def hentai(self, ctx):
                """Get a random hentai image"""
                
                url = "https://api.waifu.im/search"
                params = {'is_nsfw': 'true', 'included_tags': 'hentai'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
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



        @waifuim.command()
        @commands.is_nsfw()
        async def milf(self, ctx):
                """Get a random milf image"""
                
                url = "https://api.waifu.im/search"
                params = {'is_nsfw': 'true', 'included_tags': 'milf'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
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



        @waifuim.command()
        @commands.is_nsfw()
        async def oral(self, ctx):
                """Get a random oral image"""
                
                url = "https://api.waifu.im/search"
                params = {'is_nsfw': 'true', 'included_tags': 'oral'}
                
                async with aiohttp.ClientSession()as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
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

        @waifuim.command()
        @commands.is_nsfw()
        async def paizuri(self, ctx):
                """Get a random paizuri image"""
                
                url = "https://api.waifu.im/search"
                params = {'is_nsfw': 'true', 'included_tags': 'paizuri'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
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



        @waifuim.command()
        @commands.is_nsfw()
        async def ecchi(self, ctx):
                """Get a random ecchi image"""

                url = "https://api.waifu.im/search"
                params = {'is_nsfw': 'true', 'included_tags': 'ecchi'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
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



        @waifuim.command()
        @commands.is_nsfw()
        async def ero(self, ctx):
                """Get a random ero image"""
                url = "https://api.waifu.im/search"
                params = {'is_nsfw': 'true', 'included_tags': 'ero'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
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

        @waifuim.command()
        @commands.is_nsfw()
        async def nwaifu(self, ctx):
                """Get a random nsfw waifu image"""
                
                url = "https://api.waifu.im/search"
                params = {'is_nsfw': 'true', 'included_tags': 'waifu'}

                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
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


        @waifuim.command()
        @commands.is_nsfw()
        async def nmaid(self, ctx):
                """Get a random nsfw maid image"""
                
                url = "https://api.waifu.im/search"
                params = {'is_nsfw': 'true', 'included_tags': 'maid'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
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

        @waifuim.command()
        @commands.is_nsfw()
        async def ngif(self, ctx):
                """Get a random  nsfw gif"""
                
                url = "https://api.waifu.im/search"
                params = {'is_nsfw': 'true', 'included_tags': 'gif'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
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

        @waifuim.command()
        @commands.is_nsfw()
        async def oppai(self, ctx):
                """Get a random oppai image"""
                
                url = "https://api.waifu.im/search"
                params = {'is_nsfw': 'true', 'included_tags': 'oppai'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
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

        @waifuim.command()
        @commands.is_nsfw()
        async def nselfies(self, ctx):
                """Get a random  nsfw selfies image"""
                
                url = "https://api.waifu.im/search"
                params = {'is_nsfw': 'true', 'included_tags': 'selfies'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
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

        @waifuim.command()
        @commands.is_nsfw()
        async def nuniform(self, ctx):
                """Get a random  nsfw uniform image"""
                
                url = "https://api.waifu.im/search"
                params = {'is_nsfw': 'true', 'included_tags': 'uniform'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
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
                                        
                                        
        @waifuim.command()
        @commands.is_nsfw()
        async def nmarin(self, ctx):
                """Get a random NSFW Marin Kitagawa image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'marin-kitagawa', 'is_nsfw': 'true'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
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
                                        
        @waifuim.command()
        @commands.is_nsfw()
        async def nmori(self, ctx):
                """Get a random NSFW Mori Calliope image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'mori-calliope', 'is_nsfw': 'true'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
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
                                        
                                        
                                                @waifuim.command()
                                                
        @waifuim.command()
        @commands.is_nsfw()
        async def nraiden(self, ctx):
                """Get a random NSFW Raiden Shogun image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'raiden-shogun', 'is_nsfw': 'true'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        embed = discord.Embed()
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