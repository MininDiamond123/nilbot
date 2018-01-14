import discord
import random
import gui

bot = commands.Bot(command_prefix = "ch.", description = "This is a customized bot for The Clubhouse! If you have any suggestions, please tag a Bot Developer.", owner_id = 389472478545575937)

@bot.command()
async def flip(ctx):
    em = discord.Embed(color=discord.Color(value=0xb2acef))
    em.title = "Coinflip Results:"
    list = []
    for heads in range(0, 49):
        list.append("It landed on Heads.")
    for tails in range(0, 49):
        list.append("It landed on Tails.")
    for side in range(0, 2):
        list.append("It landed on the side!")
    flipped = random.choice(list)
    em.description = f"{flippeds}"
    await ctx.send(embed=em)





bot.run(os.environ.get("TOKEN"))
