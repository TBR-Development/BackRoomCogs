from typing import Literal

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
            logger_channel = '',
            guild_logs = '',
            error_logs = '',
            console_logs = ''
            )
                
    @commands.hybrid_group()
    @commands.is_owner()
    async def logger(self, ctx):
        """
        Base command for the Logger cog
        """
        return
    
    @logger.command()
    async def enable(self, ctx, channel: discord.TextChannel):
        """
        Set the channel to send logs to
        """
        
        await self.config.logger_channel.set(channel.id)
        await ctx.send('Logger has been enabled in: <#{}>.'.format(channel.id))
        
    @logger.command()
    async def disable(self, ctx):
        """
        Remove the logger channel
        """
        
        await self.config.logger_channel.clear()
        await ctx.send('Logger has been disabled.')
        
    @logger.command()
    async def settings(self, ctx):
        """
        View the logger config
        """
        
        if self.config.logger_channel == None:
            logs_channel = 'No channel set'
            logger_enabled='False'
        else:
            c = self.bot.get_channel(await self.config.logger_channel())
            logs_channel = '{} ({})'.format(c, c.id)
            logger_enabled='True'
            
        embed = discord.Embed(title='Logger Settings')
        embed.color = await ctx.embed_color()
        embed.add_field(name='Enabled', value=logger_enabled)
        embed.add_field(name='Channel', value=box(logs_channel))
        embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.display_avatar.url)
        
        await ctx.send(embed=embed)
                
        
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        """
        Guild add event
        """
        
        raw = datetime.now()
        
        date_time = raw.strftime('%B %d, %Y - %H:%M')
        
        logs_channel = self.bot.get_channel(await self.config.logger_channel())
        description = '{} has been added to a guild.'.format(self.bot.user.name)
            
        embed = discord.Embed(description=description, color=discord.Color.blue())
        embed.add_field(name='Guild', value=guild.name, inline=True),
        embed.add_field(name='Date', value=date_time, inline=True)
        embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.display_avatar.url)
        
        await logs_channel.send(embed=embed)
        
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        """
        Guild remove event
        """
        
        raw = datetime.now()
        
        date_time = raw.strftime('%B %d, %Y - %H:%M')
        
        logs_channel = self.bot.get_channel(await self.config.logger_channel())
        description = '{} has been removed from a guild.'.format(self.bot.user.name)
            
        embed = discord.Embed(description=description, color=discord.Color.red())
        embed.add_field(name='Guild', value=guild.name, inline=True),
        embed.add_field(name='Date', value=date_time, inline=True)
        embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.display_avatar.url)
        
        await logs_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_command_error(self, error):
        """
        Command error event 
        """
        logs_channel = self.bot.get_channel(await self.config.logger_channel())
        await ctx.send(str(error))
        t=traceback.format_exc()
        
        await logs_channel.send('```py\n{}```'.format(t))
        
