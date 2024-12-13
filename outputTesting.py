import IndexProcessing.ContentReader as ContentReader
import Bert.relevance_rank as Rmodel
import Bert.CheckwithBert as Bert
import numpy as np
import datetime

# 获取文章docs
model = Rmodel.relevance_rank()
sentence2 = ['Are fever blisters and canker sores the same?']
# sentence2 = ['Can eye diseases be treated?']
query = sentence2[0]

docs = model.relevance_rank(query, 200)

# 获取reader
myReader = ContentReader.MyContentReader()
score_model = Bert.CheckwithBert()

# 创建一个存储器，存储最高评分的文档里，最高相似度的句子分数

check = 0

startTime = datetime.datetime.now()

for doc in docs:
    # 获取每个文档和查询内容的分数，找到最高的那个分数，获取文章内容，判断内容中是否带有否定词
    docNO = doc.getDocNo()
    english_sentences1 = myReader.getContent(docNO)
    english_sentences2 = sentence2

    score = score_model.getScore(english_sentences1, english_sentences2)

    # 找到里面数值最高的值的那个下标
    max_index = np.argmax(score)
    # 获取最高分数
    max_score = score[max_index]

    if max_score > 0.3:
        # 对应这个下标找到那句话
        sentence = english_sentences1[max_index]
        # 输出部分
        print("the result doc is " + str(doc.getDocNo()) + ", it's website is " + str(
            doc.getWeb()) + ", it's doc score is "
              + str(doc.getScore()))
        print("The score of the sentence with the highest similarity is " + str(max_score))
        print("the sentence is :" + sentence)

        # 判断这句话里有没有否定词
        check_point = score_model.negetiveCheck(sentence)
        print("the emotion score is " + str(check_point))

        print("-----------------------------")

        if check_point == 1:
            # 句子偏向肯定积极
            check = check + 1
        elif check_point == -1:
            # 句子偏向否定消极
            check = check - 1



# 最终获取结果
if check > 1:
    print("Answer is Correct")
elif check < -1:
    print("Answer is Wrong")
else:
    print("We cannot judge the answer")

endTime = datetime.datetime.now()
print("time to load index & retrieve the token: ", endTime - startTime)


