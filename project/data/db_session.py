from sqlalchemy import create_engine
import sqlalchemy.orm as orm

from data.modelbase import SqlAlchemyBase

__factory = None

def global_init(db_file: str):
    global __factory
    if __factory:
        return
    if not db_file or not db_file.strip():
        raise Exception("You must specify a db file.")
    conn_str = "sqlite:///" + db_file.strip()
    engine = create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    import data.__all_models
    SqlAlchemyBase.metadata.create_all(engine)

def create_session() -> orm.Session:
    global __factory
    return __factory()