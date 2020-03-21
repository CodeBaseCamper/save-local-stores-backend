import os

from flask import jsonify
from loguru import logger

from app import app, DefaultPaths, sql, return_json
from app.views.permissions import token_required

log = logger
log.add(f"{os.path.join(DefaultPaths.LOG_PATH)}/cities.log", rotation="5 MB",
        format="[{time:HH:mm:ss}] [{level}] {message}")


@app.route('/cities/<string:get_all>', methods=['GET'])
@app.route('/cities/<int:city_id>', methods=['GET'])
def show_all_cities(get_all: str = None, city_id: int = None):
    result = None

    if get_all == 'all':
        # get all cities
        log.debug("show_all_cities()")
        result = sql.query_all('cities')
    elif city_id:
        # get only city by id
        log.debug(f"show city of id: {city_id}")
        result = sql.query("SELECT * FROM cities WHERE id = %(city_id)s", {'city_id': city_id})

    if result is None:
        return_json(status=204, message='No data found')
    else:
        log.debug(result)
        return return_json(result)


@app.route('/cities/<int:id>', methods=['GET'])
def show_citiy_by_id():

    log.debug("show_hello()")
    data = {
        'status': 200,
        'message': "Hello"
    }
    return jsonify(data)