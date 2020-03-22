from typing import Union
import uuid

from flask import jsonify


def return_json(data: Union[list, dict] = None, status: int = 200, message: str = ""):
    data = data if data else []
    return jsonify({'status': status, 'message': message, 'results': data})


def generate_voucher_id():

    voucher_id = str(uuid.uuid4())
    return voucher_id    
