from typing import Final
from datetime import datetime

import discord
import aiohttp

from redbot.core import Config, commands
from redbot.core.bot import Red
from redbot.core.utils.chat_formatting import box

embed_icon: Final[str] = 'https://avatars.githubusercontent.com/u/91619079?s=200&v=4'
footer_text = 'Powered by Waifu.IM API'

class WaifuIM(commands.Cog):
    """
    Get images from Waifu.IM API
    """

    def __init__(self, bot):
            self.bot = bot
            self.session = aiohttp.ClientSession()
            self.config = Config.get_conf(self, identifier=465228604721201158)
            
            self.config.register_global(
                    bearer_token = ''
                    )
                     
    async def cog_unload(self):
            await self.session.close()
            
            
    @commands.hybrid_group()
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
            
            tags_endpoint = 'https://api.waifu.im/tags'
            
            async with self.session.get(tags_endpoint) as response:
                data = await response.json()
            
            versatile = data['versatile']
            nsfw = data['nsfw']
            versatile_array = ', '.join(versatile)
            nsfw_array = ', '.join(nsfw)
            versatile_tags = '{}'.format(versatile_array)
            nsfw_tags = '{}, {}'.format(versatile_array, nsfw_array)
                
            embed = discord.Embed(title='Tag Help', description='Here is a list of available tags from the waifu.im api.\n\nThe `[p]tag` and `[p]ntag` commands are the only ones that require a tag. All other commands do not accapt a tag.', timestamp=datetime.now())
            embed.color = await ctx.embed_color()
            embed.add_field(name='SFW Tags', value=box(versatile_tags))
            embed.add_field(name='NSFW Tags', value=box(nsfw_tags))
            embed.set_thumbnail(url=embed_icon)
            embed.set_image(url='https://cdn.waifu.im/7892.jpg')
            embed.set_footer(text=footer_text, icon_url=embed_icon)
            view = discord.ui.View()
            style = discord.ButtonStyle.grey
            website_button = discord.ui.Button(style=style, label='Waifu.IM', url='https://www.waifu.im/')
            view.add_item(item=website_button)
            
            await ctx.send(embed=embed, view=view)   

    @waifuim.command()
    @commands.is_administrator()
    async def settoken(self, ctx, token):
            """
            Set the authorization bearer token.
            
            Your bearer token can be found at:
            
            - https://www.waifu.im/dashboard
            """
            
            await self.config.logger_channel.set(token)
            await ctx.send(':white_check_mark: The token has been set.')
    
    
    @waifuim.command()
    @commands.is_administrator()
    async def delfav(self, ctx, id):
            """
            Remove an image id from the guild favorites
            """
            
            token = self.config.bearer_token()
            favorites_endpoint = 'https://api.waifu.im/fav/delete'
            headers = {
                    'Accept-Version': 'v5',
                    'Autorization': f'Bearer {token}',
                    'Content-Type': 'application/json'
            }
            
            data = {
                    'image_id': id
            }

            if token != None:
                    async with self.session.get(favorites_endpoint, headers=headers, json=data) as response:
                            data = await response.json()
                    
                    await ctx.send('Image added to guild favorites')
            else:
                    await ctx.send('Authorization token not found. Please use `[p]waifuim settoken [token]` to use this command.')
                    
    @waifuim.command()
    @commands.is_administrator()
    async def addfav(self, ctx, id):
            """
            Add an image id to the guild favorites
            """
            
            token = self.config.bearer_token()
            favorites_endpoint = 'https://api.waifu.im/fav/insert'
            headers = {
                    'Accept-Version': 'v5',
                    'Autorization': f'Bearer {token}',
                    'Content-Type': 'application/json'
            }
            
            data = {
                    'image_id': id
            }

            if token != None:
                    async with self.session.get(favorites_endpoint, headers=headers, json=data) as response:
                            data = await response.json()
                    
                    await ctx.send('Image added to guild favorites')
            else:
                    await ctx.send('Authorization token not found. Please use `[p]waifuim settoken [token]` to use this command.')
                    
                    
                    
    @waifuim.command()
    async def fav(self, ctx):
            """
            Get a random image from the guild favorites.
            """
            token = self.config.bearer_token()
            favorites_endpoint = 'https://api.waifu.im/fav'
            headers = {
                    'Accept-Version': 'v5',
                    'Autorization': f'Bearer {token}'
            }
            
            if token != None:
                    async with self.session.get(favorites_endpoint, headers=headers) as response:
                            data = await response.json()
                    
                    for image in data['images']:
                            image_url = image['url']
                            source_url = image['source']
                            uploaded_at = image['uploaded_at']
                
                    raw = datetime.fromisoformat(uploaded_at).date().strftime("%B %d, %Y")
                    
                    date = '{}'.format(raw)
                    upload_date = date
                
                    embed = discord.Embed(timestamp=datetime.now())
                    embed.add_field(name='Upload Date', value=upload_date, inline=True)
                    embed.set_image(url=image_url)
                    embed.set_footer(text=footer_text, icon_url=embed_icon)
                    embed.color = await ctx.embed_color()
                    view = discord.ui.View()
                    style = discord.ButtonStyle.grey
                    image_button = discord.ui.Button(style=style, label='Open Image', url=image_url)
                    source_button = discord.ui.Button(style=style, label='Image Source', url=source_url)
                    view.add_item(item=image_button)
                    view.add_item(item=source_button)
                    
                    await ctx.send(embed=embed, view=view)
            else:
                    await ctx.send('Authorization token not found. If you are an admin, please use `[p]waifuim settoken [token]` to use this command.')
                    
    @waifuim.command()
    async def random(self, ctx):
            """
            Get a random waifu image
            """
            search_endpoint = 'https://api.waifu.im/search'
            params = {'is_nsfw': 'false'}
                        
            async with self.session.get(search_endpoint, params=params) as response:
                data = await response.json()
                    
                for image in data['images']:
                        image_url = image['url']
                        image_id = image['image_id']
                        source_url = image['source']
                        uploaded_at = image['uploaded_at']
                        
                raw = datetime.fromisoformat(uploaded_at).date().strftime("%B %d, %Y")
                
                date = '{}'.format(raw)
                upload_date = date
                
                embed = discord.Embed(timestamp=datetime.now())
                embed.add_field(name='Upload Date', value=upload_date, inline=True)
                embed.set_image(url=image_url)
                embed.set_footer(text=footer_text, icon_url=embed_icon)
                embed.color = await ctx.embed_color()
                view = discord.ui.View()
                style = discord.ButtonStyle.grey
                image_button = discord.ui.Button(style=style, label='Open Image', url=image_url)
                source_button = discord.ui.Button(style=style, label='Image Source', url=source_url)
                view.add_item(item=image_button)
                view.add_item(item=source_button)
                
                await ctx.send(embed=embed, view=view)   
                                
        
    @waifuim.command()
    async def tag(self, ctx, tag):
            """
            Get a random waifu image by tag.
            
            See `[p]waifuim help` for a list of available tags.
            """
            
            tags_endpoint = 'https://api.waifu.im/tags'
            search_endpoint = 'https://api.waifu.im/search'
            params = {'included_tags': '{}'.format(tag)}
            
            async with self.session.get(tags_endpoint) as response:
                data = await response.json()
                
            versatile_tags = data['versatile']
            
            if tag in versatile_tags: 
                    
                    async with self.session.get(search_endpoint, params=params) as response:
                            data = await response.json()
                    
                    for image in data['images']:
                            image_url = image['url']
                            image_id = image['image_id']
                            source_url = image['source']
                            uploaded_at = image['uploaded_at']
                        
                    raw = datetime.fromisoformat(uploaded_at).date().strftime("%B %d, %Y")
                        
                    date = '{}'.format(raw)
                    upload_date = date
                
                    embed = discord.Embed(timestamp=datetime.now())
                    embed.add_field(name='Image Id', value=image_id, inline=True)
                    embed.add_field(name='Upload Date', value=upload_date, inline=True)
                    embed.set_image(url=image_url)
                    embed.set_footer(text=footer_text, icon_url=embed_icon)
                    embed.color = await ctx.embed_color()
                    view = discord.ui.View()
                    style = discord.ButtonStyle.grey
                    image_button = discord.ui.Button(style=style, label='Open Image', url=image_url)
                    source_button = discord.ui.Button(style=style, label='Image Source', url=source_url)
                    view.add_item(item=image_button)
                    view.add_item(item=source_button)
                    
                    await ctx.send(embed=embed, view=view)
            
            else:
                    await ctx.send(box('Invalid tag passed. Please pass a valid tag.\n\nUse [p]waifuim help to see a list of available tags.'))
    
    @waifuim.command()
    async def gif(self, ctx):
            """
            Get a random waifu gif
            """
            
            search_endpoint = 'https://api.waifu.im/search'
            params = {'gif': 'true', 'is_nsfw': 'false'}
            
            async with self.session.get(search_endpoint, params=params) as response:
                data = await response.json()
                    
                for image in data['images']:
                        image_url = image['url']
                        image_id = image['image_id']
                        source_url = image['source']
                        uploaded_at = image['uploaded_at']
                        
                        
                raw = datetime.fromisoformat(uploaded_at).date().strftime("%B %d, %Y")
                
                date = '{}'.format(raw)
                upload_date = date
                
                embed = discord.Embed(timestamp=datetime.now())
                embed.add_field(name='Image Id', value=image_id, inline=True)
                embed.add_field(name='Upload Date', value=upload_date, inline=True)
                embed.set_image(url=image_url)
                embed.set_footer(text=footer_text, icon_url=embed_icon)
                embed.color = await ctx.embed_color()
                view = discord.ui.View()
                style = discord.ButtonStyle.grey
                image_button = discord.ui.Button(style=style, label='Open Image', url=image_url)
                source_button = discord.ui.Button(style=style, label='Image Source', url=source_url)
                view.add_item(item=image_button)
                view.add_item(item=source_button)
                
                await ctx.send(embed=embed, view=view) 
                               
    @waifuim.command()
    async def dump(self, ctx):
            """
            Dump a bunch of random waifu images
            """
            
            search_endpoint = 'https://api.waifu.im/search'
            params = {'many': 'true', 'is_nsfw': 'false'}
            
            async with self.session.get(search_endpoint, params=params) as response:
                data = await response.json()
                    
                for image in data['images']:
                        image_url = image['url']
                        image_id = image['image_id']
                        source_url = image['source']
                        uploaded_at = image['uploaded_at']
                        
                        
                raw = datetime.fromisoformat(uploaded_at).date().strftime("%B %d, %Y")
                
                date = '{}'.format(raw)
                upload_date = date
                
                embed = discord.Embed(timestamp=datetime.now())
                embed.add_field(name='Image Id', value=image_id, inline=True)
                embed.add_field(name='Upload Date', value=upload_date, inline=True)
                embed.set_image(url=image_url)
                embed.set_footer(text=footer_text, icon_url=embed_icon)
                embed.color = await ctx.embed_color()
                view = discord.ui.View()
                style = discord.ButtonStyle.grey
                image_button = discord.ui.Button(style=style, label='Open Image', url=image_url)
                source_button = discord.ui.Button(style=style, label='Image Source', url=source_url)
                view.add_item(item=image_button)
                view.add_item(item=source_button)
                
                await ctx.send(embed=embed, view=view) 
                               
    @waifuim.command()
    @commands.is_nsfw()
    async def nrandom(self, ctx):
            """
            Get a random nsfw waifu image
            """
            
            search_endpoint = 'https://api.waifu.im/search'
            params = {'is_nsfw': 'true'}
            
            async with self.session.get(search_endpoint, params=params) as response:
                data = await response.json()
                    
                for image in data['images']:
                        image_url = image['url']
                        image_id = image['image_id']
                        source_url = image['source']
                        uploaded_at = image['uploaded_at']
