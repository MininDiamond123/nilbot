import discord
import random
import gui

bot = commands.Bot(command_prefix = "ch.", description = "This is a customized bot for The Clubhouse! If you have any suggestions, please tag a Bot Developer.", owner_id = 389472478545575937)

bot.run(os.environ.get("TOKEN"))
