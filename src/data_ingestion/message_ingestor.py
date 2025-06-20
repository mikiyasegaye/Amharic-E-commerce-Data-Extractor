import os
import re
import pandas as pd
from datetime import datetime


def get_logger():
    import logging
    logger = logging.getLogger("Ingestor")
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('[%(levelname)s] %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger

logger = get_logger()

def clean_text(text):
    if not isinstance(text, str):
        return ""

    # Remove emojis and symbols
    text = re.sub(r'[^\w\s፡።፣፤ሀ-ፐ]', '', text)

    # Remove repeated punctuation
    text = re.sub(r'([።፣፤፡])\1+', r'\1', text)

    # Normalize spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text

class MessageIngestor:
    def __init__(self, raw_path, cleaned_output_path):
        self.raw_path = raw_path
        self.cleaned_output_path = cleaned_output_path

    def load_data(self):
        if not os.path.exists(self.raw_path):
            raise FileNotFoundError(f"File not found: {self.raw_path}")
        df = pd.read_csv(self.raw_path)
        logger.info(f"Loaded {len(df)} messages.")
        return df

    def clean_messages(self, df):
        df = df.dropna(subset=['Message'])  # Remove empty messages
        df['Cleaned_Message'] = df['Message'].apply(clean_text)
        return df

    def save_data(self, df):
        os.makedirs(os.path.dirname(self.cleaned_output_path), exist_ok=True)
        df.to_csv(self.cleaned_output_path, index=False, encoding='utf-8')
        logger.info(f"Saved cleaned messages to {self.cleaned_output_path}")

    def run(self):
        logger.info("Starting message ingestion pipeline...")
        df = self.load_data()
        df_cleaned = self.clean_messages(df)
        self.save_data(df_cleaned)
        logger.info("Ingestion complete.")

if __name__ == "__main__":
    ingestor = MessageIngestor(
        raw_path='data/raw/telegram_data.csv',
        cleaned_output_path='data/processed/cleaned_telegram_data.csv'
    )
    ingestor.run()
