from tika import parser # pip install tika
import os
import pandas as pd
from PyPDF2 import PdfFileReader 


def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
    
    author = info.author
    creator = info.creator
    producer = info.producer
    subject = info.subject
    title = info.title
    return title,author

directory = './pdf/'
authors=[]
titles=[]
text=[]
i=1
# Todos os arquivos do diretório
for file_name in os.listdir(directory):
    print(i)
    
    try:
        title,author = get_info(directory+file_name)
        raw = parser.from_file(directory+file_name)
        texto= str(raw['content'])
    except:
        title=file_name
        author=''
        texto=''
    
    authors.append(author)
    titles.append(title)
    text.append(texto)
    i=i+1
    

d = {   'title':titles,
        'author':authors,
        'text': text
    }

pd.DataFrame(data = d).to_csv("resumos.csv", sep=";")