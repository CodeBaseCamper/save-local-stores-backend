import os

from loguru import logger

from app import app, DefaultPaths, sql, return_json
from app.views.permissions import token_required

log = logger
log.add(f"{os.path.join(DefaultPaths.LOG_PATH)}/shops.log", rotation="5 MB",
        format="[{time:HH:mm:ss}] [{level}] {message}")


@app.route('/shops/<int:shop_id>', methods=['GET'])
#@token_required
def get_shop_info_by_id(shop_id):
    results = sql.query_where(
        'shops',
        args={'id': shop_id},
        select=[
            "id",
            "description",
            "business_categorie_id",
            "name",
            "owner_firstname",
            "owner_lastname",
            "owner_picture_",
            "picture_id",
            "street",
            "street_number",
            "telephone",
            "zip_code",
            "quote"
        ]
    )

    return return_json(results)
