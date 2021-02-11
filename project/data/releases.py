import datetime
from data.modelbase import SqlAlchemyBase
from sqlalchemy import Column, Integer, BigInteger, DateTime, String, orm, ForeignKey

class Release(SqlAlchemyBase):
    __tablename__ = 'releases'

    id = Column(Integer, primary_key=True, autoincrement=True)

    major_ver = Column(BigInteger, index=True)
    minor_ver = Column(BigInteger, index=True)
    build_ver = Column(BigInteger, index=True)

    created_date = Column(DateTime, default=datetime.datetime.now, index=True)
    last_updated = Column(DateTime, default=datetime.datetime.now, index=True)
    comment = Column(String)
    url = Column(String)
    size = Column(BigInteger)

    package_id = Column(String, ForeignKey("packages.id"))
    package = orm.relation("Package")

    @property
    def version_text(self):
        return "{}.{}.{}".format(self.major_ver, self.minor_ver, self.build_ver)