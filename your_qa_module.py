import re
from nltk.tokenize import sent_tokenize

def search_answer(text, question):
    sentences = sent_tokenize(text)
    question = question.lower()
    keywords = re.findall(r'\b\w+\b', question)

    best_sentence = None
    best_match_count = 0

    for sentence in sentences:
        sentence_lower = sentence.lower()
        match_count = sum(1 for keyword in keywords if keyword in sentence_lower)

        if match_count > best_match_count:
            best_match_count = match_count
            best_sentence = sentence

    return best_sentence if best_sentence else "I couldn't find an answer. Please try rephrasing your question or upload another file."
