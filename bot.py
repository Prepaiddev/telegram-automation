from telethon import TelegramClient, events
import re

# Replace with your details
api_id = 28276427  # Your API ID
api_hash = 'ce10c0651e18d453af7920b6785a87b4'  # Your API Hash
phone_number = '+2348132237695'  # Your phone number (including country code)

# Create the Telegram client
client = TelegramClient('session_name', api_id, api_hash)

# Function to remove links from messages
def remove_links(text):
    return re.sub(r'http[s]?://\S+', '', text)

# Event handler for new messages in AhmedFreeSignals
@client.on(events.NewMessage(chats='https://t.me/ahmedfreesignals'))
async def handler_ahmed(event):
    message = event.message.text
    
    # Remove any links from the message
    clean_message = remove_links(message)
    
    # Get the target channel (EtherauraCoin)
    target_channel = await client.get_entity('https://t.me/etherauracoin')
    
    # Forward the cleaned message to your channel
    await client.send_message(target_channel, clean_message)

# Event handler for new messages in TechCryptoAnalyst
@client.on(events.NewMessage(chats='https://t.me/TechCryptoAnalyst'))
async def handler_techcrypto(event):
    message = event.message.text
    
    # Remove any links from the message
    clean_message = remove_links(message)
    
    # Get the target channel (EtherauraCoin)
    target_channel = await client.get_entity('https://t.me/etherauracoin')
    
    # Forward the cleaned message to your channel
    await client.send_message(target_channel, clean_message)

# Start the client and run the event loop
async def main():
    await client.start(phone_number)
    print("Bot is running... Listening for new messages.")
    await client.run_until_disconnected()

# Run the bot
client.run_until_disconnected()
