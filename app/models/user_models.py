from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("mysql+mysqlconnector://root:123456@localhost/test")
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    try:
        db = Session()
        yield db
    finally:
        db.close()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), index=True)
    email = Column(String(100), index=True)
    password = Column(String(256))

Base.metadata.create_all(bind=engine)