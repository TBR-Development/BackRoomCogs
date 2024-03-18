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
        
        try:
            await self.config.logger_channel.set(channel.id)
            await ctx.send('Logger has been enabled in: <#{}>.'.format(channel.id))
        except:
            for p in pagify(''.join(traceback.TracebackException.from_exception(error).format()), shorten_by=10):
                await ctx.send(box(p, 'py'))
        
    @logger.command()
    async def disable(self, ctx):
        """
        Remove the logger channel
        """
        error = Exception
        
        try:
            await self.config.logger_channel.clear()
            await ctx.send('Logger has been disabled.')
        except:
            for p in pagify(''.join(traceback.TracebackException.from_exception(error).format()), shorten_by=10):
                await ctx.send(box(p, 'py'))
        
    @logger.command()
    async def settings(self, ctx):
        """
        View the logger config
        """
        logs_channel = self.bot.get_channel(await self.config.logger_channel())
        error = Exception
    
        try:
            if logs_channel is None:
                logs_channel = 'No channel set'
                logger_enabled = 'False'
                embed_color = await ctx.embed_color()
            else:
                channel = logs_channel 
                logs_channel = f'{channel} ({channel.id})'
                logger_enabled = 'True'
                embed_color = discord.Color.blue()

            d = f'Here are the current Logger settings.\n\n**Logger Enabled**: {logger_enabled}\n**Logger Channel**: {logs_channel}'
            
            e = discord.Embed(description=d, color=embed_color)
            await ctx.send(embed=e)
        except:
            for p in pagify(''.join(traceback.TracebackException.from_exception(error).format()), shorten_by=10):
                await ctx.send(box(p, 'py'))
             
    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        """
        Args:
            guild (discord.Guild)
        """
        logs_channel = self.bot.get_channel(await self.config.logger_channel())
        error = Exception
        
        try:
            if logs_channel is None:
                return
    
            now = datetime.now()
            date_time = now.strftime('%B %d, %Y - %I:%M %p')
            
            d = f'{self.bot.user.name} has been added to a guild.\n\n**Guild**: {guild.name} ({guild.id})\n**Date**: {date_time}'
            e = discord.Embed(description=d, color=discord.Color.blue())
            
            await logs_channel.send(embed=e)
        except:
            for p in pagify(''.join(traceback.TracebackException.from_exception(error).format()), shorten_by=10):
                await logs_channel.send(box(p, 'py'))
        
    @commands.Cog.listener()
    async def on_guild_remove(self, guild: discord.Guild):
        """
        Args:
            guild (discord.Guild)
        """
        logs_channel = self.bot.get_channel(await self.config.logger_channel())
        error = Exception
        
        try:
            if logs_channel is None:
                return
        
            now = datetime.now()
            date_time = now.strftime('%B %d, %Y - %I:%M %p')
            
            d = f'{self.bot.user.name} has been removed from a guild.\n\n**Guild**: {guild.name} ({guild.id})\n**Date**: {date_time}'
            e = discord.Embed(description=d, color=discord.Color.red())
            
            await logs_channel.send(embed=e)
        except:
            for p in pagify(''.join(traceback.TracebackException.from_exception(error).format()), shorten_by=10):
                await logs_channel.send(box(p, 'py'))
        
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        """
        Args:
            member (discord.Member)
        """
        logs_channel = self.bot.get_channel(await self.config.logger_channel())
        error = Exception

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
            
            d = f'A user has joined a guild.\n\n**Member**: {member.name} ({member.id})\n**Bot**: {is_bot}\n**Created**: {created_date}\n**Guild**: {member.guild.name} ({member.guild.id})\n**Date**: {date_time}'
            e = discord.Embed(description=d, color=discord.Color.blue())
            
            await logs_channel.send(embed=e)
        except:
            d = f"**Guild**: {member.guild.name} ({member.guild.id})\n{box(str(error), 'py')}"
            e = discord.Embed(description=d, color=discord.Color.red())
            await logs_channel.send(embed=e)
            for p in pagify(''.join(traceback.TracebackException.from_exception(error).format()), shorten_by=10):
                await logs_channel.send(box(p, 'py'))
       

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        """
        Args:
            member (discord.Member)
        """
        logs_channel = self.bot.get_channel(await self.config.logger_channel())
        error = Exception

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
            
            d = f'A user has left a guild.\n\n**Member**: {member.name} ({member.id})\n**Bot**: {is_bot}\n**Created**: {created_date}\n**Guild**: {member.guild.name} ({member.guild.id})\n**Date**: {date_time}'
            e = discord.Embed(description=d, color=discord.Color.red())
            
            await logs_channel.send(embed=e)
        except:
            d = f"{box(str(error), 'py')}\n**Guild**: {member.guild.name} ({member.guild.id})"
            e = discord.Embed(description=d, color=discord.Color.red())
            await logs_channel.send(embed=e)
            for p in pagify(''.join(traceback.TracebackException.from_exception(error).format()), shorten_by=10):
                await logs_channel.send(box(p, 'py'))
        
    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: Exception):
        """
        Args:
            ctx (commands.Context)
            error (Exception)
        """
        logs_channel = self.bot.get_channel(await self.config.logger_channel())
        
        if logs_channel is None:
            return
        
        if isinstance(error, commands.MissingRequiredArgument):
            try:
                ctx.send(f"Missing required argument(s).\n\nUse `[p]help {ctx.command}` to learn how to use this command.")
                for p in pagify(''.join(traceback.TracebackException.from_exception(error).format()), shorten_by=10):
                    await logs_channel.send(box(p, 'py'))
            except:
                d = f"{box(str(error), 'py')}\n**Guild**: {ctx.guild.name} ({ctx.guild.id})"
                e = discord.Embed(description=d, color=discord.Color.red())
                await logs_channel.send(embed=e)
                for p in pagify(''.join(traceback.TracebackException.from_exception(error).format()), shorten_by=10):
                    await logs_channel.send(box(p, 'py'))
        elif isinstance(error, commands.MemberNotFound):
            try:
                await ctx.send(f"I could not find member: `{error.argument}`. Please try again.")
                for p in pagify(''.join(traceback.TracebackException.from_exception(error).format()), shorten_by=10):
                    await logs_channel.send(box(p, 'py'))
            except:
                d = f"{box(str(error), 'py')}\n**Guild**: {ctx.guild.name} ({ctx.guild.id})"
                e = discord.Embed(description=d, color=discord.Color.red())
                await logs_channel.send(embed=e)
                for p in pagify(''.join(traceback.TracebackException.from_exception(error).format()), shorten_by=10):
                    await logs_channel.send(box(p, 'py'))
        elif isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.send(f"`The command: `{ctx.command}` cannot be used inprivate messages.")
                for p in pagify(''.join(traceback.TracebackException.from_exception(error).format()), shorten_by=10):
                    await logs_channel.send(box(p, 'py'))
            except:
                d = f"{box(str(error), 'py')}\n**Guild**: {ctx.guild.name} ({ctx.guild.id})"
                e = discord.Embed(description=d, color=discord.Color.red())
                await logs_channel.send(embed=e)
                for p in pagify(''.join(traceback.TracebackException.from_exception(error).format()), shorten_by=10):
                    await logs_channel.send(box(p, 'py'))
        elif isinstance(error, commands.CommandNotFound):
            pass
        else:
            try:
                d = f"{box(str(error), 'py')}\n***Commands**: {ctx.command}\n*Guild**: {ctx.guild.name} ({ctx.guild.id})"
                e = discord.Embed(description=d, color=discord.Color.red())
                await logs_channel.send(embed=e)
                for p in pagify(''.join(traceback.TracebackException.from_exception(error).format()), shorten_by=10):
                    await logs_channel.send(box(p, 'py'))
            except:
                d = f"{box(str(error), 'py')}\n**Guild**: {ctx.guild.name} ({ctx.guild.id})"
                e = discord.Embed(description=d, color=discord.Color.red())
                await logs_channel.send(embed=e)
                for p in pagify(''.join(traceback.TracebackException.from_exception(error).format()), shorten_by=10):
                    await logs_channel.send(box(p, 'py'))

    @commands.Cog.listener()
    async def on_app_command_error(self, interaction: discord.Interaction, error: Exception):
        """
        Args:
            interaction (discord.Interaction)
            error (Exception)
        """
        logs_channel = self.bot.get_channel(await self.config.logger_channel())
        
        if logs_channel is None:
            return
        
        if isinstance(error, commands.MissingRequiredArgument):
            try:
                await interaction.reply(f"Missing required argument(s).\n\nUse `[p]help {interaction.command}` to learn how to use this command.")
                for p in pagify(''.join(traceback.TracebackException.from_exception(error).format()), shorten_by=10):
                    await logs_channel.send(box(p, 'py'))
            except:
                d = f"{box(str(error), 'py')}\n**Guild**: {interaction.guild.name} ({interaction.guild.id})"
                e = discord.Embed(description=d, color=discord.Color.red())
                await logs_channel.send(embed=e)
                for p in pagify(''.join(traceback.TracebackException.from_exception(error).format()), shorten_by=10):
                    await logs_channel.send(box(p, 'py'))
        elif isinstance(error, commands.MemberNotFound):
            try:
                await interaction.reply(f"I could not find member: `{error.argument}`. Please try again.")
                for p in pagify(''.join(traceback.TracebackException.from_exception(error).format()), shorten_by=10):
                    await logs_channel.send(box(p, 'py'))
            except:
                d = f"{box(str(error), 'py')}\n**Guild**: {interaction.guild.name} ({interaction.guild.id})"
                e = discord.Embed(description=d, color=discord.Color.red())
                await logs_channel.send(embed=e)
                for p in pagify(''.join(traceback.TracebackException.from_exception(error).format()), shorten_by=10):
                    await logs_channel.send(box(p, 'py'))
        elif isinstance(error, commands.NoPrivateMessage):
            try:
                await interaction.reply(f"`The command: `{interaction.command}` cannot be used in private messages.")
                for p in pagify(''.join(traceback.TracebackException.from_exception(error).format()), shorten_by=10):
                    await logs_channel.send(box(p, 'py'))
            except:
                d = f"{box(str(error), 'py')}\n**Guild**: {interaction.guild.name} ({interaction.guild.id})"
                e = discord.Embed(description=d, color=discord.Color.red())
                await logs_channel.send(embed=e)
                for p in pagify(''.join(traceback.TracebackException.from_exception(error).format()), shorten_by=10):
                    await logs_channel.send(box(p, 'py'))
        elif isinstance(error, commands.CommandNotFound):
            pass
        else:
            try:
                d = f"{box(str(error), 'py')}\n**Command**: {interaction.command}\n**Guild**: {interaction.guild.name} ({interaction.guild.id})"
                e = discord.Embed(description=d, color=discord.Color.red())
                await logs_channel.send(embed=e)
                for p in pagify(''.join(traceback.TracebackException.from_exception(error).format()), shorten_by=10):
                    await logs_channel.send(box(p, 'py'))
            except:
                d = f"{box(str(error), 'py')}\n**Guild**: {interaction.guild.name} ({interaction.guild.id})"
                e = discord.Embed(description=d, color=discord.Color.red())
                await logs_channel.send(embed=e)
                for p in pagify(''.join(traceback.TracebackException.from_exception(error).format()), shorten_by=10):
                    await logs_channel.send(box(p, 'py'))
