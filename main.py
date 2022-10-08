# -*- coding: utf-8 -*-
import json, os, discord, time, datetime
from discord.commands import SlashCommand, ApplicationContext, Option

from discord.ext import commands

with open("./config.json", "r", encoding="utf-8") as config: config = json.loads(config.read())
if not os.path.exists("./templates"): os.mkdir("./templates")


bot = discord.Bot(intents=discord.Intents.all())

class Greetings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def sobesedovanie(self, ctx:discord.ApplicationContext, sobes_user: discord.User, days: int = 7):
        
        
        dosieebmed=discord.Embed(title="Досье на опрашиваемого", url=f"https://discord-tracker.ru/tracker/user/{sobes_user.id}/", color=0xffffff)
        dosieebmed.set_author(name=ctx.author.display_name, url=f"https://discord-tracker.ru/tracker/user/{ctx.author.id}/", icon_url=ctx.author.display_avatar.url)
        dosieebmed.set_thumbnail(url=sobes_user.display_avatar.url)
        dosieebmed.add_field(name="Первый шаг", value=f"Знакомимся с собеседником", inline=False)
        dosieebmed.add_field(name="Второй шаг", value=f"[Проверяем дискорд трекер](https://discord-tracker.ru/tracker/user/{sobes_user.id}/)", inline=False)
        dosieebmed.set_footer(text="Если всё окей, то жмём зелёную:)")
        
        ts = datetime.datetime.now() + datetime.timedelta(days=days)
        
        lists_id = [504665587956318218, 821428282464665641, 393829114152353793, 931928150382878721, 640797508649615380]
        otchetiebmed=discord.Embed(title="Отчёты")
        otchetiebmed.add_field(name="Отчёт", value=f"```\n<@{sobes_user.id}> <– Взят на испытательный срок на неделю до <t:{int(ts.timestamp())}:d>\n" +", ".join([f"<@{x}>" for x in lists_id])+ "\n```", inline=False)
        otchetiebmed.add_field(name="Пригласить на сервер печенек", value=f"`https://discord.gg/RPNeP3TYSf`", inline=False)
        otchetiebmed.add_field(name="Написать о добавлении нового ивентёра", value=f"```\n♥ <@&877302308667551794>, приветствуйте новичка (<@{sobes_user.id}>) в вашей семье! ♥\n♥ Обязательно подружитесь с ним! ♥\n```")
        
        messageembed=discord.Embed(title="Личные сообщения")
        messageembed.add_field(name="Линк", value=f"<@{sobes_user.id}>")
        messageembed.add_field(name="Приглашение на набор", value="```:tada:**Приветик солнышко**:tada:\n\nВам пишет Мастер EventsMod, сервера **XIVIVIDE**\nВы оставили заявку, которую одобрили!\nНе желаете пройти собеседование, на котором мы поговорим и порассуждаем планы вашего вступления к нам?\nP.S. Напишите, когда вам будет удобнее всего пройти собес. Целую\n\nМой ID: 640797508649615380```")
        
        await ctx.respond(embeds=[dosieebmed, otchetiebmed, messageembed])

    @discord.slash_command()
    async def sobesedovanie_close(self, ctx:discord.ApplicationContext, sobes_user: discord.User, days: int = 7):
        
        
        dosieebmed=discord.Embed(title="Досье на опрашиваемого", url=f"https://discord-tracker.ru/tracker/user/{sobes_user.id}/", color=0xffffff)
        dosieebmed.set_author(name=ctx.author.display_name, url=f"https://discord-tracker.ru/tracker/user/{ctx.author.id}/", icon_url=ctx.author.display_avatar.url)
        dosieebmed.set_thumbnail(url=sobes_user.display_avatar.url)
        dosieebmed.add_field(name="Первый шаг", value=f"Знакомимся с собеседником", inline=False)
        dosieebmed.add_field(name="Второй шаг", value=f"[Проверяем дискорд трекер](https://discord-tracker.ru/tracker/user/{sobes_user.id}/)", inline=False)
        dosieebmed.set_footer(text="Если всё окей, то жмём зелёную:)")
        
        ts = datetime.datetime.now() + datetime.timedelta(days=days)
        
        lists_id = [295127995725643778, 640797508649615380]
        otchetiebmed=discord.Embed(title="Отчёты")
        otchetiebmed.add_field(name="Отчёт", value=f"```\n<@{sobes_user.id}> <– Взят на ИС клозера на неделю до <t:{int(ts.timestamp())}:d>\n" +", ".join([f"<@{x}>" for x in lists_id])+ "\n```", inline=False)
        otchetiebmed.add_field(name="Пригласить на сервер печенек", value=f"`https://discord.gg/RPNeP3TYSf`", inline=False)
        otchetiebmed.add_field(name="Написать о добавлении нового ивентёра", value=f"```\n♥ <@&877302308667551794>, приветствуйте новичка (<@{sobes_user.id}>) в вашей семье! ♥\n♥ Обязательно подружитесь с ним! ♥\n```")
        
        messageembed=discord.Embed(title="Личные сообщения")
        messageembed.add_field(name="Линк", value=f"<@{sobes_user.id}>")
        messageembed.add_field(name="Приглашение на набор", value="```:tada:**Приветик солнышко**:tada:\n\nВам пишет Мастер EventsMod, сервера **XIVIVIDE**\nВы оставили заявку, которую одобрили!\nНе желаете пройти собеседование, на котором мы поговорим и порассуждаем планы вашего вступления к нам?\nP.S. Напишите, когда вам будет удобнее всего пройти собес. Целую\n\nМой ID: 640797508649615380```")
        
        await ctx.respond(embeds=[dosieebmed, otchetiebmed, messageembed])


   #@discord.slash_command()
   #async def sobranie(self, ctx:discord.ApplicationCommand, ts: int):
   #    Ивентёры, напоминаем, что у нас состоится собрание (<#995737870633541652>) <t:1660489200:R>
   #    Точное время: <t:1660489200:F>
   #    Явка обязательна для всех.
   #    Если есть уважительная причина отсутствовать – сообщите **куратору** или **мастеру**
                
                
                
        
        



bot.add_cog(Greetings(bot)) # add the cog to the bot

bot.run(config["d_token"])