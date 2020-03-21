import os

from flask import jsonify
from loguru import logger

from app import app, DefaultPaths, sql, return_json
from app.views.permissions import token_required

log = logger
log.add(f"{os.path.join(DefaultPaths.LOG_PATH)}/cities.log", rotation="5 MB",
        format="[{time:HH:mm:ss}] [{level}] {message}")


@app.route('/cities', methods=['GET'])
def show_all_cities():
    # get all cities
    log.debug("show_all_cities()")
    result = sql.query_all('cities')

    return return_json(result)
