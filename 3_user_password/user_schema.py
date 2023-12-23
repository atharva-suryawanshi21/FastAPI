from pydantic import BaseModel


class schema_class(BaseModel):

    username: str
    email: str
    password: str


class Show_User(BaseModel):
    username: str
    email: str

    class Config():
        from_attributes = True
