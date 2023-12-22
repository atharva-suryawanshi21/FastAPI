from pydantic import BaseModel


class schema_class(BaseModel):

    username: str
    email: str
    password: str
