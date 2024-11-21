# 测试Reader功能用的文件，后续正式版本可以删掉该文件
import IndexProcessing.MyIndexReader as IndexReader

reader = IndexReader.MyIndexReader()

print(reader.getDocContent(1))
docNO = reader.getDocNO(1)
print(docNO)
print(reader.getDocId(docNO))
print(reader.getDocURL(1))
print(reader.getDocTime(1))
print(reader.getDocDomainCount(1))
print(reader.DocFreq('servic'))
print(reader.CollectionFreq('servic'))
print(reader.WordFreq('servic', 1))