from redbot.core import commands

import requests
import discord
# import aiohttp

class Waifu(commands.Cog):
        """
        Get images from Waifu.IM API
        """

        def __init__(self, bot):
                self.bot = bot

                @commands.command()
                async def waifu(self, ctx):
                        """
                        Description: Get a random SFW image
                        Usage: [p]waifu
                        """
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
                        """
                        Description: Get a random NSFW image
                        Usage: [p]lewds
                        """
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
                        """
                        Description: Get a random SFW gif
                        Usage: [p]aniwaifu
                        """
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
                        """
                        Description: Get a random NSFW gif
                        Usage: [p]anilewds
                        """
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
                                embed = discord.Embed(
                                        title = "NSFW Command",
                                        description = "I am unable to post NSFW content in this channel.\nPlease move to an NSFW channel and try again."
                                        )
                                await ctx.send(embed=embed)
                        else:
                                embed = discord.Embed(
                                        title = "Command Error",
                                        description = error.args[0]
                                        )
                                await ctx.send(embed=embed)