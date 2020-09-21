import os
import pandas as pd

directory = './pdf/'
authors=[]
titles=[]
text=[]

for file_name in os.listdir(directory):
    text.append(file_name)

d = {  
        'text': text
    }

pd.DataFrame(data = d).to_csv("arquivos.csv", sep=";")