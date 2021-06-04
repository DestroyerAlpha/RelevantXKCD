from rake_nltk import Rake

def get_keywords(input_string):
    r = Rake()
    r.extract_keywords_from_sentences(input_string)
    return r.get_ranked_phrases()