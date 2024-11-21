import Classes.Path as Path
import string
import re

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.

# Please add comments along with your code.
class WordTokenizer:

    def __init__(self, content):
        # Tokenize the input texts.

        # delete "" first
        pattern = r'"(.*?)"'
        content = re.sub(pattern, r'\1', content)

        # create my tokenizer
        delete_str = "(),:-_.@!?#&$;:[]{}=/+"
        transtab = str.maketrans(delete_str, "                      ")
        content = content.translate(transtab)
        self.tokens = content.split()
        self.count = 0
        return

    def nextWord(self):
        # Return the next word in the document.
        # Return null, if it is the end of the document.

        # check the null situation
        if self.count == len(self.tokens):
            return None
        # get the next word
        word = self.tokens[self.count]
        self.count = self.count + 1
        return word