#                        
                        
                raw = datetime.fromisoformat(uploaded_at).date().strftime("%B %d, %Y")
                
                date = '{}'.format(raw)
                upload_date = date
                
                embed = discord.Embed(timestamp=datetime.now())
                embed.add_field(name='Image Id', value=image_id, inline=True)
                embed.add_field(name='Upload Date', value=upload_date, inline=True)
                embed.set_image(url=image_url)
                embed.set_footer(text=footer_text, icon_url=embed_icon)
                embed.color = await ctx.embed_color()
                view = discord.ui.View()
                style = discord.ButtonStyle.grey
                image_button = discord.ui.Button(style=style, label='Open Image', url=image_url)
                source_button = discord.ui.Button(style=style, label='Image Source', url=source_url)
                view.add_item(item=image_button)
                view.add_item(item=source_button)
                
                await ctx.send(embed=embed, view=view)
                                
    @waifuim.command()
    @commands.is_nsfw()
    async def ntag(self, ctx, tag):
            """
            Get a random nsfw waifu image by tag.
            
            See `[p]waifuim help` for a list of available tags.
            """
            
            tags_endpoint = 'https://api.waifu.im/tags'
            search_endpoint = 'https://api.waifu.im/search'
            params = {'included_tags': '{}'.format(tag)}
            
            async with self.session.get(tags_endpoint) as response:
                data = await response.json()
                
            versatile_tags = data['versatile']
            nsfw_tags = data['nsfw']
            
            if tag in versatile_tags: 
                    
                    async with self.session.get(search_endpoint, params=params) as response:
                            data = await response.json()
                    
                    for image in data['images']:
                            image_url = image['url']
                            image_id = image['image_id']
                            source_url = image['source']
                            uploaded_at = image['uploaded_at']
                        
                    raw = datetime.fromisoformat(uploaded_at).date().strftime("%B %d, %Y")
                        
                    date = '{}'.format(raw)
                    upload_date = date
                
                    embed = discord.Embed(timestamp=datetime.now())
                    embed.add_field(name='Image Id', value=image_id, inline=True)
                    embed.add_field(name='Upload Date', value=upload_date, inline=True)
                    embed.set_image(url=image_url)
                    embed.set_footer(text=footer_text, icon_url=embed_icon)
                    embed.color = await ctx.embed_color()
                    view = discord.ui.View()
                    style = discord.ButtonStyle.grey
                    image_button = discord.ui.Button(style=style, label='Open Image', url=image_url)
                    source_button = discord.ui.Button(style=style, label='Image Source', url=source_url)
                    view.add_item(item=image_button)
                    view.add_item(item=source_button)
                    
                    await ctx.send(embed=embed, view=view)
                    
            elif tag in nsfw_tags: 
                    
                    async with self.session.get(search_endpoint, params=params) as response:
                            data = await response.json()
                    
                    for image in data['images']:
                            image_url = image['url']
                            image_id = image['image_id']
                            source_url = image['source']
                            uploaded_at = image['uploaded_at']
                        
                    raw = datetime.fromisoformat(uploaded_at).date().strftime("%B %d, %Y")
                        
                    date = '{}'.format(raw)
                    upload_date = date
                
                    embed = discord.Embed(timestamp=datetime.now())
                    embed.add_field(name='Image Id', value=image_id, inline=True)
                    embed.add_field(name='Upload Date', value=upload_date, inline=True)
                    embed.set_image(url=image_url)
                    embed.set_footer(text=footer_text, icon_url=embed_icon)
                    embed.color = await ctx.embed_color()
                    view = discord.ui.View()
                    style = discord.ButtonStyle.grey
                    image_button = discord.ui.Button(style=style, label='Open Image', url=image_url)
                    source_button = discord.ui.Button(style=style, label='Image Source', url=source_url)
                    view.add_item(item=image_button)
                    view.add_item(item=source_button)
                    
                    await ctx.send(embed=embed, view=view)
                    
            else:
                    await ctx.send(box('Invalid tag passed. Please pass a valid tag.\n\nUse [p]waifuim help to see a list of available tags.'))
                    
    @waifuim.command()
    @commands.is_nsfw()
    async def ngif(self, ctx):
            """
            Get a random nsfw waifu gif
            """
            
            search_endpoint = 'https://api.waifu.im/search'
            params = {'gif': 'true', 'is_nsfw': 'true'}
            
            async with self.session.get(search_endpoint, params=params) as response:
                data = await response.json()
                    
                for image in data['images']:
                        image_url = image['url']
                        image_id = image['image_id']
                        source_url = image['source']
                        uploaded_at = image['uploaded_at']
