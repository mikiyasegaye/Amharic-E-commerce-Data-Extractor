# ingestion/telegram_scraper.py

from telethon import TelegramClient
import csv
import os
from dotenv import load_dotenv

# Load env vars
load_dotenv('.env')
api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')
phone = os.getenv('phone')

client = TelegramClient('scraping_session', api_id, api_hash)

# Save media to this folder
media_dir = 'data/raw/photos'
os.makedirs(media_dir, exist_ok=True)

async def scrape_channel(client, channel_username, writer):
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

async def main():
    await client.start(phone=phone)
    with open('data/raw/telegram_data.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Channel Title', 'Channel Username', 'ID', 'Message', 'Date', 'Media Path'])

        # Read from Excel file with channels
        import pandas as pd
        df = pd.read_excel('ingestion/channels_to_crawl.xlsx')
        for channel in df['channel'].dropna():
            print(f"Scraping {channel}...")
            await scrape_channel(client, channel.strip(), writer)
            print(f"Done scraping {channel}")

with client:
    client.loop.run_until_complete(main())
