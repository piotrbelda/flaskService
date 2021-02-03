from flask import Blueprint
from infrastructure.view_modifiers import response

blueprint = Blueprint("package", __name__, template_folder="templates")

@blueprint.route("/project/<package_name>")
#@response(template_file="packages/details.html")
def package_details(package_name: str):
    return "Package details for {}".format(package_name)