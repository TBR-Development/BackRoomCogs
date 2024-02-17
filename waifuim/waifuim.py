from typing import Final

import aiohttp
import discord

from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.utils.chat_formatting import box

footer_icon: Final[str] = "https://avatars.githubusercontent.com/u/91619079?s=200&v=4"
footer_text = "Powered by Waifu.IM API"

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
          return

        @waifuim.command()
        async def waifu(self, ctx):
                """Get a random waifu image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'waifu', 'gif': 'false', 'is_nsfw': 'false'}

                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        e = discord.Embed()
                                        e.color = await ctx.embed_color()
                                        e.set_image(url=image)
                                        e.set_footer(text=footer_text, icon_url=footer_icon)
                                        v = discord.ui.View()
                                        s = discord.ButtonStyle.grey
                                        i = discord.ui.Button(
                                                style=s,
                                                label="Open Image",
                                                url=image,
                                        )
                                        v.add_item(item=i)
                                        await ctx.send(embed=e, view=v)


        @waifuim.command()
        async def dump(self, ctx):
                """Dump a bunch of waifu images"""
                
                url = "https://api.waifu.im/search"
                params = {'many': 'true', 'gif': 'false', 'is_nsfw': 'false'}

                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        e = discord.Embed()
                                        e.color = await ctx.embed_color()
                                        e.set_image(url=image)
                                        e.set_footer(text=footer_text, icon_url=footer_icon)
                                        v = discord.ui.View()
                                        s = discord.ButtonStyle.grey
                                        i = discord.ui.Button(
                                                style=s,
                                                label="Open Image",
                                                url=image,
                                        )
                                        v.add_item(item=i)
                                        await ctx.send(embed=e, view=v)
        
        @waifuim.command()
        async def maid(self, ctx):
                """Get a random maid image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'maid', 'gif': 'false', 'is_nsfw': 'false'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        e = discord.Embed()
                                        e.color = await ctx.embed_color()
                                        e.set_image(url=image)
                                        e.set_footer(text=footer_text, icon_url=footer_icon)
                                        v = discord.ui.View()
                                        s = discord.ButtonStyle.grey
                                        i = discord.ui.Button(
                                                style=s,
                                                label="Open Image",
                                                url=image,
                                        )
                                        v.add_item(item=i)
                                        await ctx.send(embed=e, view=v)

        @waifuim.command()
        async def marin(self, ctx):
                """Get a random Marin Kitagawa image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'marin-kitagawa', 'gif': 'false', 'is_nsfw': 'false'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        e = discord.Embed()
                                        e.color = await ctx.embed_color()
                                        e.set_image(url=image)
                                        e.set_footer(text=footer_text, icon_url=footer_icon)
                                        v = discord.ui.View()
                                        s = discord.ButtonStyle.grey
                                        i = discord.ui.Button(
                                                style=s,
                                                label="Open Image",
                                                url=image,
                                        )
                                        v.add_item(item=i)
                                        await ctx.send(embed=e, view=v)


        @waifuim.command()
        async def mori(self, ctx):
                """Get a random Mori Calliope image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'mori-calliope', 'gif': 'false', 'is_nsfw': 'false'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        e = discord.Embed()
                                        e.color = await ctx.embed_color()
                                        e.set_image(url=image)
                                        e.set_footer(text=footer_text, icon_url=footer_icon)
                                        v = discord.ui.View()
                                        s = discord.ButtonStyle.grey
                                        i = discord.ui.Button(
                                                style=s,
                                                label="Open Image",
                                                url=image,
                                        )
                                        v.add_item(item=i)
                                        await ctx.send(embed=e, view=v)

        @waifuim.command()
        async def raiden(self, ctx):
                """Get a random Raiden Shogun image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'raiden-shogun', 'gif': 'false', 'is_nsfw': 'false'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        e = discord.Embed()
                                        e.color = await ctx.embed_color()
                                        e.set_image(url=image)
                                        e.set_footer(text=footer_text, icon_url=footer_icon)
                                        v = discord.ui.View()
                                        s = discord.ButtonStyle.grey
                                        i = discord.ui.Button(
                                                style=s,
                                                label="Open Image",
                                                url=image,
                                        )
                                        v.add_item(item=i)
                                        await ctx.send(embed=e, view=v)



        @waifuim.command()
        async def selfies(self, ctx):
                """Get a random selfies image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'selfies', 'gif': 'false', 'is_nsfw': 'false'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        e = discord.Embed()
                                        e.color = await ctx.embed_color()
                                        e.set_image(url=image)
                                        e.set_footer(text=footer_text, icon_url=footer_icon)
                                        v = discord.ui.View()
                                        s = discord.ButtonStyle.grey
                                        i = discord.ui.Button(
                                                style=s,
                                                label="Open Image",
                                                url=image,
                                        )
                                        v.add_item(item=i)
                                        await ctx.send(embed=e, view=v)

        @waifuim.command()
        async def uniform(self, ctx):
                """Get a random uniform image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'uniform', 'gif': 'false', 'is_nsfw': 'false'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        e = discord.Embed()
                                        e.color = await ctx.embed_color()
                                        e.set_image(url=image)
                                        e.set_footer(text=footer_text, icon_url=footer_icon)
                                        v = discord.ui.View()
                                        s = discord.ButtonStyle.grey
                                        i = discord.ui.Button(
                                                style=s,
                                                label="Open Image",
                                                url=image,
                                        )
                                        v.add_item(item=i)
                                        await ctx.send(embed=e, view=v)
                                        
        @waifuim.command()
        async def oppai(self, ctx):
                """Get a random oppai image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'oppai', 'gif': 'false', 'is_nsfw': 'false'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        e = discord.Embed()
                                        e.color = await ctx.embed_color()
                                        e.set_image(url=image)
                                        e.set_footer(text=footer_text, icon_url=footer_icon)
                                        v = discord.ui.View()
                                        s = discord.ButtonStyle.grey
                                        i = discord.ui.Button(
                                                style=s,
                                                label="Open Image",
                                                url=image,
                                        )
                                        v.add_item(item=i)
                                        await ctx.send(embed=e, view=v)
                                        
        @waifuim.command()
        async def gif(self, ctx):
                """Get a random gif image"""
                
                url = "https://api.waifu.im/search"
                params = {'gif': 'true', 'is_nsfw': 'false'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        e = discord.Embed()
                                        e.color = await ctx.embed_color()
                                        e.set_image(url=image)
                                        e.set_footer(text=footer_text, icon_url=footer_icon)
                                        v = discord.ui.View()
                                        s = discord.ButtonStyle.grey
                                        i = discord.ui.Button(
                                                style=s,
                                                label="Open Image",
                                                url=image,
                                        )
                                        v.add_item(item=i)
                                        await ctx.send(embed=e, view=v)



        @waifuim.command()
        @commands.is_nsfw()
        async def ass(self, ctx):
                """Get a random ass image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'ass', 'is_nsfw': 'true', 'gif': 'false'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        e = discord.Embed()
                                        e.color = await ctx.embed_color()
                                        e.set_image(url=image)
                                        e.set_footer(text=footer_text, icon_url=footer_icon)
                                        v = discord.ui.View()
                                        s = discord.ButtonStyle.grey
                                        i = discord.ui.Button(
                                                style=s,
                                                label="Open Image",
                                                url=image,
                                        )
                                        v.add_item(item=i)
                                        await ctx.send(embed=e, view=v)
                await ctx.send(embed=e, view=v)


        @waifuim.command()
        @commands.is_nsfw()
        async def hentai(self, ctx):
                """Get a random hentai image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'hentai', 'is_nsfw': 'true', 'gif': 'false'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        e = discord.Embed()
                                        e.color = await ctx.embed_color()
                                        e.set_image(url=image)
                                        e.set_footer(text=footer_text, icon_url=footer_icon)
                                        v = discord.ui.View()
                                        s = discord.ButtonStyle.grey
                                        i = discord.ui.Button(
                                                style=s,
                                                label="Open Image",
                                                url=image,
                                        )
                                        v.add_item(item=i)
                                        await ctx.send(embed=e, view=v)

        @waifuim.command()
        @commands.is_nsfw()
        async def milf(self, ctx):
                """Get a random milf image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'milf', 'is_nsfw': 'true', 'gif': 'false'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        e = discord.Embed()
                                        e.color = await ctx.embed_color()
                                        e.set_image(url=image)
                                        e.set_footer(text=footer_text, icon_url=footer_icon)
                                        v = discord.ui.View()
                                        s = discord.ButtonStyle.grey
                                        i = discord.ui.Button(
                                                style=s,
                                                label="Open Image",
                                                url=image,
                                        )
                                        v.add_item(item=i)
                                        await ctx.send(embed=e, view=v)

        @waifuim.command()
        @commands.is_nsfw()
        async def oral(self, ctx):
                """Get a random oral image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'oral', 'is_nsfw': 'true', 'gif': 'false'}
                
                async with aiohttp.ClientSession()as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        e = discord.Embed()
                                        e.color = await ctx.embed_color()
                                        e.set_image(url=image)
                                        e.set_footer(text=footer_text, icon_url=footer_icon)
                                        v = discord.ui.View()
                                        s = discord.ButtonStyle.grey
                                        i = discord.ui.Button(
                                                style=s,
                                                label="Open Image",
                                                url=image,
                                        )
                                        v.add_item(item=i)
                                        await ctx.send(embed=e, view=v)

        @waifuim.command()
        @commands.is_nsfw()
        async def paizuri(self, ctx):
                """Get a random paizuri image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'paizuri', 'is_nsfw': 'true', 'gif': 'false'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        e = discord.Embed()
                                        e.color = await ctx.embed_color()
                                        e.set_image(url=image)
                                        e.set_footer(text=footer_text, icon_url=footer_icon)
                                        v = discord.ui.View()
                                        s = discord.ButtonStyle.grey
                                        i = discord.ui.Button(
                                                style=s,
                                                label="Open Image",
                                                url=image,
                                        )
                                        v.add_item(item=i)
                                        await ctx.send(embed=e, view=v)

        @waifuim.command()
        @commands.is_nsfw()
        async def ecchi(self, ctx):
                """Get a random ecchi image"""

                url = "https://api.waifu.im/search"
                params = {'included_tags': 'ecchi', 'is_nsfw': 'true', 'gif': 'false'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        e = discord.Embed()
                                        e.color = await ctx.embed_color()
                                        e.set_image(url=image)
                                        e.set_footer(text=footer_text, icon_url=footer_icon)
                                        v = discord.ui.View()
                                        s = discord.ButtonStyle.grey
                                        i = discord.ui.Button(
                                                style=s,
                                                label="Open Image",
                                                url=image,
                                        )
                                        v.add_item(item=i)
                                        await ctx.send(embed=e, view=v)

        @waifuim.command()
        @commands.is_nsfw()
        async def ero(self, ctx):
                """Get a random ero image"""
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'ero', 'is_nsfw': 'true', 'gif': 'false'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        e = discord.Embed()
                                        e.color = await ctx.embed_color()
                                        e.set_image(url=image)
                                        e.set_footer(text=footer_text, icon_url=footer_icon)
                                        v = discord.ui.View()
                                        s = discord.ButtonStyle.grey
                                        i = discord.ui.Button(
                                                style=s,
                                                label="Open Image",
                                                url=image,
                                        )
                                        v.add_item(item=i)
                                        await ctx.send(embed=e, view=v)

        @waifuim.command()
        @commands.is_nsfw()
        async def nwaifu(self, ctx):
                """Get a random nsfw waifu image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'waifu', 'is_nsfw': 'true', 'gif': 'false'}

                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        e = discord.Embed()
                                        e.color = await ctx.embed_color()
                                        e.set_image(url=image)
                                        e.set_footer(text=footer_text, icon_url=footer_icon)
                                        v = discord.ui.View()
                                        s = discord.ButtonStyle.grey
                                        i = discord.ui.Button(
                                                style=s,
                                                label="Open Image",
                                                url=image,
                                        )
                                        v.add_item(item=i)
                                        await ctx.send(embed=e, view=v)

        @waifuim.command()
        @commands.is_nsfw()
        async def nmaid(self, ctx):
                """Get a random nsfw maid image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'maid', 'is_nsfw': 'true', 'gif': 'false'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        e = discord.Embed()
                                        e.color = await ctx.embed_color()
                                        e.set_image(url=image)
                                        e.set_footer(text=footer_text, icon_url=footer_icon)
                                        v = discord.ui.View()
                                        s = discord.ButtonStyle.grey
                                        i = discord.ui.Button(
                                                style=s,
                                                label="Open Image",
                                                url=image,
                                        )
                                        v.add_item(item=i)
                                        await ctx.send(embed=e, view=v)

        @waifuim.command()
        @commands.is_nsfw()
        async def ngif(self, ctx):
                """Get a random  nsfw gif"""
                
                url = "https://api.waifu.im/search"
                params = {'is_nsfw': 'true', 'gif': 'true'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        e = discord.Embed()
                                        e.color = await ctx.embed_color()
                                        e.set_image(url=image)
                                        e.set_footer(text=footer_text, icon_url=footer_icon)
                                        v = discord.ui.View()
                                        s = discord.ButtonStyle.grey
                                        i = discord.ui.Button(
                                                style=s,
                                                label="Open Image",
                                                url=image,
                                        )
                                        v.add_item(item=i)
                                        await ctx.send(embed=e, view=v)

        @waifuim.command()
        @commands.is_nsfw()
        async def noppai(self, ctx):
                """Get a random NSFW oppai image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'oppai', 'is_nsfw': 'true', 'gif': 'false'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        e = discord.Embed()
                                        e.color = await ctx.embed_color()
                                        e.set_image(url=image)
                                        e.set_footer(text=footer_text, icon_url=footer_icon)
                                        v = discord.ui.View()
                                        s = discord.ButtonStyle.grey
                                        i = discord.ui.Button(
                                                style=s,
                                                label="Open Image",
                                                url=image,
                                        )
                                        v.add_item(item=i)
                                        await ctx.send(embed=e, view=v)

        @waifuim.command()
        @commands.is_nsfw()
        async def nselfies(self, ctx):
                """Get a random  nsfw selfies image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'selfies', 'is_nsfw': 'true', 'gif': 'false'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        e = discord.Embed()
                                        e.color = await ctx.embed_color()
                                        e.set_image(url=image)
                                        e.set_footer(text=footer_text, icon_url=footer_icon)
                                        v = discord.ui.View()
                                        s = discord.ButtonStyle.grey
                                        i = discord.ui.Button(
                                                style=s,
                                                label="Open Image",
                                                url=image,
                                        )
                                        v.add_item(item=i)
                                        await ctx.send(embed=e, view=v)

        @waifuim.command()
        @commands.is_nsfw()
        async def nuniform(self, ctx):
                """Get a random  nsfw uniform image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'uniform', 'is_nsfw': 'true', 'gif': 'false'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        e = discord.Embed()
                                        e.color = await ctx.embed_color()
                                        e.set_image(url=image)
                                        e.set_footer(text=footer_text, icon_url=footer_icon)
                                        v = discord.ui.View()
                                        s = discord.ButtonStyle.grey
                                        i = discord.ui.Button(
                                                style=s,
                                                label="Open Image",
                                                url=image,
                                        )
                                        v.add_item(item=i)
                                        await ctx.send(embed=e, view=v)
                                        
                                        
        @waifuim.command()
        @commands.is_nsfw()
        async def nmarin(self, ctx):
                """Get a random NSFW Marin Kitagawa image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'marin-kitagawa', 'is_nsfw': 'true', 'gif': 'false'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        e = discord.Embed()
                                        e.color = await ctx.embed_color()
                                        e.set_image(url=image)
                                        e.set_footer(text=footer_text, icon_url=footer_icon)
                                        v = discord.ui.View()
                                        s = discord.ButtonStyle.grey
                                        i = discord.ui.Button(
                                                style=s,
                                                label="Open Image",
                                                url=image,
                                        )
                                        v.add_item(item=i)
                                        await ctx.send(embed=e, view=v)
                                        
        @waifuim.command()
        @commands.is_nsfw()
        async def nmori(self, ctx):
                """Get a random NSFW Mori Calliope image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'mori-calliope', 'is_nsfw': 'true', 'gif': 'false'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        e = discord.Embed()
                                        e.color = await ctx.embed_color()
                                        e.set_image(url=image)
                                        e.set_footer(text=footer_text, icon_url=footer_icon)
                                        v = discord.ui.View()
                                        s = discord.ButtonStyle.grey
                                        i = discord.ui.Button(
                                                style=s,
                                                label="Open Image",
                                                url=image,
                                        )
                                        v.add_item(item=i)
                                        await ctx.send(embed=e, view=v)

        @waifuim.command()
        @commands.is_nsfw()
        async def nraiden(self, ctx):
                """Get a random NSFW Raiden Shogun image"""
                
                url = "https://api.waifu.im/search"
                params = {'included_tags': 'raiden-shogun', 'is_nsfw': 'true', 'gif': 'false'}
                
                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        e = discord.Embed()
                                        e.color = await ctx.embed_color()
                                        e.set_image(url=image)
                                        e.set_footer(text=footer_text, icon_url=footer_icon)
                                        v = discord.ui.View()
                                        s = discord.ButtonStyle.grey
                                        i = discord.ui.Button(
                                                style=s,
                                                label="Open Image",
                                                url=image,
                                        )
                                        v.add_item(item=i)
                                        await ctx.send(embed=e, view=v)
                                        
        @waifuim.command()
        @commands.is_nsfw()
        async def ndump(self, ctx):
                """Dump a bunch of NSFW waifu images"""
                
                url = "https://api.waifu.im/search"
                params = {'many': 'true', 'is_nsfw': 'true', 'gif': 'false'}

                async with aiohttp.ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                data = await response.json()
                                for image in data['images']:
                                        image = image['url']
                                        e = discord.Embed()
                                        e.color = await ctx.embed_color()
                                        e.set_image(url=image)
                                        e.set_footer(text=footer_text, icon_url=footer_icon)
                                        
                                        v = discord.ui.View()
                                        s = discord.ButtonStyle.grey
                                        i = discord.ui.Button(
                                                style=s,
                                                label="Open Image",
                                                url=image,
                                        )
                                        v.add_item(item=i)
                                        await ctx.send(embed=e, view=v)