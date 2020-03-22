import os

from flask import jsonify, send_file, abort
from loguru import logger

from app import app, DefaultPaths, sql, return_json
from app.helper.helper import get_voucher_pdf
from app.views.permissions import token_required

log = logger
log.add(f"{os.path.join(DefaultPaths.LOG_PATH)}/vouchers.log", rotation="5 MB",
        format="[{time:HH:mm:ss}] [{level}] {message}")


@app.route('/vouchers/<int:voucher_id>', methods=['GET'])
#@token_required
def get_voucher_by_id(voucher_id):
    log.debug(f"Get voucher_id [{voucher_id}] requested..")

    query = """
        SELECT
            "vouchers"."timestamp",
            "vouchers"."amount",
            "vouchers"."code",
            "shops"."name",
            "shops"."street",
            "shops"."street_number",
            "shops"."zip_code",
            "shops"."telephone"
        FROM
            "vouchers"
        INNER JOIN
            "shops"
            ON
            "shops"."id" = "vouchers"."shop_id"
        WHERE 
            "vouchers"."id" = %(voucher_id)s
    """

    result = sql.query(query, args={'voucher_id': voucher_id})

    return return_json(result)


@app.route('/vouchers/pdf/<int:shop_id>/<int:amount>', methods=['GET'])
def test(shop_id, amount):
    log.info(f"Generate PDF for shop[{shop_id}] with an amount of {amount} EURO.")
    amount = "{0:.2f}".format(amount)
    file_path = None
    try:
        # generate pdf
        file_path = get_voucher_pdf(shop_id, amount)
    except Exception:
        abort(500)

    return send_file(file_path, attachment_filename='Kiezmarie_Voucher.pdf', as_attachment=False)
