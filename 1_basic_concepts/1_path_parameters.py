from fastapi import FastAPI
'''
to run:
uvicorn 1_path_parameters:app --relaod
'''
# make instance of FastAPI
app = FastAPI()

# ______________________________________________________________________
# Define various endpoints and their respective path operation functions

# Root endpoint


@app.get('/')
# / -> base url, local
# get -> operation
# index -> path operation function
# @app -> path operation decorator
# the above line (decorator) defines how the following function handles the path
def index():
    return {'data': 'hello'}  # Returns a JSON response for the root URL


@app.get('/about')
def about():
    return {'data': 'about page'}

# ______________________________________________________________________


@app.get('/blog')
def blog():
    return {'data': 'blog list'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'unpublished'}
# Fast api read file , line by line, hence if we have path ->'/blog/3'
# it will simply ignore the above function and go to next function i.e. show()
# this does not happen in reverse, like if we have show() above unpublished()
# then for path '/blog/unpublished' it will throw exception as 'unpublished' is not
# an integer, which show() was expecting

# parameter and data type conversion


@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id: int):
    return {'data': {'comments': {'1', '2', '5'}}}

# ______________________________________________________________________
# Documentation endpoints
# Access Swagger UI documentation at '/docs' and ReDoc at '/redoc'
