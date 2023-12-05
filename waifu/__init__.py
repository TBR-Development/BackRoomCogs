from .Waifu import Waifu

async def setup(bot):
	await bot.add(Waifu(bot))
