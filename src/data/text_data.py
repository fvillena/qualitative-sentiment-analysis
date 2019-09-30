import json
import re
import spacy
nlp = spacy.load('es_core_news_sm')
def normalizer(text):
    """Receives a string, lowers the string, removes all the punctutation and 
    special characters and returns a normalized string."""
    text = text.lower() #string lowering
    text = re.sub(r'[^A-Za-zñáéíóú]', ' ', text) #replaces every punctuation with a space
    return text
def tokenizer(sentence):
    """Receives a string sentence, divides the sentence into words and returns a list of word tokens."""
    tokens = sentence.split(' ')
    tokens = [token for token in tokens if token != '']
    return tokens
class Preprocessor:
    def __init__(self, surveys_location):
        with open(surveys_location, 'r', encoding='utf-8') as f:
            self.surveys = json.load(f)
    def preprocess(self):
        self.surveys_tokenized = {}
        for survey,conversation in self.surveys.items():
            self.surveys_tokenized[survey] = []
            for dialog in conversation:
                subject = dialog[0]
                sentence = dialog[1]
                sentence_normalized = normalizer(sentence)
                doc = nlp(sentence_normalized)
                sentence_tokenized = [token.lemma_ for token in doc if ' ' not in token.lemma_]
                self.surveys_tokenized[survey].append((subject,sentence_tokenized))
    def write_surveys(self, surveys_destination):
        with open(surveys_destination, 'w', encoding='utf-8') as json_file:
            json.dump(self.surveys_tokenized, json_file, indent=2, ensure_ascii=False)
