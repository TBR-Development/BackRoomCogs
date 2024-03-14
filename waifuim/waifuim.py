from typing import Final
from datetime import datetime

import discord
import aiohttp

from redbot.core import commands
from redbot.core.bot import Red

footer_icon: Final[str] = 'https://avatars.githubusercontent.com/u/91619079?s=200&v=4'
footer_text = 'Powered by Waifu.IM API'

class WaifuIM(commands.Cog):
    """
    Get images from Waifu.IM API
    """

    def __init__(self, bot):
            self.bot = bot
            self.session = aiohttp.ClientSession()
                     
    async def cog_unload(self):
            self.session.close()
        
    @commands.hybrid_command()
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def random(self, ctx):
            """
            Get a random waifu image
            """
            
            url = 'https://api.waifu.im/search'
            params = {'is_nsfw': 'false'}
            
            async with self.session.get(url, params=params) as response:
                data = await response.json()
                    
                for image in data['images']:
                        image_url = image['url']
                        source_url = image['source']
                        uploaded_at = image['uploaded_at']
                        artist_name = image['artist']['name']
                        
                raw = datetime.fromisoformat(uploaded_at).date().strftime("%B %d, %Y")
                
                date= '{}'.format(raw)
                upload_date = date
                
                embed = discord.Embed()
                embed.add_field(name='Artist Name', value=artist_name, inline=True)
                embed.add_field(name='Upload Date', value=upload_date, inline=True)
                embed.set_image(url=image_url)
                embed.set_footer(text=footer_text, icon_url=footer_icon)
                embed.color = await ctx.embed_color()
                view = discord.ui.View()
                style = discord.ButtonStyle.grey
                image_button = discord.ui.Button(style=style, label='Open Image', url=image_url)
                source_button = discord.ui.Button(style=style, label='Image Source', url=source_url)
                view.add_item(item=image_button)
                view.add_item(item=source_button)
                
                await ctx.send(embed=embed, view=view)
                                
        
    @commands.hybrid_command()
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def tag(self, ctx, tag):
            """
            Get a random waifu image by tag
            Available tags:
            
            - waifu
            - maid
            - marin-kitagawa
            - mori-calliope
            - raiden-shogun
            - oppai
            - selfies
            - uniform
            - kamisato-ayaka
            """
            
            
            url = 'https://api.waifu.im/search'
            params = {'included_tags': '{}'.format(tag), 'is_nsfw': 'false'}
            
            async with self.session.get(url, params=params) as response:
                data = await response.json()
                    
                for image in data['images']:
                        image_url = image['url']
                        source_url = image['source']
                        uploaded_at = image['uploaded_at']
                        artist_name = image['artist']['name']
                        
                raw = datetime.fromisoformat(uploaded_at).date().strftime("%B %d, %Y")
                
                date= '{}'.format(raw)
                upload_date = date
                
                if artist_name == None:
                        author = 'null'
                else:
                        author = artist_name
                
                embed = discord.Embed()
                embed.add_field(name='Artist Name', value=author, inline=True)
                embed.add_field(name='Upload Date', value=upload_date, inline=True)
                embed.set_image(url=image_url)
                embed.set_footer(text=footer_text, icon_url=footer_icon)
                embed.color = await ctx.embed_color()
                view = discord.ui.View()
                style = discord.ButtonStyle.grey
                image_button = discord.ui.Button(style=style, label='Open Image', url=image_url)
                source_button = discord.ui.Button(style=style, label='Image Source', url=source_url)
                view.add_item(item=image_button)
                view.add_item(item=source_button)
                
                await ctx.send(embed=embed, view=view)
                               
    @commands.hybrid_command()
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def gif(self, ctx):
            """
            Get a random waifu gif
            """
            
            url = 'https://api.waifu.im/search'
            params = {'gif': 'true', 'is_nsfw': 'false'}
            
            async with self.session.get(url, params=params) as response:
                data = await response.json()
                    
                for image in data['images']:
                        image_url = image['url']
                        source_url = image['source']
                        uploaded_at = image['uploaded_at']
                        artist_name = image['artist']['name']
                        
                raw = datetime.fromisoformat(uploaded_at).date().strftime("%B %d, %Y")
                
                date= '{}'.format(raw)
                upload_date = date
                
                if artist_name == None:
                        author = 'null'
                else:
                        author = artist_name
                
                embed = discord.Embed()
                embed.add_field(name='Artist Name', value=author, inline=True)
                embed.add_field(name='Upload Date', value=upload_date, inline=True)
                embed.set_image(url=image_url)
                embed.set_footer(text=footer_text, icon_url=footer_icon)
                embed.color = await ctx.embed_color()
                view = discord.ui.View()
                style = discord.ButtonStyle.grey
                image_button = discord.ui.Button(style=style, label='Open Image', url=image_url)
                source_button = discord.ui.Button(style=style, label='Image Source', url=source_url)
                view.add_item(item=image_button)
                view.add_item(item=source_button)
                
                await ctx.send(embed=embed, view=view)
                               
    @commands.hybrid_command()
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def dump(self, ctx):
            """
            Dump a bunch of random waifu images
            """
            
            url = 'https://api.waifu.im/search'
            params = {'many': 'true', 'is_nsfw': 'false'}
            
            async with self.session.get(url, params=params) as response:
                data = await response.json()
                    
                for image in data['images']:
                        image_url = image['url']
                        source_url = image['source']
                        uploaded_at = image['uploaded_at']
                        artist_name = image['artist']['name']
                        
                raw = datetime.fromisoformat(uploaded_at).date().strftime("%B %d, %Y")
                
                date= '{}'.format(raw)
                upload_date = date
                
                if artist_name == None:
                        author = 'null'
                else:
                        author = artist_name
                
                embed = discord.Embed()
                embed.add_field(name='Artist Name', value=author, inline=True)
                embed.add_field(name='Upload Date', value=upload_date, inline=True)
                embed.set_image(url=image_url)
                embed.set_footer(text=footer_text, icon_url=footer_icon)
                embed.color = await ctx.embed_color()
                view = discord.ui.View()
                style = discord.ButtonStyle.grey
                image_button = discord.ui.Button(style=style, label='Open Image', url=image_url)
                source_button = discord.ui.Button(style=style, label='Image Source', url=source_url)
                view.add_item(item=image_button)
                view.add_item(item=source_button)
                
                await ctx.send(embed=embed, view=view)
                               
    @commands.hybrid_command()
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    @commands.is_nsfw()
    async def nrandom(self, ctx):
            """
            Get a random nsfw waifu image
            """
            
            url = 'https://api.waifu.im/search'
            params = {'is_nsfw': 'true'}
            
            async with self.session.get(url, params=params) as response:
                data = await response.json()
                    
                for image in data['images']:
                        image_url = image['url']
                        source_url = image['source']
                        uploaded_at = image['uploaded_at']
                        artist_name = image['artist']['name']
                        
                raw = datetime.fromisoformat(uploaded_at).date().strftime("%B %d, %Y")
                
                date= '{}'.format(raw)
                upload_date = date
                
                if artist_name == None:
                        author = 'null'
                else:
                        author = artist_name
                
                embed = discord.Embed()
                embed.add_field(name='Artist Name', value=author, inline=True)
                embed.add_field(name='Upload Date', value=upload_date, inline=True)
                embed.set_image(url=image_url)
                embed.set_footer(text=footer_text, icon_url=footer_icon)
                embed.color = await ctx.embed_color()
                view = discord.ui.View()
                style = discord.ButtonStyle.grey
                image_button = discord.ui.Button(style=style, label='Open Image', url=image_url)
                source_button = discord.ui.Button(style=style, label='Image Source', url=source_url)
                view.add_item(item=image_button)
                view.add_item(item=source_button)
                
                await ctx.send(embed=embed, view=view)
                                
    @commands.hybrid_command()
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    @commands.is_nsfw()
    async def ntag(self, ctx, tag):
            """
            Get a random nsfw waifu image by tag
            
            Available tags:
            
            - waifu
            - maid
            - marin-kitagawa
            - mori-calliope
            - raiden-shogun
            - oppai
            - selfies
            - uniform
            - kamisato-ayaka
            - ero
            - ass
            - hentai
            - milf
            - oral
            - paizuri
            - ecchi
            """
            
            url = 'https://api.waifu.im/search'
            params = {'included_tags': '{}'.format(tag), 'is_nsfw': 'true'}
            
            async with self.session.get(url, params=params) as response:
                data = await response.json()
                    
                for image in data['images']:
                        image_url = image['url']
                        source_url = image['source']
                        uploaded_at = image['uploaded_at']
                        artist_name = image['artist']['name']
                        
                raw = datetime.fromisoformat(uploaded_at).date().strftime("%B %d, %Y")
                
                date= '{}'.format(raw)
                upload_date = date
                
                if artist_name == None:
                        author = 'null'
                else:
                        author = artist_name
                
                embed = discord.Embed()
                embed.add_field(name='Artist Name', value=author, inline=True)
                embed.add_field(name='Upload Date', value=upload_date, inline=True)
                embed.set_image(url=image_url)
                embed.set_footer(text=footer_text, icon_url=footer_icon)
                embed.color = await ctx.embed_color()
                view = discord.ui.View()
                style = discord.ButtonStyle.grey
                image_button = discord.ui.Button(style=style, label='Open Image', url=image_url)
                source_button = discord.ui.Button(style=style, label='Image Source', url=source_url)
                view.add_item(item=image_button)
                view.add_item(item=source_button)
                
                await ctx.send(embed=embed, view=view)
                               
    @commands.hybrid_command()
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    @commands.is_nsfw()
    async def ngif(self, ctx):
            """
            Get a random nsfw waifu gif
            """
            
            url = 'https://api.waifu.im/search'
            params = {'gif': 'true', 'is_nsfw': 'true'}
            
            async with self.session.get(url, params=params) as response:
                data = await response.json()
                    
                for image in data['images']:
                        image_url = image['url']
                        source_url = image['source']
                        uploaded_at = image['uploaded_at']
                        artist_name = image['artist']['name']
                        
                raw = datetime.fromisoformat(uploaded_at).date().strftime("%B %d, %Y")
                
                date= '{}'.format(raw)
                upload_date = date
                
                if artist_name == None:
                        author = 'null'
                else:
                        author = artist_name
                
                embed = discord.Embed()
                embed.add_field(name='Artist Name', value=author, inline=True)
                embed.add_field(name='Upload Date', value=upload_date, inline=True)
                embed.set_image(url=image_url)
                embed.set_footer(text=footer_text, icon_url=footer_icon)
                embed.color = await ctx.embed_color()
                view = discord.ui.View()
                style = discord.ButtonStyle.grey
                image_button = discord.ui.Button(style=style, label='Open Image', url=image_url)
                source_button = discord.ui.Button(style=style, label='Image Source', url=source_url)
                view.add_item(item=image_button)
                view.add_item(item=source_button)
                
                await ctx.send(embed=embed, view=view)
                               
    @commands.hybrid_command()
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    @commands.is_nsfw()
    async def ndump(self, ctx):
            """
            Dump a bunch of random nsfw waifu images
            """
            
            url = 'https://api.waifu.im/search'
            params = {'many': 'true', 'is_nsfw': 'true'}
            
            async with self.session.get(url, params=params) as response:
                data = await response.json()
                    
                for image in data['images']:
                        image_url = image['url']
                        source_url = image['source']
                        uploaded_at = image['uploaded_at']
                        artist_name = image['artist']['name']
                        
                raw = datetime.fromisoformat(uploaded_at).date().strftime("%B %d, %Y")
                
                date= '{}'.format(raw)
                upload_date = date
                
                if artist_name == None:
                        author = 'null'
                else:
                        author = artist_name
                
                embed = discord.Embed()
                embed.add_field(name='Artist Name', value=author, inline=True)
                embed.add_field(name='Upload Date', value=upload_date, inline=True)
                embed.set_image(url=image_url)
                embed.set_footer(text=footer_text, icon_url=footer_icon)
                embed.color = await ctx.embed_color()
                view = discord.ui.View()
                style = discord.ButtonStyle.grey
                image_button = discord.ui.Button(style=style, label='Open Image', url=image_url)
                source_button = discord.ui.Button(style=style, label='Image Source', url=source_url)
                view.add_item(item=image_button)
                view.add_item(item=source_button)
                
                await ctx.send(embed=embed, view=view)
                               
