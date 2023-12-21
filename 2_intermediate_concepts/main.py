from fastapi import FastAPI, Depends, status, Response, HTTPException
import schema
import model_schema
from database_connection import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

model_schema.Base.metadata.create_all(engine)
# responsible to create tables in the database based on SQLAlchemy models defined
# in the 'model_schema' module


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
# creates new Database session
# when 'yield' is used in a function, it turns that function into a generator
# generator functions produce a series of values and maintain their state between calling of them,
#     i.e. generators 'yield' a value and pause execution, allowing the function
#     to be resumed from where it left off
# unlike regular functions that return a value and exit


@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: schema.blog_info, db: Session = Depends(get_db)):
    # new instance of Blog model
    new_blog = model_schema.Blog(title=request.title, body=request.body)
    db.add(new_blog)  # adds newly created instance to database session db
    db.commit()
    db.refresh(new_blog)
    return new_blog  # returns newly created blog object as response

# request- represents Pydantic model or schema describing
#          the structure of incoming JSON data for creating a blog
# db - SQLAlchemy session that the function can use
#      to interact with the database
# refresh() - 1. Synchronizing State: aligns the object's state in the SQLAlchemy
#                session with its current state in the database
#             2. Reflect DB Changes: updates the session object to mirror any alterations
#                made to the corresponding database entity by other sessions, triggers, etc
#             3. Maintain Consistency: ensures session's object accurately represents
#                the most recent database data for that specific entity
# status_code - default->200, indicates successful request
#               201, explicitly communicates that the request was successful and resulted
#               in the creation of a new resource
# need of 201: 1. Client Understanding: clear indication of success helps clients comprehend their action's outcome
#              2. Semantic Clarity: Specific status codes alighn with RESTful principles enhancing API clarity
#              3. Error Handling
# note: 201 for resource creations not for updating existing resources


@app.get('/blog')
# to get all the blogs
def get_all_blogs(db: Session = Depends(get_db)):
    all_blogs = db.query(model_schema.Blog).all()
    return all_blogs
# query() - used to construct a database query to retrive data from database


@app.get('/blog/{id}')
# to get specific blog
# also handle situation where the requested id is absent
def get_specific(id: int,  get_response: Response, db: Session = Depends(get_db)):
    blog = db.query(model_schema.Blog).filter(
        model_schema.Blog.id == id).first()

    if not blog:
        # get_response.status_code = status.HTTP_404_NOT_FOUND
        # return {'Detail': f"The blog with id : {id} not found"}
        # instead of above code, below code to implemented
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The blog with id : {id} not found")
    return blog


@app.delete('/blog/{id}')
# to delete a blog
def delete(id, db: Session = Depends(get_db)):
    db.query(model_schema.Blog).filter(
        model_schema.Blog.id == id).delete(synchronize_session=False)

    db.commit()
    return {'detail': f"The blog with id:{id}, is deleted"}
