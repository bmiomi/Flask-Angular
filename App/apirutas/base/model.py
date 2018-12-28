
#Engine = create_engine('sqlite:///'+ os.path.abspath(os.getcwd())+'foo.db')

from datetime import datetime
from marshmallow import Schema,fields
import os 

from main import db
from main import ma

class pato():
    pass

## SQLAlchemy
## estructura de la base de datos 
class entidad(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    created_at =db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    last_updated_by = db.Column(db.String(20))

    def __init__(self, created_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by

class usuario(db.Model):
    
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(20))
    usuario=db.Column(db.String(20))


##MARSHMALLOW

class Entidad_(ma.Schema):
    
    id=fields.Integer(dump_only=True)
    created_at=fields.DateTime(),
    Updated_at=fields.DateTime(),
    last_update_by=fields.String()

class Usuario_(ma.Schema):
    
    id=fields.Integer(dump_only=True)
    nombre=fields.String()
    usuario=fields.String()

    