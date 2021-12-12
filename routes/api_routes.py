import os
from flask import (
    Blueprint, flash, g, json, redirect, render_template, request, session, url_for, jsonify
)
from models.data_dto import DataDTO
from services.auth_service import AuthService
from werkzeug.datastructures import MultiDict

from services.data_service import DataService

bp = Blueprint('apis', __name__, url_prefix="/api")

@bp.route("/authenticate",methods = ["POST"])
def auth():
    content = request.json
    return AuthService.auth_user(content)

@bp.route("/upload",methods=["POST"])
def upload():
    f = request.files
    file = f.get("file")
    data_service = DataService()
    resp = {"status":"failed"}
    if file != None:
        obj = json.load(file)
        for data in obj:
            print(data)
            data_dto = DataDTO(id=data["id"],userId=data["userId"],title=data["title"],body=data["body"])
            data_service.entry_into_db(data_dto=data_dto)
        resp["status"] = "success"
    return resp