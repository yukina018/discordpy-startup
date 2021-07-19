from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def neko(ctx):
    await ctx.send('にゃん') 

@bot.command()
async def チャーミィ(ctx):
    await ctx.send('はじめまして！ボクCHARMの妖精チャーミィ☆') 
    
@bot.command()
async def ラスバレ(ctx):
    await ctx.send('https://assaultlily.bushimo.jp/' ) 
    
@bot.command()
async def ツイッター(ctx):
    await ctx.send('https://twitter.com/assaultlily_lb') 
    
@bot.command()
async def 画像(ctx):
    await ctx.send('https://twitter.com/assaultlily_lb/status/1416774770331316224/photo/1') 
    
@bot.command()
async def ヘルプ(ctx):
    await ctx.send('コマンド一覧だよ！\n・/ラスバレ\n・/ツイッター\n・/画像') 
    
@bot.command()
async def ヒーラー(ctx):
    await ctx.send('https://drive.google.com/file/d/17X1a_HkkNUOycIylK0g6yQQa1jeHxJx2/view?usp=sharing') 
    
@bot.command()
async def ヒーラー2(ctx):
    await ctx.send('https://drive.google.com/file/d/1tqyVpv-fq072y5cEr0FboIsV9P3XmrnQ/view?usp=sharing') 
    
@bot.command()
async def 資料(ctx):
    await ctx.send('https://drive.google.com/file/d/1CmqSft5-7YsCYWiTKP14xHi0qhHbnGUd/view?usp=sharing') 
 

@bot.event
async def on_message(ctx):
    if ctx.channel.id != 866022441029206016: # チャンネルが違う場合は無視する
        return

    await bot.process_commands(ctx)
    
        
bot.run(token)
