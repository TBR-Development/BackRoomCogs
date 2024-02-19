import discord

from redbot.core import Config, commands

from datetime import datetime
from typing import Final

class Logger(commands.Cog):
    """
    Logger cog for logging events to a specified channel
    """
    
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=465228604721201158)
        
        self.config.register_global(
            logger_channel=True
        )
        
    
    @commands.group()
    @commands.is_owner()
    async def logger(self, ctx):
        """
        Logger setup command
        """
        pass
    
    @logger.command(name='channel')
    async def set_channel(self, ctx, channel: discord.TextChannel):
        """
        Set the logging channel to send the logs to
        """
        
        await self.config.logger_channel.set(channel.id)
        
        await ctx.send('Successfully enabled logger') 
        
        
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        """
        Log guild join events to the logger channel if it is set
        """
        
        date = datetime.now()
        
        join_date = date.strftime('%a %d %b %Y, %I:%M %p')
        
        logger_channel = self.bot.get_channel(await self.config.logger_channel())
            
        e = discord.Embed(title='Logger', description='The bot has been added to a new guild.', timestamp=date)
        e.add_field(name='Guild Name', value=guild.name, inline=True),
        e.add_field(name='Guild ID', value='||{}||'.format(guild.id), inline=True)
        e.add_field(name='Join Date', value=join_date, inline=False)
        e.color(discord.Color.blue())
        e.set_footer(text=self.bot.user.name, icon_url=self.bot.user.display_avatar.url)
        await logger_channel.send(embed=e)
        
            