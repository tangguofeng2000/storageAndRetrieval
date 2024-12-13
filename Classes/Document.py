class Document:

    def __init__(self):
        return

    docid = ""
    docno = ""
    website = ""
    score = 0.0

    def getDocId(self):
        return self.docid

    def getDocNo(self):
        return self.docno

    def getScore(self):
        return self.score

    def getWeb(self):
        return self.website

    def setDocId(self, docid):
        self.docid = docid

    def setDocNo(self, no):
        self.docno = no

    def setScore(self, the_score):
        self.score = the_score

    def setWeb(self, website):
        self.website = website