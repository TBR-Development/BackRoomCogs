from .waifuim import Waifus

async def setup(bot):
	await bot.add_cog(WaifuIM(bot))
