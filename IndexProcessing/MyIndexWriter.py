import json
import re
import Classes.Path as Path

# Efficiency and memory cost should be paid with extra attention.
#
# Please explain the code with necessary comments.
class MyIndexWriter:

    def __init__(self):
        # id指的是数字编号
        # no指的是文档自身的编号，即那串字符串
        # idToOther中，存储了文档id对应的一系列数据
        # 从前往后依次是：
        # docNO、content文章内容、timestamp文章创建时间、url文章所在网站、domainCount域名计数（此处用作域名权威性）
        self.idToOther = {}
        self.NOToID = {}

        # key是word，value是(doc:feq)的二元组
        self.index_dict = {}

        return

    # 该函数用于计算域名count
    def countDomain(self):
        domainCount = {}
        for i in range(len(self.idToOther)):
            # 查看域名是否存在
            docID = i
            tempDomain = self.idToOther[docID][3]
            # 存在则增加计数
            if tempDomain in domainCount:
                domainCount[tempDomain] = domainCount[tempDomain] + 1
            # 不存在则创建计数
            else:
                domainCount[tempDomain] = 1

        # 最终再将计数返回到存储中
        for i in range(len(self.idToOther)):
            docID = i
            tempDomain = self.idToOther[docID][3]
            self.idToOther[docID].append(domainCount[tempDomain])

        return

    # 该函数用于创建index
    def index(self, docID, docNO, content, timestamp, url):
        # 完成IDtoOther
        # 因为content在预处理阶段已经处理过，所以这里处理一下url即可
        match = re.search(r'//(.*?)/', url)
        domain = match.group(1) if match else None
        otherList = [docNO, content, timestamp, domain]
        self.idToOther[docID] = otherList

        # 完成NOtoID
        self.NOToID[docNO] = str(docID)

        # split content
        words = content.split()
        length = len(words)

        # 完成index
        for i in range(length):
            word = words[i]
            # check if word is stored or not
            if word in self.index_dict:
                # check if the doc is stored or not
                if id in self.index_dict[word]:
                    self.index_dict[word][docID] = self.index_dict[word][docID] + 1
                else:
                    self.index_dict[word][docID] = 1

            else:
                self.index_dict[word] = {}
                self.index_dict[word][docID] = 1

        return



    # Close the index writer, and you should output all the buffered content (if any).
    def close(self):
        file_path = "IndexData/idToOther.json"
        with open(file_path, 'w') as f:
            json.dump(self.idToOther, f)

        file_path = "IndexData/NOToID.json"
        with open(file_path, 'w') as f:
            json.dump(self.NOToID, f)

        file_path = "IndexData/index_dict.json"
        with open(file_path, 'w') as f:
            json.dump(self.index_dict, f)

        return
