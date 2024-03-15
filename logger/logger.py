from typing import Literal

import discord

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
            logger_channel=''
        )
        
    
    @commands.hybrid_command()
    async def loggerchannel(self, ctx, option: Literal['set', 'remove']):
        """
        Set the channel to send the logs to
        """
        
        channel = ctx.channel
        
        if option == 'set':
            await self.config.logger_channel.set(channel.id)
            await ctx.send('The logger channel has been set to: <#{}>.'.format(channel.id))
        else:
            if option == 'remove':
                await self.config.logger_channel.clear()
                await ctx.send('The logger channel has been removed.')
                
        
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        """
        Log guild add events
        """
        
        date = datetime.now()
        
        join_date = date.strftime('%B %d, %Y - %H:%M')
        
        logs_channel = self.bot.get_channel(await self.config.logger_channel())
            
        embed = discord.Embed(title='Logger', description='{} has been added to a guild.'.format(self.bot.user.name), timestamp=date, color=discord.Color.blue())
        embed.add_field(name='Guild', value='{} ({})'.format(guild.name, guild.id), inline=True),
        embed.add_field(name='Date Added', value=join_date, inline=False)
        embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.display_avatar.url)
        await logs_channel.send(embed=embed)
        
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        """
        Log guild remove events
        """
        
        date = datetime.now()
        
        leave_date = date.strftime('%B %d, %Y - %H:%M')
        
        logs_channel = self.bot.get_channel(await self.config.logger_channel())
            
        embed = discord.Embed(title='Logger', description='{} has been removed from a guild.'.format(self.bot.user.name), timestamp=date, color=discord.Color.blue())
        embed.add_field(name='Guild Name', value=guild.name, inline=True),
        embed.add_field(name='Date Removed', value=leave_date, inline=False)
        embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.display_avatar.url)
        await logs_channel.send(embed=embed)
        