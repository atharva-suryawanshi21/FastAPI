from database_connection import Base
from sqlalchemy import Column, Integer, String


class table_class(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
