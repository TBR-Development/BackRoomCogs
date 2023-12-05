from redbot.core import commands
import requests

class Waifu(commands.Cog):
	"""Waifu images commands using Waifu.im API"""
	def __init__(self, bot):
		self.bot = bot
		if ctx.invoked_subcommand is None:
			await ctx.send('Please specify a subcommand.')

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
			"""Get a random maid image from Waifu.im"""
			"""Usage: [p]waifu maid"""
			url = 'https://api.waifu.im/search'
			params = {
				'included_tags': ['maid'],
				'height': '>=2000'
				}

			response = requests.get(url, parames=params)

			if response.status_code == 200:
				data.response.json()
			else:
				print('Request failed with status code:', response.status_code)

			await ctx.send(response)

		@waifu.command()
                async def waifu(self, ctx):
                        """Get a random waifu image from Waifu.im"""
			"""Usage: [p]waifu waifu"""
                        url = 'https://api.waifu.im/search'
                        params = {
                                'included_tags': ['waifu'],
                                'height': '>=2000'
                                }

                        response = requests.get(url, parames=params)

                        if response.status_code == 200:
                                data.response.json()
                        else:
                                print('Request failed with status code:', response.status_code)

                        await ctx.send(response)

		@waifu.command()
                async def hentai(self, ctx):
                        """Get a random hentai image from Waifu.im"""
			"""Usage: [p]waifu hentai"""
                        url = 'https://api.waifu.im/search'
                        params = {
                                'included_tags': ['hentai'],
                                'height': '>=2000'
                                }

                        response = requests.get(url, parames=params)

                        if response.status_code == 200:
                                data.response.json()
                        else:
                                print('Request failed with status code:', response.status_code)

                        await ctx.send(response)

		@waifu.command()
                async def oppai(self, ctx):
                        """Get a random oppai image from Waifu.im"""
			"""Usage: [p]waifu oppai"""
                        url = 'https://api.waifu.im/search'
                        params = {
                                'included_tags': ['oppai'],
                                'height': '>=2000'
                                }

                        response = requests.get(url, parames=params)

                        if response.status_code == 200:
                                data.response.json()
                        else:
                                print('Request failed with status code:', response.status_code)

                        await ctx.send(response)

		@waifu.command()
                async def selfies(self, ctx):
                        """Get a random selfie image from Waifu.im"""
			"""Usage: [p]waifu selfies"""
                        url = 'https://api.waifu.im/search'
                        params = {
                                'included_tags': ['selfies'],
                                'height': '>=2000'
                                }

                        response = requests.get(url, parames=params)

                        if response.status_code == 200:
                                data.response.json()
                        else:
                                print('Request failed with status code:', response.status_code)

                        await ctx.send(response)

		@waifu.command()
                async def mori_calliope(self, ctx):
                        """Get a random Mori Calliope image from Waifu.im"""
			"""Usage: [p]waifu mori_calliope"""
                        url = 'https://api.waifu.im/search'
                        params = {
                                'included_tags': ['mori-calliope'],
                                'height': '>=2000'
                                }

                        response = requests.get(url, parames=params)

                        if response.status_code == 200:
                                data.response.json()
                        else:
                                print('Request failed with status code:', response.status_code)

                        await ctx.send(response)

		@waifu.command()
                async def raiden_shogun(self, ctx):
                        """Get a random Raiden Shogun image from Waifu.im"""
			"""Usage: [p]waifu raiden_shogun"""
                        url = 'https://api.waifu.im/search'
                        params = {
                                'included_tags': ['raiden-shogun'],
                                'height': '>=2000'
                                }

                        response = requests.get(url, parames=params)

                        if response.status_code == 200:
                                data.response.json()
                        else:
                                print('Request failed with status code:', response.status_code)

                        await ctx.send(response)

		@waifu.command()
                async def marin_kitagawa(self, ctx):
                        """Get a random Marin Kitagawa image from Waifu.im"""
			"""Usage: [p]waifu marin_kitagawa"""
                        url = 'https://api.waifu.im/search'
                        params = {
                                'included_tags': ['marin-kitagawa'],
                                'height': '>=2000'
                                }

                        response = requests.get(url, parames=params)

                        if response.status_code == 200:
                                data.response.json()
                        else:
                                print('Request failed with status code:', response.status_code)

                        await ctx.send(response)

		@waifu.command()
                async def ass(self, ctx):
                        """Get a random ass image from Waifu.im"""
			"""Usage: [p]waifu ass"""
                        url = 'https://api.waifu.im/search'
                        params = {
                                'included_tags': ['ass'],
                                'height': '>=2000'
                                }

                        response = requests.get(url, parames=params)

                        if response.status_code == 200:
                                data.response.json()
                        else:
                                print('Request failed with status code:', response.status_code)

                        await ctx.send(response)

		@waifu.command()
                async def milf(self, ctx):
                        """Get a random milf image from Waifu.im"""
			"""Usage: [p]waifu milf"""
                        url = 'https://api.waifu.im/search'
                        params = {
                                'included_tags': ['milf'],
                                'height': '>=2000'
                                }

                        response = requests.get(url, parames=params)

                        if response.status_code == 200:
                                data.response.json()
                        else:
                                print('Request failed with status code:', response.status_code)

                        await ctx.send(response)

		@waifu.command()
                async def oral(self, ctx):
                        """Get a random oral image from Waifu.im"""
			"""Usage: [p]waifu oral"""
                        url = 'https://api.waifu.im/search'
                        params = {
                                'included_tags': ['oral'],
                                'height': '>=2000'
                                }

                        response = requests.get(url, parames=params)

                        if response.status_code == 200:
                                data.response.json()
                        else:
                                print('Request failed with status code:', respoms.status_code)

                        await ctx.send(response)

		@waifu.command()
                async def ecchi(self, ctx):
                        """Get a random ecchi image from Waifu.im"""
			"""Usage: [p]waifu ecchi"""
                        url = 'https://api.waifu.im/search'
                        params = {
                                'included_tags': ['ecchi'],
                                'height': '>=2000'
                                }

                        response = requests.get(url, parames=params)

                        if response.status_code == 200:
                                data.response.json()
                        else:
                                print('Request failed with status code:', response.status_code)

                        await ctx.send(response)

		@waifu.command()
                async def ero(self, ctx):
                        """Get a random ero image from Waifu.im"""
			"""Usage: [p]waifu ero"""
                        url = 'https://api.waifu.im/search'
                        params = {
                                'included_tags': ['ero'],
                                'height': '>=2000'
                                }

                        response = requests.get(url, parames=params)

                        if response.status_code == 200:
                                data.response.json()
                        else:
                                print('Request failed with status code:', response.status_code)

                        await ctx.send(response)

		@waifu.command()
                async def uniform(self, ctx):
                        """Get a random uniform image from Waifu.im"""
			"""Usage: [p]waifu uniform"""
                        url = 'https://api.waifu.im/search'
                        params = {
                                'included_tags': ['uniform'],
                                'height': '>=2000'
                                }

                        response = requests.get(url, parames=params)

                        if response.status_code == 200:
                                data.response.json()
                        else:
                                print(('Request failed with error code', response.status_code)

                        return await ctx.send(response)

		@waifu.command()
                async def paizuri(self, ctx):
                        """Get a random paizuri image from Waifu.im"""
			"""Usage: [p]waifu paizuri"""
                        url = 'https://api.waifu.im/search'
                        params = {
                                'included_tags': ['paizuri'],
                                'height': '>=2000'
                                }

                        response = requests.get(url, parames=params)

                        if response.status_code == 200:
                                data.response.json()
                        else:
                                print('Request failed with status code:', response.status_code)

                        await ctx.send(response)


	@commands.Cog.listener()
	async def on_command_error(self, ctx):
		if isinstance(error, commands.errors.NSFWChannelRequired):

		msg.title = "NSFW Command"
		msg.description = error.args[0]

		return await ctx.send(embed=msg) 
