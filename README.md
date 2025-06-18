# EthioMart Amharic E-commerce NER System

A machine learning pipeline to extract structured information (product names, prices, and locations) from Amharic-language e-commerce messages collected from Telegram. This project supports EthioMart’s mission to centralize fragmented online commerce in Ethiopia.

---

## Task 1: Data Ingestion and Preprocessing

### Task Overview

This task involves building a pipeline for ingesting and preprocessing Amharic-language messages collected from Ethiopian e-commerce Telegram channels. The goal is to prepare clean, structured data for Named Entity Recognition (NER) model training.

### Business Context

EthioMart aims to centralize fragmented Telegram-based e-commerce activities in Ethiopia. To achieve this, messages from various Telegram vendors are aggregated, and key entities (e.g., product names, prices, and locations) are extracted using machine learning.

---

## Task Objectives

1. Identify and connect to relevant Telegram channels using a custom scraping script.
2. Ingest message data (text and media) from these channels in real time.
3. Preprocess Amharic messages by cleaning, normalizing, and tokenizing the text.
4. Separate metadata (e.g., sender, timestamp) from message content.
5. Save the cleaned, structured data in a format ready for annotation and modeling.

---

## Tools and Technologies Used

- Python 3.11+
- Telethon for Telegram message scraping
- pandas for data manipulation
- python-dotenv for secure environment variable management
- Regular expressions for Amharic text cleaning
- Jupyter Notebook for interactive data exploration

---

## Directory Structure

```

ethiomart-amharic-ner/
├── data/
│   ├── raw/                        # Raw Telegram messages and media
│   ├── processed/                  # Cleaned message data for modeling
│   └── samples/                    # Small data subsets for testing
│
├── ingestion/
│   ├── telegram\_scraper.py         # Telegram scraping script using Telethon
│   ├── config.yaml                 # Channel list and metadata
│   └── channels\_to\_crawl.xlsx     # Telegram channel links
│
├── preprocessing/
│   ├── amharic\_text\_cleaner.py     # Cleaning/tokenizing logic
│   └── preprocess\_pipeline.py      # Pipeline to clean and save messages
│
├── notebooks/
│   └── exploration.ipynb           # Interactive cleaning preview
│
├── utils/
│   ├── io\_helpers.py               # File I/O functions
│   └── logger.py                   # Custom logging (optional)
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

```

---

## What Was Done

1. Created a structured project repository with clearly separated folders for ingestion, preprocessing, and utilities.
2. Implemented a Telegram scraping script that collects messages and media into a local CSV and image archive.
3. Wrote a cleaning function tailored to Amharic, removing emojis, URLs, mentions, and unwanted punctuation.
4. Created a preprocessing pipeline that processes raw messages and stores the result in `cleaned_telegram_data.csv`.
5. Verified and visualized message cleaning logic using an interactive Jupyter notebook.

---

## Output

- `data/raw/telegram_data.xlsx` – Raw messages collected from Telegram
- `data/processed/cleaned_telegram_data.csv` – Preprocessed messages ready for labeling

---
