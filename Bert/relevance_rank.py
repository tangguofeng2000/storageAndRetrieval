import IndexProcessing.MyIndexReader as IndexReader
import Classes.Document as Document
import re

class relevance_rank:

    def __init__(self):
        self.reader = IndexReader.MyIndexReader()
        return

    def relevance_rank(self, query_content, topN, miu = 2000):
        query_tokens = re.split(r'[^^a-zA-Z0-9]', query_content)
        for item in query_tokens:
            if item == '':
                query_tokens.remove(item)

        # Calculate the probability of each word P(w|Ms) = #(w,S) / |S|
        query_post_list, doc_all = [], []
        for word in query_tokens:
            post_list = self.reader.getPostingList(word)
            #print(post_list)
            if post_list:
                query_post_list.append(post_list)

                for doc in post_list:
                    if doc not in doc_all:
                        doc_all.append(doc)
            else:
                query_post_list.append([])

        prob_Ref = {}
        for i in range(len(query_tokens)):
            # check if the word appears in the whole collection
            df = self.reader.DocFreq(query_tokens[i])
            if df == 0:
                prob_Ref[query_tokens[i]] = 1
            else:
                total_word_count, total_doc_length = 0,0
                for doc_id in doc_all:
                    doc_length = self.reader.getDocLength(doc_id)
                    if doc_id not in query_post_list[i]:
                        continue
                    else:
                        word_count = query_post_list[i][doc_id]
                        total_word_count += word_count
                        total_doc_length += doc_length
                prob_Ref[query_tokens[i]] = total_word_count / total_doc_length

        # calculate the probability of each query in each document, save as a dictionary
        prob_dic = {}
        for doc_id in doc_all:
            doc_length = self.reader.getDocLength(doc_id)
            prob_query = 1
            for i in range(len(query_post_list)):
                # detect the cases where the word doesn't appear in the document
                if doc_id in query_post_list[i]:
                    word_count = query_post_list[i][doc_id]
                    #prob_word = (word_count+miu*1) / (doc_length+miu)
                    prob_word = (word_count + miu * prob_Ref[query_tokens[i]]) / (doc_length + miu)
                    prob_query = prob_query * prob_word
                else:
                    #prob_word = (0+miu*1) / (doc_length+miu)
                    prob_word = (0 + miu * prob_Ref[query_tokens[i]]) / (doc_length + miu)
                    prob_query = prob_query * prob_word
            prob_dic[doc_id] = prob_query
        # Rank the dictionary by the value, and slice the topN
        topN_dic = dict(sorted(prob_dic.items(), key=lambda x: x[1], reverse=True)[:topN])

        # save the document objects
        doc_obj_list = []
        for doc_id in topN_dic:
            doc_obj = Document.Document()
            doc_No = self.reader.getDocNO(doc_id)
            doc_obj.setDocId(doc_id)
            doc_obj.setDocNo(doc_No)
            doc_obj.setScore(topN_dic[doc_id])
            doc_obj.setWeb(self.reader.getDocURL(doc_id))
            doc_obj_list.append(doc_obj)

        return doc_obj_list
