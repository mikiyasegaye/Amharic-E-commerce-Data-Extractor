import pandas as pd
import re
import os
from preprocessing.amharic_text_cleaner import clean_amharic_text
from utils.io_helpers import save_cleaned_csv

def preprocess_telegram_data(input_path, output_path):
    df = pd.read_excel(input_path)
    
    if 'Message' not in df.columns:
        raise ValueError("Expected a 'Message' column in the input file.")

    df['Cleaned_Message'] = df['Message'].astype(str).apply(clean_amharic_text)
    
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"[✓] Cleaned data saved to {output_path}")
