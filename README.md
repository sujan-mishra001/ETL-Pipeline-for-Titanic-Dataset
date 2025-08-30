# Titanic ETL Pipeline 
This project shows an ETL (Extract, Transform, Load) pipeline using the Titanic dataset in PostgresSQL.

## Project Structure 
- `extract.py`: Extracts data from CSV files. 
- `transform.py`: Transforms and cleans the data. 
- `load.py`: Loads the data into a PostgreSQL database using SQLAlchemy. 
- `main.py`:  Execute the ETL process. 
- `config.py`: Stores database config. 
- `titanic.csv`: The Sample Titanic dataset. 
- `postgres/docker-compose.yaml`: Contains Docker Compose file for PostgreSQL setup. 

## How to Run 
1. Start PostgreSQL using Docker Compose: 
``` 
cd postgres 
docker compose up 
``` 

2. Login to the pgAdmin page with 

``` 
email: admin@123.com 
password: admin123
``` 
And PostgresSQL with 

``` 
host: postgres 
database: database 
username: admin 
```
Change the pgAdmin and PostgresSQL database credentials in the docker-compose.yaml according to your need.

3. Update `config.py` with your database credentials if changed. 

4. Run the ETL pipeline:

``` 
python main.py
 ``` 


## Requirements 
- Python 3.8+ 
- pandas 
- SQLAlchemy 
- Docker (for PostgreSQL) 

## Purpose 
To Build a simple ETL pipeline which stores the titanic dataset in the PostgresSQL.

