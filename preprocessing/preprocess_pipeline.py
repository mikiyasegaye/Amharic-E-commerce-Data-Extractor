import pandas as pd
import re
import os
from preprocessing.amharic_text_cleaner import clean_amharic_text
from utils.io_helpers import save_cleaned_csv
from utils.logger import get_logger

logger = get_logger()

def preprocess_telegram_data(input_path, output_path):
    """
    Preprocess Telegram data by cleaning Amharic messages and saving the result.
    Args:
        input_path (str): Path to the input Excel file.
        output_path (str): Path to save the cleaned CSV file.
    """
    df = pd.read_excel(input_path)
    
    if 'Message' not in df.columns:
        logger.error("Expected a 'Message' column in the input file.")
        raise ValueError("Expected a 'Message' column in the input file.")

    df['Cleaned_Message'] = df['Message'].astype(str).apply(clean_amharic_text)
    
    save_cleaned_csv(df, output_path)
    logger.info(f"[✓] Cleaned data saved to {output_path}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Preprocess Telegram data for NER.")
    parser.add_argument('--input', required=True, help='Path to input Excel file')
    parser.add_argument('--output', required=True, help='Path to output CSV file')
    args = parser.parse_args()
    preprocess_telegram_data(args.input, args.output)
