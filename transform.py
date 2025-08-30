def transform_data(df):
    df_clean=df
    df_clean['Sex']=df_clean['Sex'].map({'female':1,'male':0})

    print("data tranformed")
    return df_clean