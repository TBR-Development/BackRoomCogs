from typing import Literal

import discord
import traceback

from redbot.core import Config, commands
from redbot.core.utils.chat_formatting import box, pagify

from datetime import datetime

class Logger(commands.Cog):
    """
    Logger cog for use with debugging and support.
    """
    
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=465228604721201158)
        
        self.config.register_global(
            logger_channel = ''
        )
                
    @commands.hybrid_group()
    @commands.is_owner()
    async def logger(self, ctx):
        """
        Enable or disable Logger
        """
        return
    
    @logger.command()
    async def enable(self, ctx, channel: discord.TextChannel):
        """
        Set the Logger channel

        ```
        channel: The channel to send the logs to
        ```
        """
        error = Exception
        
        async def send_error():
            e = discord.Embed(description=str(error), color=discord.Color.red())
            ctx.send(embed=e)
            for p in pagify(traceback.format_exc(), shorten_by=10):
                ctx.send(box(p, 'py'))
        
        try:
            await self.config.logger_channel.set(channel.id)
            await ctx.send('Logger has been enabled in: `{} ({})`'.format(channel, channel.id))
        except:
            await send_error()
        
    @logger.command()
    async def disable(self, ctx):
        """
        Remove the logger channel
        """
        error = Exception
        
        async def send_error():
            e = discord.Embed(description=str(error), color=discord.Color.red())
            ctx.send(embed=e)
            for p in pagify(traceback.format_exc(), shorten_by=10):
                ctx.send(box(p, 'py'))
        
        try:
            await self.config.logger_channel.clear()
            await ctx.send('Logger has been disabled.')
        except:
            await send_error()
        
    @logger.command()
    async def settings(self, ctx):
        """
        View the logger config
        """
        logs_channel = self.bot.get_channel(await self.config.logger_channel())
        error = Exception
        
        async def send_error():
            e = discord.Embed(description=str(error), color=discord.Color.red())
            ctx.send(embed=e)
            for p in pagify(traceback.format_exc(), shorten_by=10):
                ctx.send(box(p, 'py'))
        try:
            if logs_channel is None:
                channel = 'No channel set'
                enabled = 'False'
                color = await ctx.embed_color()
            else: 
                channel = f'{logs_channel} ({logs_channel.id})'
                enabled = 'True'
                color = discord.Color.blue()

            d = f'Here are the current Logger settings.\n\n**Enabled**: {enabled}\n**Channel**: {channel}'
            e = discord.Embed(description=d, color=color)
            await ctx.send(embed=e)
        except:
            await send_error()
             
    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        """
        Args:
            guild: discord.Guild
        """
        logs_channel = self.bot.get_channel(await self.config.logger_channel())
        error = Exception
        
        if logs_channel is None:
            return
        
        async def send_error():
            for p in pagify(''.join(traceback.TracebackException.from_exception(error).format()), shorten_by=10):
                await logs_channel.send(box(p, 'py'))
                
        try:
            now = datetime.now()
            date_time = now.strftime('%B %d, %Y - %I:%M %p')
            
            d = f'{self.bot.user.name} has been added to a guild.\n\n**Guild**: {guild} ({guild.id})\n**Date**: {date_time}'
            e = discord.Embed(description=d, color=discord.Color.blue())
            
            await logs_channel.send(embed=e)
        except:
            await send_error()
        
    @commands.Cog.listener()
    async def on_guild_remove(self, guild: discord.Guild):
        """
        Params:
            guild: discord.Guild
        """
        logs_channel = self.bot.get_channel(await self.config.logger_channel())
        error = Exception
        
        if logs_channel is None:
            return
        
        async def send_error():
            for p in pagify(''.join(traceback.TracebackException.from_exception(error).format()), shorten_by=10):
                await logs_channel.send(box(p, 'py'))
        
        try:
            now = datetime.now()
            date_time = now.strftime('%B %d, %Y - %I:%M %p')
            
            d = f'{self.bot.user.name} has been removed from a guild.\n\n**Guild**: {guild} ({guild.id})\n**Date**: {date_time}'
            e = discord.Embed(description=d, color=discord.Color.red())
            
            await logs_channel.send(embed=e)
        except:
            await send_error()
        
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        """
        Params:
            member: discord.Member
        """
        logs_channel = self.bot.get_channel(await self.config.logger_channel())
        error = Exception
        
        async def send_error():
            d = f"**Guild**: {member.guild} ({member.guild.id})"
            e = discord.Embed(title=str(error), description=d, color=discord.Color.red())
            await logs_channel.send(embed=e)
            for p in pagify(''.join(traceback.TracebackException.from_exception(error).format()), shorten_by=10):
                await logs_channel.send(box(p, 'py'))

        try:
            if logs_channel is None:
                return
            
            if member.bot == True:
                is_bot = 'True'
            else:
                is_bot = 'False'
        
            now = datetime.now()
            created_at = member.created_at
            
            date_time = now.strftime('%B %d, %Y - %I:%M %p')
            created_date = created_at.strftime('%B %d, %Y - %I:%M %p')
            
            d = f'A user has joined a guild.\n\n**Member**: {member.name} ({member.id})\n**Bot**: {is_bot}\n**Created**: {created_date}\n**Guild**: {member.guild} ({member.guild.id})\n**Date**: {date_time}'
            e = discord.Embed(description=d, color=discord.Color.blue())
            
            await logs_channel.send(embed=e)
        except:
            await send_error()
       

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        """
        Params:
            member: discord.Member
        """
        logs_channel = self.bot.get_channel(await self.config.logger_channel())
        error = Exception
        
        now = datetime.now()
        date_time = now.strftime('%B %d, %Y - %I:%M %p')
        
        async def send_error():
            d = f"**Guild**: {member.guild} ({member.guild.id})\n**Date**: {date_time}"
            e = discord.Embed(title=str(error), description=d, color=discord.Color.red())
            await logs_channel.send(embed=e)
            for p in pagify(''.join(traceback.TracebackException.from_exception(error).format()), shorten_by=10):
                await logs_channel.send(box(p, 'py'))

        try:
            if logs_channel is None:
                return
            
            if member.bot == True:
                is_bot = 'True'
            else:
                is_bot = 'False'
            
            now = datetime.now()
            created_at = member.created_at
            
            date_time = now.strftime('%B %d, %Y - %I:%M %p')
            created_date = created_at.strftime('%B %d, %Y - %I:%M %p')
            
            d = f'A user has left a guild.\n\n**Member**: {member.name} ({member.id})\n**Bot**: {is_bot}\n**Created**: {created_date}\n**Guild**: {member.guild} ({member.guild.id})\n**Date**: {date_time}'
            e = discord.Embed(description=d, color=discord.Color.red())
            
            await logs_channel.send(embed=e)
        except:
            await send_error()
            
    @commands.Cog.listener()
    async def on_error(self, error: Exception):
        """
        Params:
            error: Exception
        """
        logs_channel = self.bot.get_channel(await self.config.logger_channel())
        
        if logs_channel is None:
            return
        
        async def send_error():
            e = discord.Embed(description=str(error), color=discord.Color.red())
            await logs_channel.send(embed=e)
            for p in pagify(''.join(traceback.TracebackException.from_exception(error).format()), shorten_by=10):
                await logs_channel.send(box(p, 'py'))
                
        await send_error()
        
    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: Exception):
        """
        Params:
            ctx: commands.Context
            error: Exception
        """
        logs_channel = self.bot.get_channel(await self.config.logger_channel())
        
        now = datetime.now()
        date_time = now.strftime('%B %d, %Y - %I:%M %p')
        
        if logs_channel is None:
            return
        
        async def send_error():
            if ctx.command == None:
                d = f"**Guild**: {ctx.guild} ({ctx.guild.id})\n**Date**: {date_time}"
            else:
                d = f"**Command**: {ctx.command}\n**Invoker**: {ctx.member.name} ({ctx.member.id})\n**Guild**: {ctx.guild} ({ctx.guild.id})\n**Date**: {date_time}"
            e = discord.Embed(title=str(error), description=d, color=discord.Color.red())
            await logs_channel.send(embed=e)
            for p in pagify(''.join(traceback.TracebackException.from_exception(error).format()), shorten_by=10):
                await logs_channel.send(box(p, 'py'))
        
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Missing required argument(s).\n\nUse `[p]help {ctx.command}` to learn how to use this command.")
            await send_error()
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send(f"I could not find member: `{error.argument}`. Please try again.")
            await send_error()
        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.send(f"`The command: `{ctx.command}` cannot be used in private messages.")
            await send_error()
