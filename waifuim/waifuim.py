from typing import Final
from datetime import datetime
from json import loads

import discord
import aiohttp

from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.utils.chat_formatting import box

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
            await self.session.close()
            
            
    @commands.hybrid_group()
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def waifuim(self, ctx):
            """
            Get waifu images from waifu.im api.
            """
            return
    
            
    @waifuim.command()
    async def help(self, ctx):
            """
            Get a list of available tags for use with WaifuIM.
            """
            
            url = 'https://api.waifu.im/tags'
            
            async with self.session.get(url) as response:
                data = await response.json()
                    
                versatile = data['versatile']
                nsfw = data['nsfw']
                
                versatile_array = ', '.join(versatile)
                nsfw_array = ', '.join(nsfw)
                
                sfw_tags = '{}'.format(versatile_array)
                nsfw_tags = '{}, {}'.format(versatile_array, nsfw_array)
                
                embed = discord.Embed(title='Tag Help', description='Here is a list of available tags from the waifu.im api.\nThe `[p]tag` and `[p]ntag` commands are the only ones that require a tag. All other commands do not accapt a tag.', timestamp=datetime.now())
                embed.color = await ctx.embed_color()
                embed.add_field(name='SFW Tags', value=box(sfw_tags))
                embed.add_field(name='NSFW Tags', value=box(nsfw_tags))
                embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.display_avatar.url)
                embed.color = await ctx.embed_color()
                
                if response.status == 200:
                        await ctx.send(embed=embed)
                else:
                        await ctx.send(':x: Request failed with status: ', response.status)   
        
    @waifuim.command()
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
#                        artist_name = image['artist']['name']
                        
                raw = datetime.fromisoformat(uploaded_at).date().strftime("%B %d, %Y")
                
                date = '{}'.format(raw)
                upload_date = date
                
                embed = discord.Embed(timestamp=datetime.now())
#                embed.add_field(name='Artist Name', value=artist_name, inline=True)
                embed.add_field(name='Upload Date', value=upload_date, inline=True)
                embed.set_image(url=image_url)
                embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.display_avatar.url)
                embed.color = await ctx.embed_color()
                view = discord.ui.View()
                style = discord.ButtonStyle.grey
                image_button = discord.ui.Button(style=style, label='Open Image', url=image_url)
                source_button = discord.ui.Button(style=style, label='Image Source', url=source_url)
                view.add_item(item=image_button)
                view.add_item(item=source_button)
                
                if response.status == 200:
                        await ctx.send(embed=embed, view=view)
                else:
                        await ctx.send(':x: Request failed with status: ', response.status)     
                                
        
    @waifuim.command()
    async def tag(self, ctx, tag):
            """
            Get a random waifu image by tag.
            
            See [p]taghelp for a list of available tags.
            """
            
            
            url = 'https://api.waifu.im/search'
            params = {'included_tags': '{}'.format(tag), 'is_nsfw': 'false'}
            
            
            async with self.session.get(url, params=params) as response:
                data = await response.json()
                    
                for image in data['images']:
                        image_url = image['url']
                        source_url = image['source']
                        uploaded_at = image['uploaded_at']
#                        artist_name = image['artist']['name']
                        
                raw = datetime.fromisoformat(uploaded_at).date().strftime("%B %d, %Y")
                
                date = '{}'.format(raw)
                upload_date = date
                
                embed = discord.Embed(timestamp=datetime.now())
#                embed.add_field(name='Artist Name', value=artist_name, inline=True)
                embed.add_field(name='Upload Date', value=upload_date, inline=True)
                embed.set_image(url=image_url)
                embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.display_avatar.url)
                embed.color = await ctx.embed_color()
                view = discord.ui.View()
                style = discord.ButtonStyle.grey
                image_button = discord.ui.Button(style=style, label='Open Image', url=image_url)
                source_button = discord.ui.Button(style=style, label='Image Source', url=source_url)
                view.add_item(item=image_button)
                view.add_item(item=source_button)
                
                if response.status == 200:
                        await ctx.send(embed=embed, view=view)
                else:
                        await ctx.send(':x: Request failed with status: ', response.status)     
                               
    @waifuim.command()
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
#                        artist_name = image['artist']['name']
                        
                raw = datetime.fromisoformat(uploaded_at).date().strftime("%B %d, %Y")
                
                date = '{}'.format(raw)
                upload_date = date
                
                embed = discord.Embed(timestamp=datetime.now())
#                embed.add_field(name='Artist Name', value=artist_name, inline=True)
                embed.add_field(name='Upload Date', value=upload_date, inline=True)
                embed.set_image(url=image_url)
                embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.display_avatar.url)
                embed.color = await ctx.embed_color()
                view = discord.ui.View()
                style = discord.ButtonStyle.grey
                image_button = discord.ui.Button(style=style, label='Open Image', url=image_url)
                source_button = discord.ui.Button(style=style, label='Image Source', url=source_url)
                view.add_item(item=image_button)
                view.add_item(item=source_button)
                
                if response.status == 200:
                        await ctx.send(embed=embed, view=view)
                else:
                        await ctx.send(':x: Request failed with status: ', response.status)     
                               
    @waifuim.command()
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
#                        artist_name = image['artist']['name']
                        
                raw = datetime.fromisoformat(uploaded_at).date().strftime("%B %d, %Y")
                
                date = '{}'.format(raw)
                upload_date = date
                
                embed = discord.Embed(timestamp=datetime.now())
