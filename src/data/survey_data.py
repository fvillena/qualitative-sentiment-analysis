import os
import re
import json
class SurveysLoader:
    def __init__(self, surveys_location):
        self.surveys = {}
        for filename in os.listdir(surveys_location):
            self.surveys[filename] = []
            with open (surveys_location + filename, encoding='utf-8') as f:
                for line in f:
                    m = re.search(r'^(\w): (.*)$', line.rstrip().lower())
                    subject = m.group(1)
                    sentence = m.group(2)
                    self.surveys[filename].append((subject,sentence))
    def write_surveys(self, surveys_destination):
        with open(surveys_destination, 'w', encoding='utf-8') as json_file:
            json.dump(self.surveys, json_file, indent=2, ensure_ascii=False)
