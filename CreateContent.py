import IndexProcessing.ContentProcessing as ContentProcessing
import IndexProcessing.ContentWriter as ContentWriter

# 写入index文件
contentDocument = ContentProcessing.IndexProcessing()
contentWriter = ContentWriter.ContentWriter()

while True:
    # 只要nextDocument()不返回None，就一直进行index写入
    doc = contentDocument.nextDocument()
    if doc == None:
        break
    contentWriter.contentStore(doc[0], doc[1])
    count = doc[2]

print(count)
contentWriter.close()



