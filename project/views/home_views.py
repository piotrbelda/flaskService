from flask import Blueprint
from infrastructure.view_modifiers import response
import services.package_service as package_service

blueprint = Blueprint("home",__name__, template_folder="templates")

@blueprint.route("/")
@response(template_file="home/index.html")
def home():
    test_packages = package_service.get_latest_releases()
    return {"releases": test_packages,
            "package_count": package_service.get_package_count(),
            "release_count": package_service.get_release_count(),
            "user_count": package_service.get_user_count()}

@blueprint.route("/about")
@response(template_file="home/about.html")
def about():
    return {}