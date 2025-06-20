import pandas as pd
from utils.logger import get_logger

logger = get_logger()

def save_cleaned_csv(df, output_path):
    """
    Save a DataFrame to CSV with UTF-8 encoding.
    Args:
        df (pd.DataFrame): DataFrame to save.
        output_path (str): Path to save the CSV file.
    """
    try:
        df.to_csv(output_path, index=False, encoding='utf-8')
        logger.info(f"Saved cleaned data to {output_path}")
    except Exception as e:
        logger.error(f"Failed to save CSV to {output_path}: {e}")
