from mcp.server.fastmcp import FastMCP
import discord
import asyncio
import threading

# -------------------------
# CONFIGURATION
# -------------------------
TOKEN = "YOUR-TOKEN"
GUILD_ID = YOUR-GUILD-ID  # must be int
CHANNEL_ID = YOUR-CHANNEL-ID  # must be int

# -------------------------
# MCP SERVER SETUP
# -------------------------
mcp = FastMCP("Discord MCP Server")

# -------------------------
# DISCORD BOT SETUP
# -------------------------
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

bot_ready = threading.Event()  # Flag to indicate bot is ready

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    bot_ready.set()  # <-- THIS marks the bot as ready


@mcp.tool()
def write_message(message: str) -> str:
    """
    Sends a message to the configured Discord channel.
    """
    if not bot_ready.is_set():
        return "Bot not ready yet. Try again in a moment."

    async def send():
        channel = bot.get_channel(CHANNEL_ID)
        if not channel:
            return f"Channel {CHANNEL_ID} not found."
        await channel.send(message)
        return f"Message sent to channel {CHANNEL_ID}"

    future = asyncio.run_coroutine_threadsafe(send(), bot.loop)
    return future.result()

# -------------------------
# DISCORD BOT EVENTS
# -------------------------
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    bot_ready.set()  # Signal that the bot is ready

# -------------------------
# RUN DISCORD BOT IN THREAD
# -------------------------
def run_bot():
    bot.run(TOKEN)

threading.Thread(target=run_bot, daemon=True).start()

# -------------------------
# START MCP SERVER
# -------------------------
if __name__ == "__main__":
    mcp.run(transport="stdio")

