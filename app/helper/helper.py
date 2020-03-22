import os
from binascii import hexlify
from pathlib import Path
from typing import Union

from app import sql, DefaultPaths

from flask import jsonify
from xhtml2pdf import pisa


def return_json(data: Union[list, dict] = None, status: int = 200, message: str = ""):
    data = data if data else []
    return jsonify({'status': status, 'message': message, 'results': data})


def get_voucher_pdf(shop_id, amount):
    # get new uniq voucher code
    voucher_code = generate_voucher_code(shop_id, amount)

    file_path = os.path.join(DefaultPaths.PDF_PATH, f"{voucher_code}.pdf")
    if not Path(DefaultPaths.PDF_PATH).exists():
        os.makedirs(DefaultPaths.PDF_PATH, exist_ok=True)

    # todo make beauty
    src_html = sql.query_where('pdf_templates', {'id': 1}, select='html_css')
    shop_name = sql.query_where('shops', {'id': shop_id}, select={'name'})[0]['name']
    src_html = src_html[0]['html_css'] % {'voucher_code': voucher_code, 'shop_name': shop_name, 'amount': amount}
    result_file = open(file_path, "w+b")

    # convert HTML to PDF
    pisa.CreatePDF(
        src_html,                # the HTML to convert
        dest=result_file)   # file handle to recieve result

    # close output file
    result_file.close()
    return file_path


def generate_voucher_code(shop_id: int, amount: str) -> str:
    voucher_code = None
    for i in range(2):
        key = str(hexlify(os.urandom(21)).upper().decode(encoding="utf-8"))
        voucher_code = f"{(key[0:4])}-{key[5:9]}-{key[10:14]}-{key[15:19]}"
        if check_voucher_exist(voucher_code):
            break

    if not voucher_code:
        raise Exception("Can't generate Voucher code! To many retries.")

    insert_new_voucher(voucher_code, shop_id, amount)
    return voucher_code


def insert_new_voucher(voucher_code, shop_id, amount):
    query = """
        INSERT INTO "vouchers" (shop_id, amount, code) VALUES
        (%(shop_id)s, %(amount)s, %(voucher_code)s)
    """

    sql.query(query, {'shop_id': shop_id, 'amount': amount, 'code': voucher_code})



def check_voucher_exist(voucher_code):
    # check if voucher code in database already exist
    result = sql.query_where('vouchers', {'code': voucher_code}, select='id')

    if result:
        return False
    else:
        return True
