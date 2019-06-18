from flask import Flask
import os
import random
import time

import pyodbc
import pandas as pd
import redis as redis
from flask import Flask, render_template, request
import sqlite3 as sql

from math import radians, sin, cos, sqrt, atan2

app = Flask(__name__)
port = int(os.getenv('VCAP_APP_PORT','5000'))
myHostname = "flyingjaguar.redis.cache.windows.net"
myPassword = "3azkQQEBo5hhkEhjS7GrD+RF8AmdpJtsjWst5KxqEYY="
r = redis.StrictRedis(host=myHostname, port=6380,password=myPassword,ssl=True)
server = 'charan.database.windows.net'
database = 'MyDB'
username = 'charan123'
password = 'Smokescreen@5'
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/records')
def records():
    return render_template('records.html')


@app.route('/list',methods=['POST', 'GET'])
def list():
    cursor = cnxn.cursor()
    d1 = request.form['d1']
    d2 = request.form['d2']
    lon = request.form['lon']
    cursor.execute("SELECT latitude,longitude,time,depthError FROM quake6 where depthError between ? and ? and longitude > ?",(d1,d2,lon),)
    row = cursor.fetchall()
    return render_template("list.html", data1=row)


if __name__ == '__main__':
    app.run()
