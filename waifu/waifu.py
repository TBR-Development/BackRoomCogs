from redbot.core import commands

class Waifu(commands.Cog):
        """
        Get images from Waifu.IM API
        """

        def __init__(self, bot):
                self.bot = bot

                @commands.command()
                async def waifu(self, ctx):
                        await ctx.send('https://api.waifu.im/search')

                @commands.command()
                @commands.is_nsfw()
                async def lewds(self, ctx):
                        await ctx.send('https://api.waifu.im/search?is_nsfw=true')
                
                @commands.command()
                async def aniwaifu(self, ctx):
                        await ctx.send('https://api.waifu.im/search?gif=true')
                
                @commands.command()
                @commands.is_nsfw()
                async def anilewds(self, ctx):
                        await ctx.send('https://api.waifu.im/search?is_nsfw=true&gif=true')
                
                @commands.Cog.listener()
                async def on_command_error(self, ctx, error):
                        if isinstance(error, commands.errors.NSFWChannelRequired):
                                await ctx.send(f"Hey! {ctx.author.mention}, sorry but I can't submit nsfw content outside an nsfw channel.")