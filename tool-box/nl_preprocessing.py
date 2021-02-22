import string
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer

def clean_text(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    text_lower = text.lower()
    text_no_nums = ''.join(word for word in text if not word.isdigit())
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(word) for word in text_no_nums]
    return ' '.join(lemmatized)
