from flask import Flask, Blueprint
from flask_restplus import Resource, Api, apidoc
import os
import json as json1
import sys
import configparser
import pymysql.cursors
import logging
from sys import stderr

config = configparser.ConfigParser()
config.read('config.ini')


flaskapp = Flask(__name__)
flaskapp.config.SWAGGER_UI_OPERATION_ID = True
flaskapp.config.SWAGGER_UI_REQUEST_DURATION = True
flaskapp.config.SWAGGER_UI_DOC_EXPANSION = 'list'
flaskapp.logger.addHandler(logging.StreamHandler(sys.stdout))
flaskapp.logger.setLevel(logging.DEBUG)
flaskapp.logger.debug("Hello World---------------------------------------------------------")

flaskapp.config['SECRET_KEY'] = config['other']['flask_key']


#from blueprints.api import api_v1
#from blueprints.ui import ui

#flaskapp.register_blueprint(api_v1)
#flaskapp.register_blueprint(ui)

flaskapp.config.from_object(Config())
#scheduler = APScheduler()
#scheduler.init_app(flaskapp)
#scheduler.start()

#this is scheduled to run check_pipelines() every 5 minus, but lets force one at the start:
#check_pipelines()