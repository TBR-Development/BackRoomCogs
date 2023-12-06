from redbot.core import commands

import requests

class Waifu(commands.Cog):
        """
        Get images from Waifu.IM API
        """

        def __init__(self, bot):
                self.bot = bot

                @commands.command()
                async def waifu(self, ctx):
                        # retrieve image url from API URL
                        # ... need to figure out how to convert from requests to aiohttp

                        params = {
                                'is_nasfw': 'false',
                                'gif': 'false'
                        }
                        
                        response = requests.get('https://api.waifu.im/search', params=params)

                        if response.status_code == 200:
                                data = response.json()
                        else:
                                print('Request failed with status code:', response.status_code)
                        
                        await ctx.send(data['url'])

                @commands.command()
                @commands.is_nsfw()
                async def lewds(self, ctx):
                        # retrieve image url from API URL
                        # ... need to figure out how to convert from requests to aiohttp

                        params = {
                                'is_nsfw': 'true',
                                'gif': 'false'
                        }

                        response = requests.get('https://api.waifu.im/search', params=params)

                        if response.status_code == 200:
                                data = response.json()
                        else:
                                print('Request failed with status code:', response.status_code)
                        
                        await ctx.send(data['url'])
                
                @commands.command()
                async def aniwaifu(self, ctx):
                        # retrieve image url from API URL
                        # ... need to figure out how to convert from requests to aiohttp

                        params = {
                                'is_nasf': 'false',
                                'gif': 'true'
                        }

                        response = requests.get('https://api.waifu.im/search', params=params)

                        if response.status_code == 200:
                                data = response.json()
                        else:
                                print('Request failed with status code:', response.status_code)
                        
                        await ctx.send(data['url'])
                
                @commands.command()
                @commands.is_nsfw()
                async def anilewds(self, ctx):
                        # retrieve image url from API URL
                        # ... need to figure out how to convert from requests to aiohttp

                        params = {
                                'is_nsfw': 'true',
                                'gif': 'true'
                        }

                        response = requests.get('https://api.waifu.im/search', params=params)

                        if response.status_code == 200:
                                data = response.json()
                        else:
                                print('Request failed with status code:', response.status_code)
                        
                        await ctx.send(data['url'])
                
                @commands.Cog.listener()
                async def on_command_error(self, ctx, error):
                        if isinstance(error, commands.errors.NSFWChannelRequired):
                                await ctx.send(f"Hey! {ctx.author.mention}, sorry but I can't submit nsfw content outside an nsfw channel.")