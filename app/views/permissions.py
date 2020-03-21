import os
from functools import wraps

from app import DefaultPaths, TOKEN
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
