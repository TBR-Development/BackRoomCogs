from .logger import Logger

async def setup(bot):
    await bot.add_cog(Logger(bot))