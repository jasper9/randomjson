import pymysql.cursors
import json as json1
from flask import Blueprint, jsonify, request, Response
from flask_restplus import Resource, Api, apidoc, reqparse, fields, Model, abort
import sys, os, string, random, re
from random import choice
from . import config

api_v1 = Blueprint('api', 'api', url_prefix='/api/v1')

api = Api(api_v1, version='1.0', title='API',
            description='A simple API')


# MODELS ###############################################################################################################
# ######################################################################################################################






# ENDPOINTS ############################################################################################################
# ######################################################################################################################
@api.route('/helloWorld')
class helloWorld(Resource):
    def get(self):
        '''helloWorld'''
        log_debug('ENTERING :: /helloWorld')
        
        txt = {'value': 'ok'}
        return jsonify(txt)