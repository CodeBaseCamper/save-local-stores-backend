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

    query = """
        SELECT
            "shops"."description",
            "shops"."business_categorie_id",
            "shops"."name",
            "shops"."owner_firstname",
            "shops"."owner_lastname",
            "shops"."owner_picture",
            "shops"."picture",
            "shops"."street",
            "shops"."street_number",
            "shops"."telephone",
            "shops"."zip_code",
            "business_categories"."name" AS "business_categorie_name"
        FROM
            "shops"
        INNER JOIN 
            "business_categories"
            ON
            "business_categories"."id" = "shops"."business_categorie_id"
        WHERE
            "shops"."city_id" = %(city_id)s
    """

    result = sql.query(query, {'city_id': city_id})
    return return_json(result)
