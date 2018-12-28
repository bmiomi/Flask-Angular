#importaciones externas
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
#importaciones internas

#configuracion
from config import DevelopmentConfig

def apps():
    app=Flask(__name__)
    CORS(app)  # allows CORS for all domains n all routes
    return app

app=apps()

db=SQLAlchemy(app)
ma=Marshmallow(app)

app.config.from_object(DevelopmentConfig)
from apirutas.rutas import api_

app.register_blueprint(api_)


with app.app_context():
    db.create_all()  # metodo para crear tablas y la propia db
