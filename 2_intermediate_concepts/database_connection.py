from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Database URL
sqlalchemy_database_url = 'sqlite:///./blogs.db'
# sqlite:/// -> specifies databse dialect/type, different databse systems,
#               like MySQL, PostgreSQL, have their own dialect
#               dialect: component responsible for translating py code generated
#                        by SQLAlchemy into specific SQL syntax
# ./ -> loaction-> current directory
# blogs.db -> SQLite databse file


# engine - central component that manages connection to a database and
#          provides a source of connectivity for executing SQL commands
engine = create_engine(sqlalchemy_database_url,
                       connect_args={"check_same_thread": False}
                       )
# connect_args - used to pass additional options or arguments directly to the
#                underlying databse connection
# "check_same_thread": False - all connections to be used across multiple threads
# threads- fundamental units of execution within a process. These are sequence
#          of instructions that can be executed independently within a program


# session- high level component that interacts with the database through the 'Engine'
#          manages interactions between python objects and the database
SessionLocal = sessionmaker(bind=engine,
                            autocommit=False,
                            autoflush=False)
# autocommit=False - changes made during a session will not automatically
#                    be committed to the database
# flush() ensures that any pending changes made to objects within the session are flushed out
# to the database. This includes INSERT,UPDATE,etc that have been made to objects
#  but haven't yet been committed
# autoflush=False - we need to manually handle flushing changes to the database

# base class for declarative class definations
Base = declarative_base()
# foundation for defining ORM-mapped classes, which represent tables in a relationl database
