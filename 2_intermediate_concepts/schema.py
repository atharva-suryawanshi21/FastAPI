from pydantic import BaseModel


class blog_info(BaseModel):
    title: str
    body: str


class blog_title(BaseModel):
    title: str

    class Config():
        from_attributes = True

# from_attributes = True: Pydantic models are capable of:
#                   1. automatically converts ORM models to Pydantic models
#                   2. enabling ORM-specific behaviour such as allowing nested models,
#                      ignoring non-ORM-related attributes, etc
# Config: allows to configure various settings for the model, like how data is parsed
#         how validation occurs and other behavioral aspects of the model
