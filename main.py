import discord
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.message_content = True  # Necessary for receiving message content

bot = commands.Bot(command_prefix="!", intents=intents)

@tasks.loop(seconds=5)
async def change_bot_status():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="KVA OFFICIAL"))

@bot.event
async def on_ready():
    print("Bot is online")
    change_bot_status.start()

@bot.command()
async def say(ctx, *, message: str):
    await ctx.message.delete()
    await ctx.send(message)

@bot.command()
async def ytlinks(ctx):
    embed = discord.Embed(
        title="Sample Embed",
        description="https://youtube.com/@pazhashixgod?feature=shared",
        color=discord.Color.blue()  # You can use any color from discord.Color
    )
    embed.add_field(name="Youtube Links <:YouTube:1070941400813817927>", value="This is the value of field 1 @everyone", inline=False)
    embed.add_field(name="Field 2", value="This is the value of field 2", inline=True)
    embed.set_footer(text="KVA FAM | DEVELOPERS")
    embed.set_thumbnail(url="https://example.com/thumbnail.png")
    embed.set_image(url="https://example.com/image.png")

    await ctx.send(embed=embed)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run("MTA0MTYzODczNDc3MDIyMTExNg.GGkd16.7CqYg8dEpRTuBbKxG7vpIxkHdJdufySzLQVafI")
