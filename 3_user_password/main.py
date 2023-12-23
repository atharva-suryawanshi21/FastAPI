from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session
import user_table
import user_schema
from database_connection import engine, SessionLocal
from hashing import Hash

app = FastAPI()

user_table.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.post('/user', tags=['user'])
# create user data
def create_user(request: user_schema.schema_class, db: Session = Depends(get_db)):
    user_data = user_table.table_class(username=request.username,
                                       email=request.email,
                                       password=Hash.bcrypt(request.password))
    db.add(user_data)
    db.commit()
    db.refresh(user_data)
    return user_data


@app.get('/user/{id}', response_model=user_schema.Show_User, tags=['user'])
# get only username and email with specified
def get_data(id, db: Session = Depends(get_db)):
    user_data = db.query(user_table.table_class).filter(
        user_table.table_class.id == id).first()
    if not user_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No user with id:{id} exists')
    return user_data
