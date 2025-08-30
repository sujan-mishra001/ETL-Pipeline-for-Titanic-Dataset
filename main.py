from extract import extract_data
from transform import transform_data
from load import get_engine,load_data
import config

def main():
    #Using the extract_data from extract.py to extract data
    df=extract_data("titanic.csv")
    #Using transform_data from trasnform.py to transform extracted data
    df_transform=transform_data(df)
    #Using get_engine from load.py to connect to  postgres database 
    engine=get_engine(config.db_config)
    #Using load_data from load.py to load the trasnformed data into postgres database
    load_data(df_transform,engine)

if __name__=='__main__':
    main()