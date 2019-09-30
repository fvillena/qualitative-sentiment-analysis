import json
import csv
import statistics
class SentimentAnalyzer:
    def __init__(self,surveys_raw,surveys_preprocessed,sentiment_lexicon):
        with open(surveys_raw, 'r', encoding='utf-8') as f:
            self.surveys_raw = json.load(f)
        with open(surveys_preprocessed, 'r', encoding='utf-8') as f:
            self.surveys_preprocessed = json.load(f)
        self.sentiment_lexicon = {}
        with open(sentiment_lexicon, 'r', encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                word = row['Palabra']
                valence = row['V.Mean.Sum']
                self.sentiment_lexicon[word] = valence
    def analyze(self):
        self.surveys_analized = []
        for survey,conversation in self.surveys_preprocessed.items():
            for i,dialog in enumerate(conversation):
                subject = dialog[0]
                sentence_tokenized = dialog[1]
                valences = []
                for word in sentence_tokenized:
                    try:
                        value = self.sentiment_lexicon[word]
                        valences.append(float(value))
                    except KeyError:
                        pass
                try:
                    mean_valence = statistics.mean(valences)
                except:
                    mean_valence = None
                sentence_raw = self.surveys_raw[survey][i][1]
                self.surveys_analized.append((survey,subject,sentence_raw,mean_valence))
    def write_result(self,result_location):
        with open(result_location, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['survey','subject','sentence','valence'])
            for row in self.surveys_analized:
                writer.writerow(row)