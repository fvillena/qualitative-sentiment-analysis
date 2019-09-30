from src.data.survey_data import SurveysLoader
from src.data.text_data import Preprocessor
loader = SurveysLoader('data/raw/')
loader.write_surveys('data/interim/surveys.json')
preprocessor = Preprocessor('data/interim/surveys.json')
preprocessor.preprocess()
preprocessor.write_surveys('data/interim/surveys_preprocessed.json')

