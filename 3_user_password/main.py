from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import user_table
import user_schema
from database_connection import engine, SessionLocal
app = FastAPI()

user_table.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.post('/user')
# create user data
def create_user(request: user_schema.schema_class, db: Session = Depends(get_db)):
    user_data = user_table.table_class(
        username=request.username, email=request.email, password=request.password)
    db.add(user_data)
    db.commit()
    db.refresh(user_data)
    return user_data
