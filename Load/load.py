#Connecting to postgressql using sqlachemy
from sqlalchemy import create_engine,Table,

def get_engine(db_config):
    print("Connecting to DB with config:", db_config)
    engine = create_engine(f"postgresql://{db_config['username']}:{db_config['password']}@{db_config['endpoint']}:{db_config['port']}/{db_config['database']}")
    print("DataBase Connected")
    return engine


def load_data(df, engine):
    df.to_sql('titanic', engine, if_exists='replace', index=False)
    
    print("Data loaded successfully")

    
    