#                        
                        
                raw = datetime.fromisoformat(uploaded_at).date().strftime("%B %d, %Y")
                
                date = '{}'.format(raw)
                upload_date = date
                
                
                embed = discord.Embed(timestamp=datetime.now())
                embed.add_field(name='Image Id', value=image_id, inline=True)
                embed.add_field(name='Upload Date', value=upload_date, inline=True)
                embed.set_image(url=image_url)
                embed.set_footer(text=footer_text, icon_url=embed_icon)
                embed.color = await ctx.embed_color()
                view = discord.ui.View()
                style = discord.ButtonStyle.grey
                image_button = discord.ui.Button(style=style, label='Open Image', url=image_url)
                source_button = discord.ui.Button(style=style, label='Image Source', url=source_url)
                view.add_item(item=image_button)
                view.add_item(item=source_button)
                
                await ctx.send(embed=embed, view=view)
                  
                               
    @waifuim.command()
    @commands.is_nsfw()
    async def ndump(self, ctx):
            """
            Dump a bunch of random nsfw waifu images
            """
            
            search_endpoint = 'https://api.waifu.im/search'
            params = {'many': 'true', 'is_nsfw': 'true'}
            
            async with self.session.get(search_endpoint, params=params) as response:
                data = await response.json()
                    
                for image in data['images']:
                        image_url = image['url']
                        image_id = image['image_id']
                        source_url = image['source']
                        uploaded_at = image['uploaded_at']
#                        
                        
                raw = datetime.fromisoformat(uploaded_at).date().strftime("%B %d, %Y")
                
                date = '{}'.format(raw)
                upload_date = date
                
                embed = discord.Embed(timestamp=datetime.now())
                embed.add_field(name='Image Id', value=image_id, inline=True)
                embed.add_field(name='Upload Date', value=upload_date, inline=True)
                embed.set_image(url=image_url)
                embed.set_footer(text=footer_text, icon_url=embed_icon)
                embed.color = await ctx.embed_color()
                view = discord.ui.View()
                style = discord.ButtonStyle.grey
                image_button = discord.ui.Button(style=style, label='Open Image', url=image_url)
                source_button = discord.ui.Button(style=style, label='Image Source', url=source_url)
                view.add_item(item=image_button)
                view.add_item(item=source_button)
                
                await ctx.send(embed=embed, view=view) 
