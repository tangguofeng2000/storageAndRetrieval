import IndexProcessing.IndexProcessing as IndexProcessing
import IndexProcessing.MyIndexReader as IndexReader
import IndexProcessing.MyIndexWriter as IndexWriter

# 写入index文件
indexDocument = IndexProcessing.IndexProcessing()
indexWriter = IndexWriter.MyIndexWriter()

while True:
    # 只要nextDocument()不返回None，就一直进行index写入
    doc = indexDocument.nextDocument()
    if doc == None:
        break
    indexWriter.index(doc[0], doc[1], doc[2], doc[3], doc[4])

indexWriter.countDomain()
indexWriter.close()

