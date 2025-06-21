import pandas as pd
import re
from pathlib import Path
import sys

def clean_amharic_text(text):
    if not isinstance(text, str):
        return ""
    text = re.sub(r"[^\u1200-\u137F\s]", " ", text)  # Keep only Amharic + whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text

def main():
    raw_path = Path("data/raw/telegram_data.csv")
    cleaned_path = Path("data/processed/telegram_data_cleaned.csv")

    print(f"📥 Loading data from {raw_path}")
    df = pd.read_csv(raw_path)
    print("📊 Available columns:", df.columns.tolist())

    message_col = "Message"  # Now matching your actual column name

    if message_col not in df.columns:
        print(f"❌ Error: '{message_col}' column not found in the CSV.")
        sys.exit(1)

    df.dropna(subset=[message_col], inplace=True)
    print(f"✅ Loaded {len(df)} rows with non-empty messages")

    print("🧹 Cleaning text...")
    df["cleaned_message"] = df[message_col].apply(clean_amharic_text)

    print(f"💾 Saving cleaned data to {cleaned_path}")
    cleaned_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(cleaned_path, index=False)

    print("✅ Done.")

if __name__ == "__main__":
    main()
