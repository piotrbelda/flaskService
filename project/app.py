from flask import Flask, render_template
from views import home_views, package_views

app = Flask(__name__)

def register_blueprints():
    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(package_views.blueprint)

def main():
    register_blueprints()
    app.run(debug=True, port="5000", host="127.0.0.1")

if __name__ == "__main__":
    main()