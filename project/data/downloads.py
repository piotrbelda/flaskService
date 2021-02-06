import datetime
from sqlalchemy import BigInteger, DateTime, String, Column
from data.modelbase import SqlAlchemyBase

class Download(SqlAlchemyBase):
    __tablename__ = "downloads"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    create_date = Column(DateTime, default=datetime.datetime.now, index=True)

    package_id = Column(String, index=True)
    release_id = Column(BigInteger, index=True)

    ip_address = Column(String)
    user_agent = Column(String)