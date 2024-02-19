import discord
import datetime

from redbot.core import Config, commands
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
        
        logger_channel = self.bot.get_channel(await self.config.logger_channel())
            
        e = discord.Embed(title='Logger', description='The bot has been added to a new guild.', timestamp=datetime.datetime.now())
        e.add_field(name='Guild Name', value=guild.name, inline=True),
        e.add_field(name='Guild ID', value='||{}||'.format(guild.id), inline=True)
        e.add_field(name="Joined At", value=datetime.strftime('%a %d %b %Y - %I:%M %p'), inline=False)
        e.set_footer(text='Powered by Red-DiscordBot', icon_url=self.bot.user.display_avatar.url)
        await logger_channel.send(embed=e)
        
            