from flask import Flask
from views import home_views, package_views, cms_views, account_views
import os
from data.db_session import global_init

app = Flask(__name__)

def register_blueprints():
    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(package_views.blueprint)
    app.register_blueprint(cms_views.blueprint)
    app.register_blueprint(account_views.blueprint)

def setup_db():
    db_file = os.path.join(os.path.dirname(__file__),"db","pypi.sqlite")
    global_init(db_file)

def main():
    register_blueprints()
    setup_db()
    app.run(debug=True, port="5000", host="127.0.0.1")

if __name__ == "__main__":
    main()