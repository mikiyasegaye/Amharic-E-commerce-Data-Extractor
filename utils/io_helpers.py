import pandas as pd

def save_cleaned_csv(df, output_path):
    df.to_csv(output_path, index=False, encoding='utf-8')
