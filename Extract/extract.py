#Extracting data using pandas
import pandas as pd

def extract_data(file_path):
    df=pd.read_csv(file_path)
    print('Data Extrcted')
    return df