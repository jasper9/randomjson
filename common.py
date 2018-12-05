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

    db_host = config['backend']['db_host']
    db_user = config['backend']['db_user']
    db_pass = config['backend']['db_pass']
    db_name = config['backend']['db_name']

    print("DB PASS: "+db_pass)
    db = pymysql.connect(
        host        =   db_host,
        user        =   db_user,
        password    =   db_pass,
        db          =   db_name,
        charset     =   'utf8mb4',
        cursorclass =   pymysql.cursors.DictCursor)

    db.cursor()
    return(db)

def disconnectDB(db):
    db.commit()
    db.close()   