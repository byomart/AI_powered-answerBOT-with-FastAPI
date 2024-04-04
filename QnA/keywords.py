from rake_nltk import Rake
import logging

class Keywords:
    def __init__(self):
        self.r = Rake()

    def extract_keywords(self, query):

        self.r.extract_keywords_from_text(query)                        # Extraction given the text.
        # r.extract_keywords_from_sentences(<list of sentences>)        # Extraction given the list of strings where each string is a sentence.
        keywords = self.r.get_ranked_phrases()                          # To get keyword phrases ranked highest to lowest.

        logging.info(f' Query: {query}')
        logging.info(f' Extracted Keywords: {keywords}')

        return keywords