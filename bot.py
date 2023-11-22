import discord
import responses
from discord.ext import tasks
import asyncio 

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTE3NjYxNDI0NzUxMDMxMDkyMg.G6hoXg.CZd_F3ujFb4c8_SbXjvfMCY7wx2-6Qz-OWLLi4'
    intents = discord.Intents().all()
    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        vc = client.get_channel(1176634041835982989)
        try:
            player = await vc.connect()
            #player = vc.create_ffmpeg_player("shisha.mp3", after=lambda: print("Spiele sound ab"))
            #player.star
            while True:
                player.play(discord.FFmpegPCMAudio("shisha.mp3"), after=lambda e: print("noch eine Runde"))
                await asyncio.sleep(283)
        except Exception as e:
            print(e)

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
