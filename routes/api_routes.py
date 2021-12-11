from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from services.auth_service import AuthService
bp = Blueprint('apis', __name__, url_prefix="/api")

@bp.route("/authenticate",methods = ["POST"])
def auth():
    content = request.json
    return AuthService.auth_user(content)