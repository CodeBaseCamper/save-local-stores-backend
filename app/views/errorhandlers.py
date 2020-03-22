# coding=utf-8
from app import app, return_json
from flask import render_template, abort


@app.errorhandler(403)
def forbidden(e):
    return return_json(status=403, message="Forbidden")


@app.errorhandler(404)
def page_not_found(e):
    return return_json(status=404, message="Page not found!")


@app.errorhandler(500)
def internal_server_error(e):
    return return_json(status=500, message="Internal Server Error!")


@app.errorhandler(502)
def bad_gateway(e):
    return return_json(status=502, message="Bad Gateway!")
