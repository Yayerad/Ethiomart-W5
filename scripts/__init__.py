from telethon import TelegramClient
import pandas as pd
from dotenv import load_dotenv
import os
import asyncio

# Load environment variables from .env file
load_dotenv()

# Retrieve API credentials from environment variables
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
CHANNEL_URL = 'https://t.me/sinayelj'

# Initialize the Telegram client
client = TelegramClient('scraper_session', API_ID, API_HASH)

# Function to scrape messages
async def scrape_channel():
    messages = []
    async with client:
        async for message in client.iter_messages(CHANNEL_URL, limit=500):  # Adjust the limit as needed
            if message.text:
                messages.append({
                    'id': message.id,
                    'date': message.date,
                    'sender': message.sender_id,
                    'content': message.text
                })
    return messages

# Main function to execute the script
async def main():
    # Start scraping messages
    scraped_messages = await scrape_channel()
    
    # Convert messages to a DataFrame
    df = pd.DataFrame(scraped_messages)
    
    # Save the DataFrame to a CSV file
    df.to_csv('telegram_messages.csv', index=False)
    print(f"Scraped {len(df)} messages and saved to 'telegram_messages.csv'.")

# Run the script
if __name__ == "__main__":
    asyncio.run(main())