from redbot.core import commands

# import aiohttp
# import asyncio
# import discord
# import json
# from io imort BytesIO

class Waifu(commands.Cog):
        """
        Get images from Waifu.IM API
        """

        def __init__(self, bot):
                self.bot = bot

                @commands.command()
                async def waifu(self, ctx):
                        url = 'https://api.waifu.im/search'

                        # Implement code for retreiving the image url from the response

                        await ctx.send(resp)

                @commands.command()
                @commands.is_nsfw()
                async def lewds(self, ctx):
                        url = 'https://api.waifu.im/search?is_nsfw=true'

                        # Implement code for retreiving the image url from the response

                        await ctx.send(resp)
                
                @commands.command()
                async def aniwaifu(self, ctx):
                        url = 'https://api.waifu.im/search?gif=true'

                        # Implement code for retreiving the image url from the response

                        await ctx.send(resp)
                
                @commands.command()
                @commands.is_nsfw()
                async def anilewds(self, ctx):
                        url = 'https://api.waifu.im/search?is_nsfw=true&gif=true'

                        # Implement code for retreiving the image url from the response

                        await ctx.send(resp)
                
                @commands.Cog.listener()
                async def on_command_error(self, ctx, error):
                        if isinstance(error, commands.errors.NSFWChannelRequired):
                                await ctx.send(f"Hey! {ctx.author.mention}, sorry but I can't submit nsfw content outside an nsfw channel.")