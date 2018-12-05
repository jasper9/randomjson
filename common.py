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

    db_host = "127.0.0.1"
    db_user = config['mysql']['user']
    db_pass = config['mysql']['password']
    db_name = config['mysql']['database_name']


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