#                embed.add_field(name='Artist Name', value=artist_name, inline=True)
                embed.add_field(name='Upload Date', value=upload_date, inline=True)
                embed.set_image(url=image_url)
                embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.display_avatar.url)
                embed.color = await ctx.embed_color()
                view = discord.ui.View()
                style = discord.ButtonStyle.grey
                image_button = discord.ui.Button(style=style, label='Open Image', url=image_url)
                source_button = discord.ui.Button(style=style, label='Image Source', url=source_url)
                view.add_item(item=image_button)
                view.add_item(item=source_button)
                
                if response.status == 200:
                        await ctx.send(embed=embed, view=view)
                else:
                        await ctx.send(':x: Request failed with status: ', response.status)     
                               
    @waifuim.command()
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
#                        artist_name = image['artist']['name']
                        
                raw = datetime.fromisoformat(uploaded_at).date().strftime("%B %d, %Y")
                
                date = '{}'.format(raw)
                upload_date = date
                
                embed = discord.Embed(timestamp=datetime.now())
#                embed.add_field(name='Artist Name', value=artist_name, inline=True)
                embed.add_field(name='Upload Date', value=upload_date, inline=True)
                embed.set_image(url=image_url)
                embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.display_avatar.url)
                embed.color = await ctx.embed_color()
                view = discord.ui.View()
                style = discord.ButtonStyle.grey
                image_button = discord.ui.Button(style=style, label='Open Image', url=image_url)
                source_button = discord.ui.Button(style=style, label='Image Source', url=source_url)
                view.add_item(item=image_button)
                view.add_item(item=source_button)
                
                if response.status == 200:
                        await ctx.send(embed=embed, view=view)
                else:
                        await ctx.send(':x: Request failed with status: ', response.status)     
                                
    @waifuim.command()
    @commands.is_nsfw()
    async def ntag(self, ctx, tag):
            """
            Get a random nsfw waifu image by tag.
            
            See [p]taghelp for a list of available tags.
            """
            
            url = 'https://api.waifu.im/search'
            params = {'included_tags': '{}'.format(tag), 'is_nsfw': 'true'}
            
            async with self.session.get(url, params=params) as response:
                data = await response.json()
                    
                for image in data['images']:
                        image_url = image['url']
                        source_url = image['source']
                        uploaded_at = image['uploaded_at']
#                        artist_name = image['artist']['name']
                    
                raw = datetime.fromisoformat(uploaded_at).date().strftime("%B %d, %Y")
                
                date = '{}'.format(raw)
                upload_date = date
                
                embed = discord.Embed(timestamp=datetime.now())
#                embed.add_field(name='Artist Name', value=artist_name, inline=True)
                embed.add_field(name='Upload Date', value=upload_date, inline=True)
                embed.set_image(url=image_url)
                embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.display_avatar.url)
                embed.color = await ctx.embed_color()
                view = discord.ui.View()
                style = discord.ButtonStyle.grey
                image_button = discord.ui.Button(style=style, label='Open Image', url=image_url)
                source_button = discord.ui.Button(style=style, label='Image Source', url=source_url)
                view.add_item(item=image_button)
                view.add_item(item=source_button)
                
                if response.status == 200:
                        await ctx.send(embed=embed, view=view)
                else:
                        await ctx.send(':x: Request failed with status: ', response.status)     
                               
    @waifuim.command()
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
#                        artist_name = image['artist']['name']
                        
                raw = datetime.fromisoformat(uploaded_at).date().strftime("%B %d, %Y")
                
                date = '{}'.format(raw)
                upload_date = date
                
                
                embed = discord.Embed(timestamp=datetime.now())
#                embed.add_field(name='Artist Name', value=artist_name, inline=True)
                embed.add_field(name='Upload Date', value=upload_date, inline=True)
                embed.set_image(url=image_url)
                embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.display_avatar.url)
                embed.color = await ctx.embed_color()
                view = discord.ui.View()
                style = discord.ButtonStyle.grey
                image_button = discord.ui.Button(style=style, label='Open Image', url=image_url)
                source_button = discord.ui.Button(style=style, label='Image Source', url=source_url)
                view.add_item(item=image_button)
                view.add_item(item=source_button)
                
                if response.status == 200:
                        await ctx.send(embed=embed, view=view)
                else:
                        await ctx.send(':x: Request failed with status: ', response.status)     
                               
    @waifuim.command()
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
#                        artist_name = image['artist']['name']
                        
                raw = datetime.fromisoformat(uploaded_at).date().strftime("%B %d, %Y")
                
                date = '{}'.format(raw)
                upload_date = date
                
                embed = discord.Embed(timestamp=datetime.now())
#                embed.add_field(name='Artist Name', value=artist_name, inline=True)
                embed.add_field(name='Upload Date', value=upload_date, inline=True)
                embed.set_image(url=image_url)
                embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.display_avatar.url)
                embed.color = await ctx.embed_color()
                view = discord.ui.View()
                style = discord.ButtonStyle.grey
                image_button = discord.ui.Button(style=style, label='Open Image', url=image_url)
                source_button = discord.ui.Button(style=style, label='Image Source', url=source_url)
                view.add_item(item=image_button)
                view.add_item(item=source_button)
                
                if response.status == 200:
                        await ctx.send(embed=embed, view=view)
                else:
                        await ctx.send(':x: Request failed with status: ', response.status)       
