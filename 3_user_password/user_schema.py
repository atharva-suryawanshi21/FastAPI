from pydantic import BaseModel


class User_class(BaseModel):
    name: str
    email: str
