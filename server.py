from flask import Flask, Blueprint, redirect
from flask_restplus import Resource, Api, apidoc
import os
import json as json1
import sys
import configparser
import pymysql.cursors
from argparse import ArgumentParser
from multiprocessing import cpu_count
from sys import stderr
import logging

from auth import auth
from app import flaskapp

port = int(os.getenv("PORT", 9099))

@flaskapp.route('/')

def hello_world2():
    txt = "Hello World (v3)<br>"
    return txt
    

if __name__ == '__main__':


    flaskapp.run(host='0.0.0.0', port=port)  #, debug=True

