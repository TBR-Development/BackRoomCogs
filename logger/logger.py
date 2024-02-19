import discord

from redbot.core import Config, commands

from datetime import datetime
from typing import Final

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
        
    
    @commands.group()
    @commands.is_owner()
    async def logger(self, ctx):
        """
        Logger setup command
        """
        pass
    
    @logger.command(name='guildlogs')
    async def guildlogs_channel(self, ctx, channel: discord.TextChannel):
        """
        Set the logging channel to send the guild logs to
        """
        
        await self.config.guilds_channel.set(channel.id)
        
        await ctx.send('Successfully set Guild Logs Channel') 
        
    
    @logger.command(name='guildlogs')
    async def errorlogs_channel(self, ctx, channel: discord.TextChannel):
        """
        Set the logging channel to send the error logs to
        
        Notes:
        
        This feature is a work in progress. As such the Erro Handler is still not ready and won't trigger
        This command has been set in place so that it will be ready once the Error Handler has been completed.
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
        
            