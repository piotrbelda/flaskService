import datetime
from sqlalchemy import Column, Integer, String, DateTime
from data.modelbase import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    email = Column(String, index=True, unique=True, nullable=True)
    hashed_password = Column(String, nullable=True, index=True)
    created_date = Column(DateTime, default=datetime.datetime.now, index=True)
    profile_image_url = Column(String)
    last_login = Column(DateTime, default=datetime.datetime.now, index=True)