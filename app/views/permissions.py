import os
from functools import wraps

from app import app, DefaultPaths, TOKEN
from flask import request, jsonify

from loguru import logger

log = logger
log.add(f"{os.path.join(DefaultPaths.LOG_PATH)}/permissions.log", rotation="5 MB",
        format="[{time:HH:mm:ss}] [{level}] {message}")


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        log.debug(f"token: {token}")

        if not token:
            return jsonify({'response': 401, 'message': 'Unauthorized'})

        if token == TOKEN:
            log.debug("Authorized !")
            return f(*args, **kwargs)
        else:
            return jsonify({'response': 401, 'message': 'Unauthorized'})
    return decorator


@app.after_request
def set_header(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET"
    return response
