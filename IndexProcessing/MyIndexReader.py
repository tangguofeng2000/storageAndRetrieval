import Classes.Path as Path
import json


# Efficiency and memory cost should be paid with extra attention.
class MyIndexReader:

    def __init__(self):
        # idToOther中，存储了文档id对应的一系列数据
        # 从前往后依次是：
        # docNO、content文章内容、timestamp文章创建时间、url文章所在网站、domainCount域名计数（此处用作域名权威性）
        with open(Path.idToOther, 'r') as f:
            self.idToOther = json.load(f)

        with open(Path.NOToID, 'r') as f:
            self.NOToID = json.load(f)

        # key是word，value是(doc:feq)的二元组
        with open(Path.index_dict, 'r') as f:
            self.index_dict = json.load(f)

    # 输入为文档NO，输出为NO对应的ID
    def getDocId(self, docNO):
        docNO = str(docNO)
        return self.NOToID[docNO]

    # 输入为ID，输出为ID对应的文档的NO
    def getDocNO(self, docID):
        docID = str(docID)
        return self.idToOther[docID][0]

    # 输入为ID，输出为ID对应的文档内容
    def getDocContent(self, docID):
        docID = str(docID)
        return self.idToOther[docID][1]

    # 输入为ID，输出为ID对应的时间戳
    def getDocTime(self, docID):
        docID = str(docID)
        return self.idToOther[docID][2]

    # 输入为ID，输出为网页url
    def getDocURL(self, docID):
        docID = str(docID)
        return self.idToOther[docID][3]

    # 输入为ID，输出为网页专业度
    def getDocDomainCount(self, docID):
        docID = str(docID)
        return self.idToOther[docID][4]

    # Return DF.
    def DocFreq(self, token):
        if token in self.index_dict:
            return len(self.index_dict[token])
        else:
            return 0

    # Return the frequency of the token in whole collection/corpus.
    def CollectionFreq(self, token):
        return sum(self.index_dict[token].values())

    # 返回单词在特定文章的出现频率
    def WordFreq(self, token, docID):
        docID = str(docID)
        return self.index_dict[token][docID]

    # Return posting list in form of {documentID:frequency}.
    def getPostingList(self, token):
        if token in self.index_dict:
            return self.index_dict[token]
        return None

    # Return the length of the requested document.
    def getDocLength(self, docID):
        words = self.getDocContent(docID)
        return len(words)