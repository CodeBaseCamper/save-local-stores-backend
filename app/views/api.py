import os

from loguru import logger

from app import app, DefaultPaths, return_json

log = logger
log.add(f"{os.path.join(DefaultPaths.LOG_PATH)}/api.log", rotation="5 MB",
        format="[{time:HH:mm:ss}] [{level}] {message}")


@app.route('/', methods=['GET'])
def show_hello():
    return return_json(message="Hello")
