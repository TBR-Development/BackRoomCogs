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
                        tags = ['waifu']
                        url = f'https://api.waifu.im/search?included_tags={tags}'

                        embed = discord.Embed()

                        async with aiohttp.ClientSession() as cs:
                                async with cs.get(url) as r:
                                        res = await r.json()
                                        embed.set_image(url=res['data'][0]['url'])

                                        await ctx.send(embed=embed)
                
                @commands.command()
                async def maid(self, ctx):
                        tags = ['maid']
                        url = f'https://api.waifu.im/search?included_tags={tags}'

                        embed = discord.Embed()

                        async with aiohttp.ClientSession() as cs:
                                async with cs.get(url) as r:
                                        res = await r.json()
                                        embed.set_image(url=res['data'][0]['url'])
                                        
                                        await ctx.send(embed=embed)

                @commands.command()
                async def uniform(self, ctx):
                        tags = ['uniform']
                        url = f'https://api.waifu.im/search?included_tags={tags}'

                        embed = discord.Embed()

                        async with aiohttp.ClientSession() as cs:
                                async with cs.get(url) as r:
                                        res = await r.json()
                                        embed.set_image(url=res['data'][0]['url'])
                                        
                                        await ctx.send(embed=embed)
                
                @commands.command()
                async def mori_calliope(self, ctx):
                        tags = ['mori-calliope']
                        url = f'https://api.waifu.im/search?included_tags={tags}'

                        embed = discord.Embed()

                        async with aiohttp.ClientSession() as cs:
                                async with cs.get(url) as r:
                                        res = await r.json()
                                        embed.set_image(url=res['data'][0]['url'])
                                        
                                        await ctx.send(embed=embed)

                @commands.command()
                async def marin_kitagawa(self, ctx):
                        tags = ['marin-kitagawa']
                        url = f'https://api.waifu.im/search?included_tags={tags}'

                        embed = discord.Embed()

                        async with aiohttp.ClientSession() as cs:
                                async with cs.get(url) as r:
                                        res = await r.json()
                                        embed.set_image(url=res['data'][0]['url'])
                                        
                                        await ctx.send(embed=embed)
                
                @commands.command()
                async def raiden_shogun(self, ctx):
                        tags = ['raiden-shogun']
                        url = f'https://api.waifu.im/search?included_tags={tags}'

                        embed = discord.Embed()

                        async with aiohttp.ClientSession() as cs:
                                async with cs.get(url) as r:
                                        res = await r.json()
                                        embed.set_image(url=res['data'][0]['url'])
                                        
                                        await ctx.send(embed=embed)

                @commands.command()
                @commands.is_nsfw()
                async def oppai(self, ctx):
                        tags = ['oppai']
                        url = f'https://api.waifu.im/search?included_tags={tags}'

                        embed = discord.Embed()

                        async with aiohttp.ClientSession() as cs:
                                async with cs.get(url) as r:
                                        res = await r.json()
                                        embed.set_image(url=res['data'][0]['url'])
                                        
                                        await ctx.send(embed=embed)

                @commands.command()
                @commands.is_nsfw()
                async def ass(self, ctx):
                        tags = ['ass']
                        url = f'https://api.waifu.im/search?included_tags={tags}'

                        embed = discord.Embed()

                        async with aiohttp.ClientSession() as cs:
                                async with cs.get(url) as r:
                                        res = await r.json()
                                        embed.set_image(url=res['data'][0]['url'])
                                        
                                        await ctx.send(embed=embed)

                @commands.command()
                @commands.is_nsfw()
                async def milf(self, ctx):
                        tags = ['milf']
                        url = f'https://api.waifu.im/search?included_tags={tags}'

                        embed = discord.Embed()

                        async with aiohttp.ClientSession() as cs:
                                async with cs.get(url) as r:
                                        res = await r.json()
                                        embed.set_image(url=res['data'][0]['url'])
                                        
                                        await ctx.send(embed=embed)


                @commands.command()
                @commands.is_nsfw()
                async def hentai(self, ctx):
                        tags = ['hentai']
                        url = f'https://api.waifu.im/search?included_tags={tags}'

                        embed = discord.Embed()

                        async with aiohttp.ClientSession() as cs:
                                async with cs.get(url) as r:
                                        res = await r.json()
                                        embed.set_image(url=res['data'][0]['url'])
                                        
                                        await ctx.send(embed=embed)

                @commands.command()
                @commands.is_nsfw()
                async def oral(self, ctx):
                        tags = ['oral']
                        url = f'https://api.waifu.im/search?included_tags={tags}'

                        embed = discord.Embed()

                        async with aiohttp.ClientSession() as cs:
                                async with cs.get(url) as r:
                                        res = await r.json()
                                        embed.set_image(url=res['data'][0]['url'])
                                        
                                        await ctx.send(embed=embed)

                @commands.command()
                @commands.is_nsfw()
                async def paizuri(self, ctx):
                        tags = ['paizuri']
                        url = f'https://api.waifu.im/search?included_tags={tags}'

                        embed = discord.Embed()

                        async with aiohttp.ClientSession() as cs:
                                async with cs.get(url) as r:
                                        res = await r.json()
                                        embed.set_image(url=res['data'][0]['url'])
                                        
                                        await ctx.send(embed=embed)

                @commands.command()
                @commands.is_nsfw()
                async def ecchi(self, ctx):
                        tags = ['ecchi']
                        url = f'https://api.waifu.im/search?included_tags={tags}'

                        embed = discord.Embed()

                        async with aiohttp.ClientSession() as cs:
                                async with cs.get(url) as r:
                                        res = await r.json()
                                        embed.set_image(url=res['data'][0]['url'])
                                        
                                        await ctx.send(embed=embed)

                @commands.command()
                @commands.is_nsfw()
                async def ero(self, ctx):
                        tags = ['ero']
                        url = f'https://api.waifu.im/search?included_tags={tags}'

                        embed = discord.Embed()

                        async with aiohttp.ClientSession() as cs:
                                async with cs.get(url) as r:
                                        res = await r.json()
                                        embed.set_image(url=res['data'][0]['url'])
                                        
                                        await ctx.send(embed=embed)


                        

                @commands.Cog.listener()
                async def on_command_error(self, ctx, error):
                        if isinstance(error, commands.errors.NSFWChannelRequired):
                                await ctx.send(f"Hey! {ctx.author.mention}, sorry but I can't submit nsfw content outside an nsfw channel.")