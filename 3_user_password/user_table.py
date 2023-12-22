
from sqlalchemy import Column, Integer, String


def get_database_connection_modeule():
    import sys
    sys.path.append('2_intermediate_concepts')
    from database_connection import Base
    return Base


Base = get_database_connection_modeule()


class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
