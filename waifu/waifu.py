from redbot.core import commands, app_commands

import discord
import aiohttp

class Waifu(commands.Cog):
        """
        Get images from Waifu.IM API
        """

        def __init__(self, bot):
                self.bot = bot


                @app_commands.command()
                async def waifu(self, interaction: discord.Interaction):
                        url = 'https://api.waifu.im/search'
                        params = {'is_nsfw': 'false', 'gif': 'false'}

                        async with aiohttp.ClientSession() as cs:
                                async with cs.get(url, params=params) as response:
                                        if response.status == 200:
                                                data = await response.json()

                                                embed = discord.Embed(title = f"{data['name']}", description = f"{data['description']}")
                                                embed.set_image(url = f"{data['url']}")
                                                
                                                await ctx.send(embed=embed)

                @app_commands.command()
                async def aniwaifu(self, interaction: discord.Interaction):
                        url = 'https://api.waifu.im/search'
                        params = {'is_nsfw': 'false', 'gif': 'true'}

                        async with aiohttp.ClientSession() as cs:
                                async with cs.get(url, params=params) as response:
                                        if response.status == 200:
                                                data = await response.json()

                                                embed = discord.Embed(title = f"{data['name']}", description = f"{data['description']}")
                                                embed.set_image(url = f"{data['url']}")
                                                
                                                await ctx.send(embed=embed)


                @app_commands.command()
                @app_commands.is_nsfw()
                async def lewds(self, interaction: discord.Interaction):
                        url = 'https://api.waifu.im/search'
                        params = {'is_nsfw': 'true', 'gif': 'false'}

                        async with aiohttp.ClientSession() as cs:
                                async with cs.get(url, params=params) as response:
                                        if response.status == 200:
                                                data = await response.json()

                                                embed = discord.Embed(title = f"{data['name']}", description = f"{data['description']}")
                                                embed.set_image(url = f"{data['url']}")
                                                
                                                await interaction.response.send_message(embed=embed)

                @app_commands.command()
                @app_commands.is_nsfw()
                async def anilewds(self, interaction: discord.Interaction):
                        url = 'https://api.waifu.im/search'
                        params = {'is_nsfw': 'true', 'gif': 'true'}

                        async with aiohttp.ClientSession() as cs:
                                async with cs.get(url, params=params) as response:
                                        if response.status == 200:
                                                data = await response.json()

                                                embed = discord.Embed(title = f"{data['name']}", description = f"{data['description']}")
                                                embed.set_image(url = f"{data['url']}")
                                                
                                                await interaction.response.send_message(embed=embed)