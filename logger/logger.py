import discord
import traceback

from redbot.core import Config, commands
from redbot.core.utils.chat_formatting import box

from datetime import datetime

class Logger(commands.Cog):
    """
    Log events to a discord channel.
    """
    
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=465228604721201158)
        
        self.config.register_global(
            guilds_channel=True,
            errors_channel=True
        )
        
    
    @commands.group(name='loggerset')
    @commands.is_owner()
    async def logger_set(self, ctx):
        """
        Logger setup command
        """
        pass
    
    @logger_set.command(name='guildschannel')
    async def guilds_channel(self, ctx, channel: discord.TextChannel):
        """
        Set the logging channel to send the guild logs to
        """
        
        await self.config.guilds_channel.set(channel.id)
        
        await ctx.send('Successfully set Guild Logs Channel') 
    
    @logger_set.command(name='errorschannel', hidden=True)
    async def errors_channel(self, ctx, channel: discord.TextChannel):
        """
        Set the logging channel to send the error logs to
        """
        
        await self.config.errors_channel.set(channel.id)
        
        await ctx.send('Successfully set Error Logs Channel') 
        
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        """
        Log guild add events
        """
        
        date = datetime.now()
        
        join_date = date.strftime('%a %d %b %Y, %I:%M %p')
        
        logs_channel = self.bot.get_channel(await self.config.guilds_channel())
            
        e = discord.Embed(title='Logger', description='{} has been added to a guild.'.format(self.bot.user.name), timestamp=date, color=discord.Color.blue())
        e.add_field(name='Guild Name', value=guild.name, inline=True),
        e.add_field(name='Guild ID', value='||{}||'.format(guild.id), inline=True)
        e.add_field(name='Date Added', value=join_date, inline=False)
        e.set_footer(text=self.bot.user.name, icon_url=self.bot.user.display_avatar.url)
        await logs_channel.send(embed=e)
        
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        """
        Log guild remove events
        """
        
        date = datetime.now()
        
        leave_date = date.strftime('%a %d %b %Y, %I:%M %p')
        
        logs_channel = self.bot.get_channel(await self.config.guilds_channel())
            
        e = discord.Embed(title='Logger', description='{} has been removed from a guild.'.format(self.bot.user.name), timestamp=date, color=discord.Color.blue())
        e.add_field(name='Guild Name', value=guild.name, inline=True),
        e.add_field(name='Date Removed', value=leave_date, inline=False)
        e.set_footer(text=self.bot.user.name, icon_url=self.bot.user.display_avatar.url)
        await logs_channel.send(embed=e)
        
    @commands.Cog.listener()
    async def on_error(self, guild):
        """
        Log error events
        
        Notes:
        
        - This feature is a work in progress
        - It might not trigger a response in it's current state
        """
        date = datetime.now()
        
        leave_date = date.strftime('%a %d %b %Y, %I:%M %p')
        
        logs_channel = self.bot.get_channel(await self.config.errors_channel())
        
        e = discord.Embed(title='Logger', description='An error has been logged', timestamp=date, color=discord.Color.red())
        e.add_field(name='Guild Name', value=guild.name, inline=True)
        e.add_field(name='Guild ID', value='||{}||'.format(guild.id), inline=True)
        e.add_field(name='Error Stack', value=box(traceback.format_exc()), inline=False)
        e.add_field(name='Error Date', value=leave_date, inline=False)
        e.set_footer(text=self.bot.user.name, icon_url=self.bot.user.display_avatar.url)
        await logs_channel.send(embed=e)