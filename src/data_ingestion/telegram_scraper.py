import os
import sys
import csv
import argparse
import asyncio
from dotenv import load_dotenv

# Fix import path to allow 'utils' usage when running directly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from telethon import TelegramClient
from utils.logger import get_logger
import pandas as pd

logger = get_logger()

# Load environment variables
def load_env_vars(env_path='.env'):
    load_dotenv(env_path)
    api_id = os.getenv('TG_API_ID')
    api_hash = os.getenv('TG_API_HASH')
    phone = os.getenv('phone')
    return api_id, api_hash, phone

api_id, api_hash, phone = load_env_vars()
client = TelegramClient('scraping_session', api_id, api_hash)

# Folder to save media
media_dir = 'data/raw/photos'
os.makedirs(media_dir, exist_ok=True)

async def scrape_channel(client, channel_username, writer):
    """
    Scrape messages and media from a Telegram channel.
    """
    try:
        entity = await client.get_entity(channel_username)
        channel_title = entity.title

        async for message in client.iter_messages(entity, limit=1000):
            media_path = None
            if message.media and hasattr(message.media, 'photo'):
                filename = f"{channel_username}_{message.id}.jpg"
                media_path = os.path.join(media_dir, filename)
                await client.download_media(message.media, media_path)

            writer.writerow([
                channel_title,
                channel_username,
                message.id,
                message.message,
                message.date,
                media_path
            ])
    except Exception as e:
        logger.error(f"Error scraping {channel_username}: {e}")

async def main(channels_path, output_path, num_channels=None):
    """
    Main scraping routine.
    """
    await client.start(phone=phone)

    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Channel Title', 'Channel Username', 'ID', 'Message', 'Date', 'Media Path'])

        df = pd.read_excel(channels_path)
        channels = df['channel'].dropna()

        if num_channels is not None:
            channels = channels.head(num_channels)

        for channel in channels:
            channel = channel.strip()
            logger.info(f"Scraping {channel}...")
            await scrape_channel(client, channel, writer)
            logger.info(f"Finished scraping {channel}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape Telegram channels for e-commerce messages.")
    parser.add_argument('--channels', required=True, help='Path to Excel file with channel list')
    parser.add_argument('--output', required=True, help='Path to output CSV file')
    parser.add_argument('--num-channels', type=int, default=None, help='Number of channels to scrape (default: all)')
    args = parser.parse_args()

    with client:
        client.loop.run_until_complete(main(args.channels, args.output, args.num_channels))
