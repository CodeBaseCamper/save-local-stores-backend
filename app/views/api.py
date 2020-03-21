import os

from flask import jsonify
from loguru import logger

from app import app, DefaultPaths
from app.views.permissions import token_required

log = logger
log.add(f"{os.path.join(DefaultPaths.LOG_PATH)}/api.log", rotation="5 MB",
        format="[{time:HH:mm:ss}] [{level}] {message}")


@app.route('/', methods=['GET'])
def show_hello():
    data = {
        'status': 200,
        'message': "Hello"
    }
    return jsonify(data)
