import os
from docx import Document
import subprocess

# define a function to count words in a .docx file
def count_words_in_docx(file):
    doc = Document(file)
    count = 0
    for para in doc.paragraphs:
        count += len(para.text.split())
    return count

# list files in the target directory
dir_path = './texts/'
files = os.listdir(dir_path)

# this flag is used to check if any file has been deleted
file_deleted = False

# iterate over the files
for file in files:
    if file.endswith('.docx'):  # if the file is a Word document
        file_path = os.path.join(dir_path, file)
        word_count = count_words_in_docx(file_path)
        print(f'{file} has {word_count} words.')

        if word_count > 5000:
            print(f'Deleting {file}...')
            os.remove(file_path)
            file_deleted = True

# if any file has been deleted, run all.py
if file_deleted:
    subprocess.call(['python', 'all.py'])
