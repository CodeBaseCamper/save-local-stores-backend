# coding=utf-8
from app import app
from flask import render_template, abort


@app.errorhandler(403)
def forbidden(e):
    abort(403)


@app.errorhandler(404)
def page_not_found(e):
    abort(404)


@app.errorhandler(500)
def internal_server_error(e):
    abort(500)
