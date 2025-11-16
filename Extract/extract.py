#Extracting data using pandas
import pandas as pd

def extract_data(file_path):
    df=pd.read_csv(file_path)
    print('Data Extrcted successfully')
    print('Data are')
    print(df.head(5))
    return df