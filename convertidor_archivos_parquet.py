import glob
import pandas as pd #instalar !pip install pandas pyarrow en caso no lo tenga
import os

list_folders_to_review = ['*.csv','Concatenated_Data\*.csv','Transformed_Data\*.csv']

files = []

for x in list_folders_to_review:
    files.extend(glob.glob(x))

for x in files:
    print(x)
    test = pd.read_csv(x,sep=';',encoding='ISO-8859-1')
    test.to_parquet(x.split('.')[0]+'.parquet', compression='brotli') 
    #gzip no sirve bien en Bigquery