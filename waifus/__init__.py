from .waifus import Waifus

async def setup(bot):
	await bot.add_cog(Waifus(bot))
