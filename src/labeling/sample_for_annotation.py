import pandas as pd
import random
from pathlib import Path

def main():
    # Define paths
    cleaned_csv_path = Path("data/processed/telegram_data_cleaned.csv")
    output_txt_path = Path("data/labeled/sample_for_annotation.txt")

    # Load cleaned data
    df = pd.read_csv(cleaned_csv_path)
    messages = df["cleaned_message"].dropna().tolist()

    # Sample 40 messages (change as needed)
    sample_size = min(40, len(messages))
    sampled_messages = random.sample(messages, sample_size)

    # Write to txt in a line-by-line token format for CoNLL annotation
    with open(output_txt_path, "w", encoding="utf-8") as f:
        for message in sampled_messages:
            tokens = message.strip().split()
            for token in tokens:
                f.write(f"{token}\tO\n")  # Default to "O", to be replaced manually
            f.write("\n")  # Sentence separator

    print(f"✅ Sampled {sample_size} messages for annotation.")
    print(f"📄 Output saved to: {output_txt_path}")

if __name__ == "__main__":
    main()
