from db.entities import db, User, Data
from utils import constants
import os
import json

orm = db

def load_data_file(data_file):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(current_dir)
    full_file_path = os.path.join(root_dir, data_file)

    json_data = []
    with open(full_file_path, 'r') as data:
        json_data = json.load(data)

    return json_data

def load_users(json_data):
    users = json_data.get(constants.DB_DATA_KEY_CONTENT_SYSTEM_USERS)
    for user in users:
        if orm.session.get(User, user['id']) == None:
            user_data = User(
                id = user['id'],
                user_name = user['userName'],
                password = user["password"]
            )
            orm.session.add(user_data)
    orm.session.commit()

def load_initial_data(app):
    APP_CONFIG = app.config[constants.APP_CONFIG_OBJ]

    data_file = APP_CONFIG.get(constants.CONFIG_PROP_DB_INIT_DATA_FILE, constants.DEFAULT_DB_INIT_DATA_FILE)

    # Read the JSON file.
    json_data = load_data_file(data_file)

    # Load default system users.
    load_users(json_data)

