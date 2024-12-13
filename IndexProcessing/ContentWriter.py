import json
import re

class ContentWriter:

    def __init__(self):
        self.noToContent1 = {}

    def remove_non_ascii(self, text):
        return ''.join(c for c in text if ord(c) < 128)

    def contentStore(self, docNO, docContent):
        # 我要存一个content列表，和docID映射
        # 分别存的目标：首先分行的肯定需要分别存，然后属于同一行内的，如果出现了标点符号例如!、?、.、......，则需要分行
        docContent = self.remove_non_ascii(docContent)

        delete_pattern = r'[{}()\[\]]'
        docContent = re.sub(delete_pattern, ' ', docContent)

        delete_pattern2 = r'\\u....'
        docContent = re.sub(delete_pattern2, '', docContent)

        delete_pattern3 = '"'
        docContent = re.sub(delete_pattern3, '', docContent)

        docContent = re.sub(r"\|/", ' ', docContent)

        split_pattern = r'[.?!\n]'
        my_list = re.split(split_pattern, docContent)
        my_list = list(filter(None, my_list))

        new_list = [re.sub(r'\\u....', '', str(item)) for item in my_list]

        self.noToContent1[docNO] = new_list

        return

    def close(self):
        file_path = "IndexData/noToContent8.json"
        with open(file_path, 'w') as f:
            json.dump(self.noToContent1, f)