from sqlalchemy import Column, DateTime, String, orm
from data.modelbase import SqlAlchemyBase
import datetime
from data.releases import Release


class Package(SqlAlchemyBase):
    __tablename__ = "packages"

    id = Column(String, primary_key=True)
    created_date = Column(DateTime, default = datetime.datetime.now, index=True)
    summary = Column(String, nullable=False)
    description = Column(String, nullable=False)

    home_page = Column(String)
    docs_url = Column(String)
    package_url = Column(String)

    author_name = Column(String)
    author_email = Column(String, index=True)

    license = Column(String, index=True)
    # maintainers
    # releases
    releases = orm.relation("Release", order_by=[
        Release.major_ver.desc(),
        Release.minor_ver.desc(),
        Release.build_ver.desc()
    ], back_populates="package")

    def __repr__(self):
        return "<Package {}>".format(self.id)