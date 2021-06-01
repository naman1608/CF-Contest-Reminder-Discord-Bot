from datetime import datetime
from datetime import date
from time import sleep
import discord
import requests

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client:
        return

    if(message.content.startswith('$Reminder')):
        today = date.today()
        print(today)
        r = requests.get('https://codeforces.com/api/contest.list?gym=false')
        r_json = r.json()
        while True:
            contestTime = date.today()
            flag = False
            for contest in r_json['result']:
                contestDate = datetime.fromtimestamp(
                    contest['startTimeSeconds']).strftime("%Y-%m-%d")
                # print(contestDate)
                if today == contestDate:
                    flag = True
                    contestTime = datetime
            if flag == False:
                await message.channel.send('No contest today')
            else:
                await message.channel.send('There is a contest today')
            sleep(86400)


client.run(sys.argv[1])
#:D:D
