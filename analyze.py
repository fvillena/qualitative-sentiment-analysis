from src.data.survey_data import SurveysLoader
from src.data.text_data import Preprocessor
from src.analysis.sentiment import SentimentAnalyzer
loader = SurveysLoader('data/raw/')
loader.write_surveys('data/interim/surveys.json')
preprocessor = Preprocessor('data/interim/surveys.json')
preprocessor.preprocess()
preprocessor.write_surveys('data/interim/surveys_preprocessed.json')
analyzer = SentimentAnalyzer('data/interim/surveys.json','data/interim/surveys_preprocessed.json','data/external/Ratings_Warriner_et_al_Spanish.csv')
analyzer.analyze()
analyzer.write_result('results/surveys_analyzed.csv')