
import argparse
import glob
import gzip
import json
import os

def new_docno(file_number, line_number):
    return f'en.noclean.c4-train.{file_number}-of-07168.{line_number}'

def add_docnos(path, pattern="?????"):
    output_path = os.path.join(path, 'en.noclean.withdocnos')
    os.makedirs(output_path, exist_ok=True)

    files = sorted(glob.iglob(f'{path}/en.noclean/c4-train.{pattern}-of-07168.json.gz'))

    for filepath in files:
        file_number = filepath[-22:-17]
        file_name = os.path.basename(filepath)
        output_file = os.path.join(output_path, file_name)
        print(f"Processing file {file_name} with file number {file_number}...")

        with gzip.open(filepath, 'rt', encoding='utf-8') as f_in, gzip.open(output_file, 'wt', encoding='utf-8') as f_out:
            for line_number, line in enumerate(f_in):
                data = json.loads(line)
                data['docno'] = new_docno(file_number, line_number)
                f_out.write(json.dumps(data) + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Add docnos to C4 collection.')
    parser.add_argument('--path', type=str, help='Root of C4 git repo.', required=True)
    parser.add_argument('--pattern', type=str, default="?????", help='File name patterns to process.')
    args = parser.parse_args()

    add_docnos(args.path, args.pattern)
