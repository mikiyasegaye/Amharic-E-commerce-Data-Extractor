import re

def clean_amharic_text(text):
    text = text.strip()

    # Remove links, hashtags, mentions
    text = re.sub(r"http\S+|www\S+|@\w+|#\w+", "", text)
    
    # Remove emojis and non-Amharic non-punctuation characters
    text = re.sub(r"[^\u1200-\u137F፡።፣፤፥፦፧0-9a-zA-Z.,!?()\[\]{} \n]", "", text)

    # Normalize space
    text = re.sub(r"\s+", " ", text)

    return text
