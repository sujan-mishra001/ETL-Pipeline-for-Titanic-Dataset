def transform_data(df):
    df_clean=df
    df_clean['Sex']=df_clean['Sex'].map({'female':1,'male':0})
    uniques=df_clean['Embarked'].unique()
    mapping={x:i for i, x in enumerate(uniques) }
    df_clean['Embarked']=df_clean['Embarked'].map(mapping)
    
    
    print("data tranformed succesfully")
    print("data after transormed")
    print(df_clean.head(5))
    return df_clean