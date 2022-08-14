import json, os, discord, time
from discord.commands import SlashCommand, ApplicationContext, Option

with open("./config.json", "r", encoding="utf-8") as config: config = json.loads(config.read())
if not os.path.exists("./templates"): os.mkdir("./templates")


bot = discord.Bot(intents=discord.Intents.all(), debug_guilds=[876086663368032256])



@bot.command(description="Sends the bot's latency.") # this decorator makes a slash command
async def sobesedovanie(ctx: ApplicationContext, user: Option(discord.User, name="собеседуемый", required=True)): # a slash command will be created with the name "ping"
    
    
    
    embed=discord.Embed(title="Полное досье", url="https://flyclipart.com/thumb2/embed-generator-discord-bots-703977.png", description="Описание досье", color=0xffffff)
    embed.set_thumbnail(url="https://flyclipart.com/thumb2/embed-generator-discord-bots-703977.png")
    await ctx.send(embed=embed)


bot.run(config["d_token"])