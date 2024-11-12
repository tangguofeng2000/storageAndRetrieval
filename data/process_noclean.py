import os
import glob
import gzip
import json
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')
nltk.download('punkt')

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def clean_text(text):
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.lower()

def preprocess_text(text):
    tokens = nltk.word_tokenize(text)
    filtered_tokens = [stemmer.stem(word) for word in tokens if word not in stop_words]
    return ' '.join(filtered_tokens)

def process_files(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    file_paths = glob.glob(os.path.join(input_folder, "*.json.gz"))
    print(f"Found {len(file_paths)} files to process in {input_folder}.")

    if not file_paths:
        print("No files found in the input folder.")
        return

    for file_path in file_paths:
        file_name = os.path.basename(file_path).replace(".json.gz", "_processed.txt")
        output_file_path = os.path.join(output_folder, file_name)

        print(f"Processing file: {file_path}")

        with gzip.open(file_path, 'rt', encoding='utf-8') as f_in, open(output_file_path, 'w', encoding='utf-8') as f_out:
            processed_lines = 0
            for line in f_in:
                try:
                    data = json.loads(line)
                    text = data.get('text', '')
                    if text:
                        cleaned_text = clean_text(text)
                        processed_text = preprocess_text(cleaned_text)
                        f_out.write(processed_text + "\n")
                        processed_lines += 1
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON in file {file_path}: {e}")
                    continue

            print(f"Finished processing {processed_lines} lines in {file_path}. Output saved to {output_file_path}")

input_folder = "en.noclean"
output_folder = "result"

process_files(input_folder, output_folder)

