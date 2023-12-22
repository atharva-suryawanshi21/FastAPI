# explaination of code in '2_intermediate_concepts/database_connection.py'
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

database_url = 'sqlite:///./user_database.db'

engine = create_engine(database_url,
                       connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine,
                            autocommit=False,
                            autoflush=False)

Base = declarative_base()
