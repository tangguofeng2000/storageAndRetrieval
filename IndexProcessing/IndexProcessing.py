import Classes.Path as Path
import json

# Please explain the code with necessary comments.
class IndexProcessing:

    def __init__(self):
        self.file = []
        self.count = 0
        with open(Path.RawData1, 'r', encoding='utf-8') as file:
            for line in file:
                entry = json.loads(line)
                self.file.append(entry)

        with open(Path.RawData2, 'r', encoding='utf-8') as file:
            for line in file:
                entry = json.loads(line)
                self.file.append(entry)

        with open(Path.RawData3, 'r', encoding='utf-8') as file:
            for line in file:
                entry = json.loads(line)
                self.file.append(entry)

        return

    def nextDocument(self):
        if self.count == len(self.file):
            return None

        docID = self.count
        self.count = self.count + 1
        docNO = self.file[docID]['docno']
        content = self.file[docID]['text']
        timestamp = self.file[docID]['timestamp']
        url = self.file[docID]['url']

        return [docID, docNO, content, timestamp, url]