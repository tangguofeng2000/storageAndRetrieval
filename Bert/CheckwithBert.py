import torch
from transformers import BertModel, BertTokenizerFast
import torch.nn.functional as F
import numpy as np
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class CheckwithBert:

    def __init__(self):
        self.english_sentences1 = []
        self.english_sentences2 = []
        nltk.download('vader_lexicon')
        self.analyzer = SentimentIntensityAnalyzer()
        return

    def negetiveCheck(self, sentence):
        sentiment = self.analyzer.polarity_scores(sentence)

        if sentiment['compound'] > 0.1:
            return 1
        elif sentiment['compound'] < -0.1:
            return -1
        else:
            return 0

    def similarity(self, embeddings_1, embeddings_2):
        normalized_embeddings_1 = F.normalize(embeddings_1, p=2)
        normalized_embeddings_2 = F.normalize(embeddings_2, p=2)
        return torch.matmul(
            normalized_embeddings_1, normalized_embeddings_2.transpose(0, 1)
        )

    def getScore(self, sentence1, sentence2):
        self.english_sentences1 = sentence1
        self.english_sentences2 = sentence2
        tokenizer = BertTokenizerFast.from_pretrained("sartifyllc/AviLaBSE")
        model = BertModel.from_pretrained("sartifyllc/AviLaBSE")
        model = model.eval()

        english_inputs1 = tokenizer(self.english_sentences1, return_tensors="pt", padding=True)

        with torch.no_grad():
            english_outputs1 = model(**english_inputs1)

        english_inputs2 = tokenizer(self.english_sentences2, return_tensors="pt", padding=True)

        with torch.no_grad():
            english_outputs2 = model(**english_inputs2)

        # 获取嵌入
        embeddings1 = english_outputs1.pooler_output
        embeddings2 = english_outputs2.pooler_output

        # 判断相似性
        simi = self.similarity(embeddings1, embeddings2)

        # 将Tensor转换为NumPy数组，并扁平化为一维数组
        numpy_array = simi.numpy().flatten()

        # 将NumPy数组转换为Python列表
        list_result = list(numpy_array)

        return list_result