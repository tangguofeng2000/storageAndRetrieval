import Classes.Path as Path
import json

# Please explain the code with necessary comments.
class IndexProcessing:

    def __init__(self):
        self.content1 = []
        self.count = 0

        with (open(Path.Content8, 'r', encoding='utf-8') as file):
            for line in file:
                entry = json.loads(line)
                self.content1.append(entry)

        self.length = len(self.content1)

        return

    def nextDocument(self):
        if self.count == self.length:
            return None

        docID = self.count
        self.count = self.count + 1

        docContent = self.content1[docID]["text"]
        docNO = self.content1[docID]["docno"]
        return [docNO, docContent, self.count]
