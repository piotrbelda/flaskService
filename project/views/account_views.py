import flask
from flask import request
from services import user_service
from infrastructure.view_modifiers import response
import infrastructure.cookie_auth as cookie_auth
from services.user_service import verify_hash

blueprint = flask.Blueprint('account', __name__, template_folder='templates')

@blueprint.route('/account')
@response(template_file='account/index.html')
def index():
    user_id = cookie_auth.get_user_id_via_auth_cookie(flask.request)

    if user_id is None:
        return flask.redirect("account/login")

    user = user_service.find_user_by_id(user_id)
    if not user:
        return flask.redirect("account/login")
    return {
        "user": user,
        "user_id": user.id
    }

@blueprint.route('/account/register', methods=['GET'])
@response(template_file='account/register.html')
def register_get():
    return {
        "user_id": cookie_auth.get_user_id_via_auth_cookie(request)
    }

@blueprint.route('/account/register', methods=['POST'])
@response(template_file='account/register.html')
def register_post():
    r = flask.request
    name = r.form['name']
    email = r.form['email']
    password = r.form['password']

    user = user_service.create_user(name, email, password)

    if not user:
        return {
            "error": "Some required fields are missing.", "name": name,
            "email": email, "password": password,
            "user_id": cookie_auth.get_user_id_via_auth_cookie(request)
        }

    resp = flask.redirect("/account")
    cookie_auth.set_auth(resp, user.id)

    return resp

@blueprint.route('/account/login', methods=['GET'])
@response(template_file='account/login.html')
def login_get():
    return {
        "user_id": cookie_auth.get_user_id_via_auth_cookie(request)
    }

@blueprint.route('/account/login', methods=['POST'])
@response(template_file='account/login.html')
def login_post():
    r = flask.request
    email = r.form['email']
    password = r.form['password']

    if not email or not password:
        return {
            "error": "Some required fields are missing.", "email": email, "password": password,
            "user_id": cookie_auth.get_user_id_via_auth_cookie(request)
        }

    user = user_service.login_user(email, password)
    if not user:
        return {
            "email": email,
            "password": password,
            "error": "The account does not exist or the password is wrong",
            "user_id": cookie_auth.get_user_id_via_auth_cookie(request)
        }

    resp = flask.redirect("/account")
    cookie_auth.set_auth(resp, user.id)

    return resp

@blueprint.route('/account/logout')
def logout():
    resp = flask.redirect("/")
    cookie_auth.logout(resp)

    return resp