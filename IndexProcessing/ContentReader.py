import Classes.Path as Path
import json

class MyContentReader:

    def __init__(self):

        with open(Path.noToContent1, 'r') as f:
            self.content1 = json.load(f)

        with open(Path.noToContent2, 'r') as f:
            self.content2 = json.load(f)

        with open(Path.noToContent3, 'r') as f:
            self.content3 = json.load(f)

        with open(Path.noToContent4, 'r') as f:
            self.content4 = json.load(f)

        with open(Path.noToContent5, 'r') as f:
            self.content5 = json.load(f)

        with open(Path.noToContent6, 'r') as f:
            self.content6 = json.load(f)

        with open(Path.noToContent7, 'r') as f:
            self.content7 = json.load(f)

        with open(Path.noToContent8, 'r') as f:
            self.content8 = json.load(f)


    def getContent(self, docNO):
        if docNO in self.content1:
            return self.content1[docNO]
        elif docNO in self.content2:
            return self.content2[docNO]
        elif docNO in self.content3:
            return self.content3[docNO]
        elif docNO in self.content4:
            return self.content4[docNO]
        elif docNO in self.content5:
            return self.content5[docNO]
        elif docNO in self.content6:
            return self.content6[docNO]
        elif docNO in self.content7:
            return self.content7[docNO]
        elif docNO in self.content8:
            return self.content8[docNO]
        else:
            return None