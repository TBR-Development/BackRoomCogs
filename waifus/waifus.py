from redbot.core import commands, app_commands
from aiohttp import ClientSession
from discord import Embed

class Waifus(commands.Cog):
        """
        Get random images and gifs using waifu.im api
        """

        def __init__(self, bot):
                self.bot = bot


        @commands.command()
        async def waifu(self, ctx):
                """
                Get a random waifu image
                """
                url = 'https://api.waifu.im/search'
                params = {'is_nsfw': 'false', 'gif': 'false'}

                async with ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                if response.status != 200:
                                        error_embed = Embed(title = 'Command Error', description = 'Request failed with status code: ' + response.status)
                                        await ctx.send(embed=error_embed)
                                else:
                                        data = await response.json()
                                        for image in data['images']:

                                                image_url = image['url']
                                                
                                                embed = Embed(description = f":white_small_square: **Direct Link**: [waifu.im]({image_url})")
                                                embed.set_image(url = image_url)
                                                
                                                await ctx.send(embed=embed)


        @commands.command()
        async def aniwaifu(self, ctx):
                """
                Get a random waifu gif
                """
                url = 'https://api.waifu.im/search'
                params = {'is_nsfw': 'false', 'gif': 'true'}

                async with ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                if response.status != 200:
                                        error_embed = Embed(title = 'Command Error', description = 'Request failed with status code: ' + response.status)
                                        await ctx.send(embed=error_embed)
                                else:
                                        data = await response.json()
                                        for image in data['images']:

                                                image_url = image['url']
                                                
                                                embed = Embed(description = f":white_small_square: **Direct Link**: [waifu.im]({image_url})")
                                                embed.set_image(url = image_url)
                                                
                                                await ctx.send(embed=embed)


        @commands.command()
        @commands.is_nsfw()
        async def lewds(self, ctx):
                """
                Get a random NSFW waifu image
                """
                url = 'https://api.waifu.im/search'
                params = {'is_nsfw': 'true', 'gif': 'false'}

                async with ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                if response.status != 200:
                                        error_embed = Embed(title = 'Command Error', description = 'Request failed with status code: ' + response.status)
                                        await ctx.send(embed=error_embed)
                                else:
                                        data = await response.json()
                                        for image in data['images']:

                                                image_url = image['url']
                                                
                                                embed = Embed(description = f":white_small_square: **Direct Link**: [waifu.im]({image_url})")
                                                embed.set_image(url = image_url)
                                                
                                                await ctx.send(embed=embed)


        @commands.command()
        @commands.is_nsfw()
        async def anilewds(self, ctx):
                """
                Get a random NSFW waifu gif
                """
                url = 'https://api.waifu.im/search'
                params = {'is_nsfw': 'true', 'gif': 'true'}

                async with ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                if response.status != 200:
                                        error_embed = Embed(title = 'Command Error', description = 'Request failed with status code: ' + response.status)
                                        await ctx.send(embed=error_embed)
                                else:
                                        data = await response.json()
                                        for image in data['images']:

                                                image_url = image['url']
                                                
                                                embed = Embed(description = f":white_small_square: **Direct Link**: [waifu.im]({image_url})")
                                                embed.set_image(url = image_url)
                                                
                                                await ctx.send(embed=embed)