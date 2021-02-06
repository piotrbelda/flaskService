from data.modelbase import SqlAlchemyBase
from sqlalchemy import Column, Integer, String

class Maintainer(SqlAlchemyBase):
    __tablename__ = 'maintainers'

    user_id = Column(Integer, primary_key=True)
    package_id = Column(String, primary_key=True)