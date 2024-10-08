from nltk.tokenize import sent_tokenize

def summarize_text(text):
    sentences = sent_tokenize(text)
    if len(sentences) > 5:  # Just a simple way to summarize
        return ' '.join(sentences[:5]) + '...'  # Summarizes to first 5 sentences
    return text  # If text is short, return it as is
