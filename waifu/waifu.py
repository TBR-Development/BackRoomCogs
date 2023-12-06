from redbot.core import commands


class Waifu(commands.Cog):
        """Waifu images commands using Waifu.im API"""
        def __init__(self, bot):
               
                @commands.Command()
                @commands.is_nsfw()
                async def waifu(self, ctx):
                        tag = 'waifu'
        
                        await ctx.send('https://api.waifu.im/search?included_tags={tag}')

                @commands.Command()
                @commands.is_nsfw()
                async def uniform(self, ctx):
                        tag = 'uniform'
        
                        await ctx.send('https://api.waifu.im/search?included_tags={tag}')
                
                @commands.Command()
                @commands.is_nsfw()
                async def maid(self, ctx):
                        tag = 'maid'
        
                        await ctx.send('https://api.waifu.im/search?included_tags={tag}')

                @commands.Command()
                @commands.is_nsfw()
                async def marin(self, ctx):
                        tag = 'marin-kitagawa'
        
                        await ctx.send('https://api.waifu.im/search?included_tags={tag}')
                
                @commands.Command()
                @commands.is_nsfw()
                async def raiden(self, ctx):
                        tag = 'raiden-shogun'
        
                        await ctx.send('https://api.waifu.im/search?included_tags={tag}')

                @commands.Command()
                @commands.is_nsfw()
                async def mori(self, ctx):
                        tag = 'mori-calliope'
        
                        await ctx.send('https://api.waifu.im/search?included_tags={tag}')

                @commands.Command()
                @commands.is_nsfw()
                async def oppai(self, ctx):
                        tag = 'oppai'
        
                        await ctx.send('https://api.waifu.im/search?included_tags={tag}')

                @commands.Command()
                @commands.is_nsfw()
                async def ass(self, ctx):
                        tag = 'ass'
        
                        await ctx.send('https://api.waifu.im/search?included_tags={tag}')

                @commands.Command()
                @commands.is_nsfw()
                async def milf(self, ctx):
                        tag = 'milf'
        
                        await ctx.send('https://api.waifu.im/search?included_tags={tag}')

                @commands.Command()
                @commands.is_nsfw()
                async def hentai(self, ctx):
                        tag = 'hentai'
        
                        await ctx.send('https://api.waifu.im/search?included_tags={tag}')

                @commands.Command()
                @commands.is_nsfw()
                async def oral(self, ctx):
                        tag = 'oral'
        
                        await ctx.send('https://api.waifu.im/search?included_tags={tag}')

                @commands.Command()
                @commands.is_nsfw()
                async def paizuri(self, ctx):
                        tag = 'paizuri'
        
                        await ctx.send('https://api.waifu.im/search?included_tags={tag}')

                @commands.Command()
                @commands.is_nsfw()
                async def ecchi(self, ctx):
                        tag = 'ecchi'
        
                        await ctx.send('https://api.waifu.im/search?included_tags={tag}')

                @commands.Command()
                @commands.is_nsfw()
                async def ero(self, ctx):
                        tag = 'ero'
        
                        await ctx.send('https://api.waifu.im/search?included_tags={tag}')


	        @commands.Cog.listener()
	        async def on_command_error(self, ctx):

                        if isinstance(error, commands.errors.NSFWChannelRequired):

		        msg.title = 'NSFW Command'
		        msg.description = 'This command must be run in and NSFW channel.'

		        return await ctx.send(embed=msg) 
