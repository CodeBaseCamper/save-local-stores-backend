from typing import Union

from flask import jsonify


def return_json(data: Union[list, dict] = None, status: int = 200, message: str = ""):
    return jsonify({'status': status, 'message': message, 'results': data})
