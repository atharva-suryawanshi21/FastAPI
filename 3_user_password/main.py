
import user_table
import user_schema
from fastapi import FastAPI


def get_database_connection_modeule():
    import sys
    # Add the path to the directory containing database_connection.py
    sys.path.append('2_intermediate_concepts')
    from database_connection import engine, SessionLocal, Base
    return engine, SessionLocal, Base


engine, SessionLocal, Base = get_database_connection_modeule()

app = FastAPI()

user_table.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
