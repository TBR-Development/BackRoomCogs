from redbot.core import commands
from aiohttp import ClientSession

class Waifu(commands.Cog):
        """Waifu images commands using Waifu.im API"""
        def __init__(self, bot):

                        
                @commands.group()
                @commands.is_nsfw()
                async def waifu(self, ctx):
                        """Waifu images using Waifu.im API"""
                        """Usage: []waifu [option]"""
                        """Options: waifu, maid, uniform, oppai, mori_calliope, raiden_shogun, marin_kitagawa, selfies, uniform, ass, milf, paizuri, hentai, oral, ecchi, ero"""
                        if ctx.invoked_subcommand is None:
                                msg.title = 'Whoops!'
                                msg.description =  "You didn't provide an option. Please provide a valid option."
                                ctx.send(embed=msg)
                
                @waifu.command()
                async def maid(self, ctx):

                        async with ClientSession() as session:
                                url = 'https://api.waifu.im/search'
                                params = {'included_tags': ['maid'], 'height': '>=2000'}

                                async with ClientSession() as session:
                                        async with session.get(url, params) as response:
                                                response = requests.get(url, parames=params)
                                                
                                                await ctx.send(response)

                @waifu.command()
                async def waifu(self, ctx):

                        url = 'https://api.waifu.im/search'
                        params = {'included_tags': ['waifu'], 'height': '>=2000'}

                        async with ClientSession() as session:
                                        async with session.get(url, params) as response:
                                                response = requests.get(url, parames=params)
                                                
                                                await ctx.send(response)

        	@waifu.command()
                async def hentai(self, ctx):

                        url = 'https://api.waifu.im/search'
                        params = {'included_tags': ['hentai'], 'height': '>=2000'}

                        async with ClientSession() as session:
                                        async with session.get(url, params) as response:
                                                response = requests.get(url, parames=params)
                                                
                                                await ctx.send(response)

        	@waifu.command()
                async def oppai(self, ctx):

                        url = 'https://api.waifu.im/search'
                        params = {'included_tags': ['oppai'], 'height': '>=2000'}

                        async with ClientSession() as session:
                                        async with session.get(url, params) as response:
                                                response = requests.get(url, parames=params)
                                                
                                                await ctx.send(response)

		@waifu.command()
                async def selfies(self, ctx):

                        url = 'https://api.waifu.im/search'
                        params = {'included_tags': ['selfies'], 'height': '>=2000'}

                        async with ClientSession() as session:
                                        async with session.get(url, params) as response:
                                                response = requests.get(url, parames=params)
                                                
                                                await ctx.send(response)

        	@waifu.command()
                async def mori_calliope(self, ctx):

                        url = 'https://api.waifu.im/search'
                        params = {'included_tags': ['mori-calliope'], 'height': '>=2000'}

                        async with ClientSession() as session:
                                        async with session.get(url, params) as response:
                                                response = requests.get(url, parames=params)
                                                
                                                await ctx.send(response)

	        @waifu.command()
                async def raiden_shogun(self, ctx):

                        url = 'https://api.waifu.im/search'
                        params = {'included_tags': ['raiden-shogun'], 'height': '>=2000'}

                        async with ClientSession() as session:
                                        async with session.get(url, params) as response:
                                                response = requests.get(url, parames=params)
                                                
                                                await ctx.send(response)

        	@waifu.command()
                async def marin_kitagawa(self, ctx):

                        url = 'https://api.waifu.im/search'
                        params = {'included_tags': ['marin-kitagawa'], 'height': '>=2000'}

                        async with ClientSession() as session:
                                        async with session.get(url, params) as response:
                                                response = requests.get(url, parames=params)
                                                
                                                await ctx.send(response)

        	@waifu.command()
                async def ass(self, ctx):

                        url = 'https://api.waifu.im/search'
                        params = {'included_tags': ['ass'], 'height': '>=2000'}

                        async with ClientSession() as session:
                                        async with session.get(url, params) as response:
                                                response = requests.get(url, parames=params)
                                                
                                                await ctx.send(response)

        	@waifu.command()
                async def milf(self, ctx):

                        url = 'https://api.waifu.im/search'
                        params = {'included_tags': ['milf'], 'height': '>=2000'}

                        async with ClientSession() as session:
                                        async with session.get(url, params) as response:
                                                response = requests.get(url, parames=params)
                                                
                                                await ctx.send(response)

        	@waifu.command()
                async def oral(self, ctx):

                        url = 'https://api.waifu.im/search'
                        params = {'included_tags': ['oral'], 'height': '>=2000'}

                        async with ClientSession() as session:
                                        async with session.get(url, params) as response:
                                                response = requests.get(url, parames=params)
                                                
                                                await ctx.send(response)

        	@waifu.command()
                async def ecchi(self, ctx):

                        url = 'https://api.waifu.im/search'
                        params = {'included_tags': ['ecchi'], 'height': '>=2000'}

                        async with ClientSession() as session:
                                        async with session.get(url, params) as response:
                                                response = requests.get(url, parames=params)
                                                
                                               await ctx.send(response)

        	@waifu.command()
                async def ero(self, ctx):

                        url = 'https://api.waifu.im/search'
                        params = {'included_tags': ['ero'], 'height': '>=2000'}

                        async with ClientSession() as session:
                                        async with session.get(url, params) as response:
                                                response = requests.get(url, parames=params)
                                                
                                               await ctx.send(response)

        	@waifu.command()
                async def uniform(self, ctx):

                        url = 'https://api.waifu.im/search'
                        params = {'included_tags': ['uniform'], 'height': '>=2000'}

                        async with ClientSession() as session:
                                        async with session.get(url, params) as response:
                                                response = requests.get(url, parames=params)
                                                
                                                await ctx.send(response)

        	@waifu.command()
                async def paizuri(self, ctx):

                        url = 'https://api.waifu.im/search'
                        params = {'included_tags': ['paizuri'], 'height': '>=2000'}

                        async with ClientSession() as session:
                                        async with session.get(url, params) as response:
                                                response = requests.get(url, parames=params)
                                                
                                               await ctx.send(response)


	        @commands.Cog.listener()
	        async def on_command_error(self, ctx):

                        if isinstance(error, commands.errors.NSFWChannelRequired):

		        msg.title = "NSFW Command"
		        msg.description = error.args[0]

		        return await ctx.send(embed=msg) 
