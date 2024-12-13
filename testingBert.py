import torch
from transformers import BertModel, BertTokenizerFast
import torch.nn.functional as F
import IndexProcessing.ContentReader as ContentReader

# 获取一下content
docNO = "en.noclean.c4-train.00020-of-07168.0"
myReader = ContentReader.MyContentReader()
english_sentences1 = myReader.getContent(docNO)

def similarity(embeddings_1, embeddings_2):
    normalized_embeddings_1 = F.normalize(embeddings_1, p=2)
    normalized_embeddings_2 = F.normalize(embeddings_2, p=2)
    return torch.matmul(
        normalized_embeddings_1, normalized_embeddings_2.transpose(0, 1)
    )

tokenizer = BertTokenizerFast.from_pretrained("sartifyllc/AviLaBSE")
model = BertModel.from_pretrained("sartifyllc/AviLaBSE")
model = model.eval()

english_inputs1 = tokenizer(english_sentences1, return_tensors="pt", padding=True)

with torch.no_grad():
    english_outputs1 = model(**english_inputs1)

english_sentences2 = [
    "Please protect the Environment"
]

english_inputs2 = tokenizer(english_sentences2, return_tensors="pt", padding=True)

with torch.no_grad():
    english_outputs2 = model(**english_inputs2)

# 获取嵌入
embeddings1 = english_outputs1.pooler_output
embeddings2 = english_outputs2.pooler_output

# 判断相似性
simi = similarity(embeddings1, embeddings2)
print(simi[1][0].item())