from fastapi import FastAPI
from typing import Optional

app = FastAPI()

'''
@app.get('/blog')
def blog():
    return {'data': 'list of blogs'}
'''

# here we get all blogs from database, this is inefficient
# we use query parameters, to get required data only
# like we set limit( no. of blogs to be displayed)
# or published(blogs that are published or not)

# the query parameter is not explicitly mentioned in path, but we
# pass parameter to the operation function


@app.get('/blog')
def blog(limit: int = 21, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'list of published blogs of size {limit}'}
    else:
        return {'data': f'list of blogs of size {limit}'}

# 1. we convert datatype of limit and published to what was intended as it was default to str
#       to demonstrate above line: '/blog?limit=33&published=false'
# 2. we set these paramters to some default so we dont have to always type in queries
#       here '/blog' works too (not in just 1. case)
# 3. an optional query -> for eg. sort from latest
#       we are not using it anywhere (dont care if it exists or not) so we set it as optional
#       we used 'Optional' from 'tying' as we set default for limit and published
#       we need to default the sort too
