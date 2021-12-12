from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from services.auth_service import AuthService
from services.data_service import DataService
from services.user_service import UserService
bp = Blueprint('pages', __name__)

@bp.route("/")
def home_page():
    result = AuthService.is_logged_in()
    if result != True:
        return result
    user_service = UserService()
    user = user_service.get_user_by_username(username=session.get("username"))
    return render_template("home.html")

@bp.route("/login",methods=["GET","POST"])
def login_page():
    if request.method == "POST":
        return redirect(url_for("pages.home_page"))
    else:
        return render_template("login.html")

@bp.route('/logout')
def logout():
    if session.get("username"):
        session.pop('username', None)
        return redirect(url_for('pages.login_page'))

@bp.route('/showdata')
def show_data():
    result = AuthService.is_logged_in()
    if result != True:
        return result
    data_service = DataService()
    data_dtos = data_service.get_all()
    return render_template("showdata.html",data_dtos=data_dtos)