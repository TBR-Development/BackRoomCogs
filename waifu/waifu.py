from redbot.core import commands, app_commands
from aiohttp import ClientSession
from discord import Embed

class Waifu(commands.Cog):
        """
        Get images from Waifu.IM API
        """

        def __init__(self, bot):
                self.bot = bot


                @commands.command()
                async def waifu(self, ctx):
                        url = 'https://api.waifu.im/search'
                        params = {'is_nsfw': 'false', 'gif': 'false'}

                        async with ClientSession() as cs:
                                async with cs.get(url, params=params) as response:
                                        if response.status == 200:
                                                data = await response.json()

                                                embed = Embed(title = f"{data['name']}", description = f"{data['description']}")
                                                embed.set_image(url = f"{data['url']}")
                                                
                                                await ctx.send(embed=embed)

                @commands.command()
                async def aniwaifu(self, ctx):
                        url = 'https://api.waifu.im/search'
                        params = {'is_nsfw': 'false', 'gif': 'true'}

                        async with ClientSession() as cs:
                                async with cs.get(url, params=params) as response:
                                        if response.status == 200:
                                                data = await response.json()

                                                embed = Embed(title = f"{data['name']}", description = f"{data['description']}")
                                                embed.set_image(url = f"{data['url']}")
                                                
                                                await ctx.send(embed=embed)


                @commands.command()
                @commands.is_nsfw()
                async def lewds(self, ctx):
                        url = 'https://api.waifu.im/search'
                        params = {'is_nsfw': 'true', 'gif': 'false'}

                        async with ClientSession() as cs:
                                async with cs.get(url, params=params) as response:
                                        if response.status == 200:
                                                data = await response.json()

                                                embed = Embed(title = f"{data['name']}", description = f"{data['description']}")
                                                embed.set_image(url = f"{data['url']}")
                                                
                                                await ctx.send(embed=embed)

                @commands.command()
                @commands.is_nsfw()
                async def anilewds(self, ctx):
                        url = 'https://api.waifu.im/search'
                        params = {'is_nsfw': 'true', 'gif': 'true'}

                        async with ClientSession() as cs:
                                async with cs.get(url, params=params) as response:
                                        if response.status == 200:
                                                data = await response.json()

                                                embed = Embed(title = f"{data['name']}", description = f"{data['description']}")
                                                embed.set_image(url = f"{data['url']}")
                                                
                                                await ctx.send(embed=embed)
