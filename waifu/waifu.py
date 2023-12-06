from redbot.core import commands

import json

class Waifu(commands.Cog):
        """
        Get images from Waifu.IM API
        """

        def __init__(self, bot):
                self.bot = bot

                @commands.command()
                async def waifu(self, ctx):
                        u = 'https://api.waifu.im/search'

                        data = json.loads(u.json())[0]
                        resp = data[0]['url']

                        await ctx.send(resp)

                @commands.command()
                @commands.is_nsfw()
                async def lewds(self, ctx):
                        u = 'https://api.waifu.im/search?is_nsfw=true'

                        data = json.loads(u.json())[0]
                        resp = data[0]['url']

                        await ctx.send(resp)
                
                @commands.command()
                async def aniwaifu(self, ctx):
                        u = 'https://api.waifu.im/search?gif=true'

                        data = json.loads(u.json())[0]
                        resp = data[0]['url']

                        await ctx.send(resp)
                
                @commands.command()
                @commands.is_nsfw()
                async def anilewds(self, ctx):
                        u = 'https://api.waifu.im/search?is_nsfw=true&gif=true'

                        data = json.loads(u.json())[0]
                        resp = data[0]['url']

                        await ctx.send(resp)
                
                @commands.Cog.listener()
                async def on_command_error(self, ctx, error):
                        if isinstance(error, commands.errors.NSFWChannelRequired):
                                await ctx.send(f"Hey! {ctx.author.mention}, sorry but I can't submit nsfw content outside an nsfw channel.")