# -*- coding: utf-8 -*-
from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
import os

# Instancia de la aplicación de flask
app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app, resources= { r"/*": {"origins": "*"} })

# COnfiguración de la base de datos Mongo y su conección
app.config['MONGO_URI'] = 'mongodb://lignum-devteam:Eafit2020@ds030817.mlab.com:30817/lignum-project'
mongo = PyMongo(app)

# Definiciones de rutas de los blueprints


# Instancias del Blueprint



@app.route('/')
def index():
    return 'Server on'
