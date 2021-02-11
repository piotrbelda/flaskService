import datetime
from sqlalchemy import DateTime, String, Column
from data.modelbase import SqlAlchemyBase

class Audit(SqlAlchemyBase):
    __tablename__ = "auditing"

    id = Column(String, primary_key=True)
    create_date = Column(DateTime, default=datetime.datetime.now, index=True)
    description = Column(String)