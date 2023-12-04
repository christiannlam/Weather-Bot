import os
import discord
import responses

#Bot sends message to user in channel
async def send_message(message, userMsg):
  try:
    response = responses.handle_response(userMsg)
    await message.channel.send(response)
  except Exception as E:
    print(E)

def run_bot():
  #Uses Bot Token from ENV
  TOKEN = os.environ['Discord_Key']
  #Creating the Bot
  client = discord.Client(intents = discord.Intents().all())

  #Confirms that Bot is Active
  @client.event
  async def on_ready():
    print(f'{client.user} is running')

  #Bot reads user message
  @client.event
  async def on_message(message):
    user = str(message.author)
    userMsg = str(message.content)
    channel = str(message.channel)
    if userMsg[0] == '!':
      userMsg = userMsg[1:]
      await send_message(message,userMsg)
      
  client.run(TOKEN)