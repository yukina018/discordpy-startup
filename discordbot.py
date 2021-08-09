from discord.ext import commands
import os
import traceback
import requests

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    

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
    await ctx.send('コマンド一覧だよ！\n/ラスバレ\n/ツイッター\n/画像\n/資料') 
 
    
@bot.command()
async def 資料(ctx):
    await ctx.send('https://drive.google.com/file/d/1FFhDMTinBL7HwlZNPV2jGh0uAS0Iq1SJ/view?usp=sharing') 
    
    
@bot.event
async def on_message(ctx):
    if ctx.channel.id != 866022441029206016: # チャンネルが違う場合は無視する
        return

    await bot.process_commands(ctx)
    

 
webhook_url = 'https://discord.com/api/webhooks/874273799418310657/SFQ9K9zswagU_xCSXmj9fLS38yC35_XcTFl_fnBvEJljWPalAkVO_Wjx92Imxon7Q20e'
 
 
main_content = {
  "username": "公式情報BOT",
  "avatar_url": "https://www.google.co.jp/images/branding/googlelogo/2x/googlelogo_color_120x44dp.png",
  "content": "コンテンツの中身:grinning: :grimacing: "
}
 
requests.post(webhook_url, main_content)
    
    
bot.run(token)
