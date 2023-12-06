from .waifu import Waifu

async def setup(bot):
	await bot.add_cog(Waifu(bot))
