from bs4 import BeautifulSoup
import requests
import discord
from discord.ext import commands

intents = discord.Intents().all()
client = commands.Bot(command_prefix='.', intents=intents)

@client.event
async def on_ready():
    print("ready")

@client.command()
async def cases(ctx, *, country):
    if(country == "world"):
        r = requests.get('https://www.worldometers.info/coronavirus/#countries')
        soup = BeautifulSoup(r.text, 'html.parser')
        statistics = soup.find_all(class_ = "maincounter-number")
        total_cases = statistics[0].text
        total_deaths = statistics[1].text
        embed = discord.Embed(
            title = "Total World Cases & Deaths",
            color = discord.Color.red(),
        )
        embed.set_thumbnail(url='https://static01.nyt.com/images/2020/03/26/science/26VIRUS-TRANSMISSION/26VIRUS-TRANSMISSION-superJumbo.jpg')
        embed.add_field(name="**Total Cases**", value=total_cases, inline=True)
        embed.add_field(name="**Total Deaths**", value=total_deaths, inline=True)
        embed.set_footer(text="Developed by Shaan")
        await ctx.send(embed=embed)
    elif(country == "USA" or country == "US" or country == "usa"):
        r = requests.get('https://www.worldometers.info/coronavirus/country/us/')
        soup = BeautifulSoup(r.text, 'html.parser')
        statistics = soup.find_all(class_ = "maincounter-number")
        total_cases = statistics[0].text
        total_deaths = statistics[1].text
        embed = discord.Embed(
            title = "United States Cases & Deaths",
            color = discord.Color.red(),
        )
        embed.set_thumbnail(url='https://static01.nyt.com/images/2020/03/26/science/26VIRUS-TRANSMISSION/26VIRUS-TRANSMISSION-superJumbo.jpg')
        embed.add_field(name="**Total Cases**", value=total_cases, inline=True)
        embed.add_field(name="**Total Deaths**", value=total_deaths, inline=True)
        embed.set_footer(text="Developed by Shaan")
        await ctx.send(embed=embed)
    else:
        r = requests.get('https://www.worldometers.info/coronavirus/country/'+country +'/')
        soup = BeautifulSoup(r.text, 'html.parser')
        statistics = soup.find_all(class_ = "maincounter-number")
        total_cases = statistics[0].text
        total_deaths = statistics[1].text
        embed = discord.Embed(
            title = country + " Cases & Deaths",
            color = discord.Color.red(),
        )
        embed.set_thumbnail(url='https://static01.nyt.com/images/2020/03/26/science/26VIRUS-TRANSMISSION/26VIRUS-TRANSMISSION-superJumbo.jpg')
        embed.add_field(name="**Total Cases**", value=total_cases, inline=True)
        embed.add_field(name="**Total Deaths**", value=total_deaths, inline=True)
        embed.set_footer(text="Developed by Shaan")
        await ctx.send(embed=embed)

client.run('MTEzNDUwNDI0MTQ4Mjk3MzMwNw.GPl-No.VaoFCkmEXyBQ332kC77JXteyXPQGH2rKWDLqYA')



