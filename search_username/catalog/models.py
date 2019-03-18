from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SaveUsers(Base):
    __tablename__ = "Instagram"

    id = Column(Integer, primary_key=True)
    followers = Column(String(30))
    followings = Column(String(30))
    time = Column(String)
