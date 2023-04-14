# Streamlabs to Discord Integration
This Python code provides an integration between Streamlabs and Discord, allowing you to send donation messages from Streamlabs to a Discord channel of your choice.

### Getting Started
1. Clone this repository to your local machine.
2. Install the required packages: pip install requests websocket-client discord.py
3. Replace the streamlabsSocketToken, discordToken, and channelID variables with your own Streamlabs socket API key, Discord bot token, and Discord channel ID, respectively.
4. Run the script with the command: python dc.py

### How it Works
The code uses the Streamlabs API to establish a WebSocket connection and listen for incoming donation events. When a donation event occurs, the event data is parsed and the donation message is sent to the specified Discord channel using the Discord API.

### Troubleshooting

If you receive an error message indicating that the loop attribute cannot be accessed in non-async contexts, try running the script with python -m asyncio dc.py instead.
If the script is not running continuously, make sure that your Discord bot is still online and that your WebSocket connection has not been closed.
