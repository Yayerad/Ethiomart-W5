from telethon import TelegramClient
import pandas as pd
from nltk.tokenize import word_tokenize
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

# Define the output directory
output_dir = os.path.join(os.getcwd(), 'src', 'data')  # Target src/data folder

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

async def scrape_channel():
    """Scrape messages from the Telegram channel."""
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

async def main():
    """Main function to scrape and process data."""
    # Scrape messages
    messages = await scrape_channel()
    df = pd.DataFrame(messages)

    # Save raw data to the specified folder
    raw_data_path = os.path.join(output_dir, 'telegram_messages_raw.csv')
    df.to_csv(raw_data_path, index=False)
    print(f"Scraped {len(df)} messages and saved to '{raw_data_path}'.")

    # Preprocess messages
    def preprocess_text(text):
        """Basic text preprocessing."""
        tokens = word_tokenize(text)  # Tokenize the message
        tokens = [token.lower() for token in tokens]  # Normalize to lowercase
        tokens = [token for token in tokens if token.isalnum()]  # Remove non-alphanumeric tokens
        return ' '.join(tokens)

    # Apply preprocessing
    df['cleaned_content'] = df['content'].apply(preprocess_text)

    # Save preprocessed data to the specified folder
    preprocessed_data_path = os.path.join(output_dir, 'telegram_messages_preprocessed.csv')
    df.to_csv(preprocessed_data_path, index=False)
    print(f"Preprocessed data saved to '{preprocessed_data_path}'.")

    # Disconnect the client after completing the task
    await client.disconnect()
    print("Client disconnected.")

# Ensure proper event loop handling for script execution
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError as e:
        if "asyncio.run()" in str(e):
            # Handle case where an event loop is already running
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main())
