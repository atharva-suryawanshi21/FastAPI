'''
1. when you need to send data from a client to your API, you send it 
    as request body
2. we check outcome of post() in documentation
3. use of BaseModel:
    Structures Data:Defines how your data should look, 
                    like specifying fields for a user's information.
    Validates Data: Sets rules for each field to ensure incoming data matches 
                    the defined structure, preventing errors.
     Handles Conversion: Converts received data into usable Python objects 
                    and serializes them (e.g., to JSON) for responses.
'''

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class blog_info(BaseModel):
    title: str
    year: int
    published: Optional[bool] = False


@app.post('/blog')
def get_data(request: blog_info):
    return {'data': f'blog with title : {request.title} and year : {request.year}'}
