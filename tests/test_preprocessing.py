import pytest
from preprocessing.amharic_text_cleaner import clean_amharic_text

def test_clean_amharic_text_removes_links():
    text = "ምሳሌ http://example.com"
    assert "http" not in clean_amharic_text(text)

def test_clean_amharic_text_removes_emojis():
    text = "ምሳሌ 😊"
    assert "😊" not in clean_amharic_text(text)

def test_clean_amharic_text_normalizes_space():
    text = "ምሳሌ    ልጅ"
    cleaned = clean_amharic_text(text)
    assert "  " not in cleaned
    assert cleaned.strip() == cleaned 