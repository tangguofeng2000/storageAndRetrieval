from nltk.stem import PorterStemmer

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.

# Please add comments along with your code.
class WordNormalizer:

    def __init__(self):
        return

    def lowercase(self, word):
        # Transform the word uppercase characters into lowercase.
        return word.lower()

    def stem(self, word):
        # Return the stemmed word with PorterStemmer imported previously.
        porter_stem = PorterStemmer()
        return porter_stem.stem(word)
