import pymysql.cursors
import json as json1
from flask import Blueprint, jsonify, request, Response
from flask_restplus import Resource, Api, apidoc, reqparse, fields, Model, abort
import sys, os, string, random
from random import choice
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def connectDB():

    db_host = "10.142.0.4"
    db_user = config['backend']['user']
    db_pass = config['backend']['pass']
    db_name = config['backend']['database_name']


    db = pymysql.connect(host=db_host,
        user=db_user,
        password=db_pass,
        db=db_name,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)

    db.cursor()
    return(db)

def disconnectDB(db):
    db.commit()
    db.close()   