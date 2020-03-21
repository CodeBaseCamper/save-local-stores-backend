import os

from flask import jsonify
from loguru import logger

from app import app, DefaultPaths, sql, return_json
from app.views.permissions import token_required

log = logger
log.add(f"{os.path.join(DefaultPaths.LOG_PATH)}/cities.log", rotation="5 MB",
        format="[{time:HH:mm:ss}] [{level}] {message}")


@app.route('/cities', methods=['GET'])
#@token_required
def show_all_cities():
    # get all cities
    log.debug("show_all_cities()")
    result = sql.query_all('cities')

    return return_json(result)


@app.route('/cities/shops/<int:city_id>', methods=['GET'])
#@token_required
def get_all_shops_by_city_id(city_id):
    result = sql.query_where(
        'shops',
        args={'city_id': city_id},
        select=[
            "id",
            "description",
            "business_categorie_id",
            "name",
            "owner_firstname",
            "owner_lastname",
            "owner_picture",
            "picture",
            "street",
            "street_number",
            "telephone",
            "zip_code"
        ]
    )

    return return_json(result)
