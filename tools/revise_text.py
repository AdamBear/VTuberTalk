import os
import re
import argparse

def process(files, path):
    text_dict = {}
    with open("./text.txt" ,'r') as text_file:
        for line in text_file.readlines():
            line = line[:-1]
            file_name, text = line.split()[0], line.split()[1]
            text_dict[file_name] = text
    for file in files:
        if not file.endswith('.txt'):
            continue
        position = path + file
        with open(position ,'r') as f:
            ori_text = ""
            for line in f.readlines():
                ori_text = line
            if file in text_dict.keys():
                revised_text = text_dict[file]
            else:
                continue

            if revised_text != ori_text:
                print(str(file) + " " + ori_text + " --> " + revised_text)
                with open(position, 'w') as revised_file:
                    revised_file.write(revised_text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument("--path", type=str, required=True)
    args = parser.parse_args()

    files=os.listdir(args.path)

    if not os.path.exists("./text.txt"):
        print("no text.txt found!")
    else:
        process(files, args.path)