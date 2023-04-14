import requests
import websocket
import json
import discord
import asyncio
import threading

streamlabsSocketToken = "Your-Streamlabs-socket-api-key"

discordToken = "<Your-discord-bot-token>"

channelID = "<Discord channel id you wanted to send donations as an integer>"


intents = discord.Intents.all()
client = discord.Client(intents=intents)


def on_message(ws, message):
    if "42" in message:
        data = json.loads(message[2:])
        if data[0] == "event":
            event_data = data[1]
            if event_data["type"] == "donation":
                name = event_data["message"][0]["from"]
                message = event_data["message"][0]["message"]
                
                asyncio.run_coroutine_threadsafe(
                    send_donation_to_discord(name, message), client.loop)


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


def on_open(ws):
    print("### open ###")
    data = {
        "type": "STREAMLABS:CONNECTED",
        "data": {
            "api_token": streamlabsSocketToken
        }
    }
    ws.send(json.dumps(data))


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


def start_discord_bot():
    client.run(discordToken)


def start_websocket():
    ws.keep_running = True
    while True:
        ws.run_forever()


async def send_donation_to_discord(name, message):
    # Your channel ID as an integer
    channel = client.get_channel(channelID)
    discord_message = f"{name} kişisinden {message} adlı donate"
    await channel.send(discord_message)

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(f"wss://sockets.streamlabs.com/socket.io/?token={streamlabsSocketToken}&EIO=3&transport=websocket",
                                on_message=on_message,
                                on_error=on_error)

    discord_thread = threading.Thread(target=start_discord_bot)
    websocket_thread = threading.Thread(target=start_websocket)

    discord_thread.start()
    websocket_thread.start()

    discord_thread.join()
    websocket_thread.join()