# --------------------------------------------------------------------------------------------------------------------------------------------- #
        elif isinstance(error, commands.CommandNotFound):
            pass
# --------------------------------------------------------------------------------------------------------------------------------------------- #
        else:
            await send_error()

    @commands.Cog.listener()
    async def on_app_command_error(self, interaction: discord.Interaction, error: Exception):
        """
        Params:
            interaction: discord.Interaction
            error: Exception
        """
        logs_channel = self.bot.get_channel(await self.config.logger_channel())
        
        now = datetime.now()
        date_time = now.strftime('%B %d, %Y - %I:%M %p')
        
        if logs_channel is None:
            return
        
        async def send_error():
            if interaction.command == None:
                d = f"**Guild**: {interaction.guild} ({interaction.guild.id})\n**Date**: {date_time}"
            else:
                d = f"**Command**: {interaction.command}\n**Invoker**: {interaction.member.name} ({interaction.member.id})\n**Guild**: {interaction.guild} ({interaction.guild.id})\n**Date**: {date_time}"
            e = discord.Embed(title=str(error), description=d, color=discord.Color.red())
            await logs_channel.send(embed=e)
            for p in pagify(''.join(traceback.TracebackException.from_exception(error).format()), shorten_by=10):
                await logs_channel.send(box(p, 'py'))
        
        if isinstance(error, commands.MissingRequiredArgument):
            await interaction.reply(f"Missing required argument(s).\n\nUse `[p]help {interaction.command}` to learn how to use this command.")
            await send_error()
        elif isinstance(error, commands.MemberNotFound):
            await interaction.reply(f"I could not find member: `{error.argument}`. Please try again.")
            await send_error()
        elif isinstance(error, commands.NoPrivateMessage):
            await interaction.reply(f"`The command: `{interaction.command}` cannot be used in private messages.")
            await send_error()
# --------------------------------------------------------------------------------------------------------------------------------------------- #
        elif isinstance(error, commands.CommandNotFound):
            pass
# --------------------------------------------------------------------------------------------------------------------------------------------- #
        else:
            await send_error()
