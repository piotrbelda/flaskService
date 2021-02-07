import os
import data.db_session as db_session

def init_db():
    top_folder = os.path.dirname(__file__)
    rel_file = os.path.join("..","..","db","pypi.sqlite")
    db_file = os.path.abspath(os.path.join(top_folder, rel_file))
    db_session.global_init(db_file)

def main():
    init_db()

if __name__ == "__main__":
    main()