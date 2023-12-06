from redbot.core import commands
import aiohttp
import discord

class Waifu(commands.Cog):
        """
        Get images from Waifu.IM API
        """

        def __init__(self, bot):
                self.bot = bot
               
                @commands.command()
                async def waifu(self, ctx):
                        url = 'https://api.waifu.im/search'

                        params = {
                                'gif': False,
                                'is_nsfw': False
                                }

                        async with aiohttp.ClientSession() as session:
                                async with session.get(url, params=params) as resp:
                                        img = await resp.read()
                                        with io.BytesIO(img) as file:
                                                await ctx.send(file=discord.File(file, img))
                        
                @commands.command()
                @commands.is_nsfw()
                async def nwaifu(self, ctx):
                        url = 'https://api.waifu.im/search'

                        params = {
                                'gif': False,
                                'is_nsfw': True
                                }

                        async with aiohttp.ClientSession() as session:
                                async with session.get(url, params=params) as resp:
                                        img = await resp.read()
                                        with io.BytesIO(img) as file:
                                                await ctx.send(file=discord.File(file, img))

                @commands.command()
                async def gif(self, ctx):
                        url = 'https://api.waifu.im/search'

                        params = {
                                'gif': True,
                                'is_nsfw': False
                        }

                        async with aiohttp.ClientSession() as session:
                                async with session.get(url, params=params) as resp:
                                        img = await resp.read()
                                        with io.BytesIO(img) as file:
                                                await ctx.send(file=discord.File(file, img))

                @commands.command()
                async def ngif(self, ctx):
                        url = 'https://api.waifu.im/search'

                        params = {
                                'gif': True,
                                'is_nsfw': True
                        }

                        async with aiohttp.ClientSession() as session:
                                async with session.get(url, params=params) as resp:
                                        img = await resp.read()
                                        with io.BytesIO(img) as file:
                                                await ctx.send(file=discord.File(file, img))

                @commands.Cog.listener()
                async def on_command_error(self, ctx):
                        if isinstance(error, commands.errors.NSFWChannelRequired):
                                msg.title = "NSFW Command"
                                msg.description = error.args[0]
                                return await ctx.send(embed=msg)