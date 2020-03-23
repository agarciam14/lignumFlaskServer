# -*- coding: utf-8 -*-
from flask import Flask, render_template
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
from project.geolocalizado.geolocalizado import geolocalizador_app
from project.crud_administrador.crud_administrador import crud_administrador_app
from project.login.login import login_app
from project.registro_usuario.registro_usuario import registro_usuario_app

# Instancias del Blueprint
app.register_blueprint(geolocalizador_app)
app.register_blueprint(crud_administrador_app)
app.register_blueprint(login_app)
app.register_blueprint(registro_usuario_app)

@app.route('/api')
def index():
    return 'Server on'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def angular(path):
    return render_template('index.html')