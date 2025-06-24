---
# EthioMart Amharic E-commerce NER System

A complete machine learning pipeline to extract structured information—like product names, prices, and locations—from Amharic e-commerce Telegram messages. This helps EthioMart assess vendors, track pricing, and identify business opportunities from unstructured chat data.
---

## 🚀 Project Goal

To build a full pipeline that:

- Collects Telegram posts from e-commerce channels
- Preprocesses Amharic text
- Labels key entities manually
- Trains and compares NER models
- Explains predictions (Model Interpretability)
- Scores vendors for micro-lending (FinTech use case)

---

## 🔧 Tools and Technologies

- Python 3.11+
- [Telethon](https://github.com/LonamiWebs/Telethon) for Telegram scraping
- Transformers (HuggingFace)
- pandas, numpy
- Jupyter Notebooks
- SHAP, LIME for interpretability
- scikit-learn for scoring
- tqdm, evaluate, datasets
- PyTorch with MPS for Apple Silicon

---

## 🗂️ Directory Structure

```bash
.
├── config/                          # YAML config files
├── data/
│   ├── raw/                         # Raw Telegram messages
│   └── processed/                   # Cleaned and labeled data (CoNLL format)
├── notebooks/                      # All development notebooks
│   ├── fine_tune_ner_model.ipynb   # Training NER model
│   ├── compare_models.ipynb        # Model benchmarking
│   ├── interpret_ner_model.ipynb   # SHAP & LIME explanation
│   ├── vendor_scorecard.ipynb      # Vendor analytics
│   └── exploration.ipynb           # Text cleaning demo
├── preprocessing/
│   ├── amharic_text_cleaner.py
│   └── preprocess_pipeline.py
├── src/
│   ├── data_ingestion/             # Scraper logic
│   ├── labeling/                   # CoNLL formatting
│   ├── modeling/                   # Training, evaluation helpers
│   └── vendor_analysis/           # Lending score logic
├── utils/                          # Reusable I/O, logging helpers
├── tests/                          # Unit tests
├── requirements.txt
└── README.md
```

---

## ✅ How to Run the Project

### 1. Install dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

> If using Apple M1/M2/M3: use `torch` with `mps` backend. It’s already handled in the code.

---

### 2. Scrape Telegram Posts

Configure target channels in `src/data_ingestion/channels_to_crawl.xlsx` and then:

```bash
python src/data_ingestion/telegram_scraper.py
```

This will save messages to `data/raw/telegram_data.csv`.

---

### 3. Preprocess the Text

```bash
python preprocessing/preprocess_pipeline.py
```

This will clean Amharic text and store it at `data/processed/telegram_data_cleaned.csv`.

---

### 4. Annotate for NER (Manually)

- Pick samples from `telegram_data_cleaned.csv`
- Annotate in CoNLL format with entity labels: `B-Product`, `I-Product`, `B-PRICE`, `B-LOC`, etc.
- Save as `data/processed/labeled_telegram_product_price_location.txt`

---

### 5. Fine-tune NER Model

Run:

```bash
jupyter notebook notebooks/train_ner_model.ipynb
```

It fine-tunes `xlm-roberta-base` or other multilingual models on your labeled data.

---

### 6. Compare Models

Run:

```bash
jupyter notebook notebooks/compare_models.ipynb
```

This compares `xlm-roberta-base`, `bert-base-amharic`, and `afroxlmr-base` on your data using precision, recall, and F1.

---

### 7. Interpret Predictions

Run:

```bash
jupyter notebook notebooks/interpret_ner_model.ipynb
```

This explains predictions using:

- SHAP for global interpretability
- LIME for local explanations

It helps understand how entity decisions are made and where the model fails.

---

### 8. Vendor Scorecard (Micro-Lending)

Run:

```bash
jupyter notebook notebooks/vendor_scorecard.ipynb
```

This analyzes Telegram metadata + NER output to:

- Measure post frequency
- Calculate average views and price
- Identify top-performing posts
- Assign a Lending Score per vendor

Final output is a table that can guide FinTech loan decisions.

---

## 📁 Key Files

| File                                          | Purpose                                    |
| --------------------------------------------- | ------------------------------------------ |
| `telegram_scraper.py`                         | Scrapes vendor posts                       |
| `preprocess_pipeline.py`                      | Cleans Amharic messages                    |
| `labeled_telegram_product_price_location.txt` | Manual annotations in CoNLL format         |
| `train_ner_model.ipynb`                       | Trains a transformer model                 |
| `compare_models.ipynb`                        | Benchmarks multiple NER models             |
| `interpret_ner_model.ipynb`                   | Explains NER predictions using SHAP + LIME |
| `vendor_scorecard.ipynb`                      | Scores vendors for loan eligibility        |

---

## 🧪 Testing

```bash
pytest tests/
```

Example:

```bash
pytest tests/test_preprocessing.py
```

---

## 🧠 Notes

- Designed for multilingual and low-resource settings (like Amharic)
- Uses modern transformers (XLM-R, AfroXLMR)
- Compatible with HuggingFace 🤗 ecosystem
- Supports vendor profiling for FinTech innovation

---

## 💡 Final Output

A production-ready system that:

- Scrapes raw Telegram data
- Cleans and labels text for NER
- Trains and explains a transformer model
- Ranks vendors by activity, reach, and pricing
- Outputs a FinTech-ready Vendor Scorecard

---
