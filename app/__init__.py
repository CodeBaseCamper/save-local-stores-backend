# coding=utf-8
import logging
import os
import configparser

from flask import Flask, render_template, g

from .constants import DefaultPaths

config = configparser.ConfigParser()
config.read('config.ini')

app = Flask(__name__)
app.secret_key = b'k%20RzmA7Guwy5tdC4gy&PC8Hw4t*QY9pUy2azQb*vU3uHEVb4XIQZ8w^lKUb@#wPN^y3WdZyubORI4XeFIqv*pU0uPHFGEnpd&'

debug = bool(config.getboolean('settings', 'debug'))
app.debug = debug

from .views import api

# dyn_query = DynQuery(config.get('database', 'ip'), config.get('database', 'user'), config.get('database', 'password'), config.get('database', 'database_name'))
