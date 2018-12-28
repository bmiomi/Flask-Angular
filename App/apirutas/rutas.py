from flask import jsonify, request,Blueprint
from flask_restful import Api
#modelo 
from main import db
from .base.model import pato
from .base.model import Usuario_,Entidad_,usuario,entidad
#respuesta json 
from .Modulos.usuario.restfull import prueva
from .Modulos.usuario.usuario import ResourceUsuario

api_=Blueprint('api',__name__,url_prefix='/api')

api=Api(api_)

#agregar ruta
api.add_resource(prueva,'/restfull')
api.add_resource(ResourceUsuario,'/Usuario')



@api_.route('/api/Users',methods=['POST'])
def add_user():
    dbadduser=usuario(
        nombre=request.json['nombre'],
        usuario=request.usuario['usuario']
    )
#    agregar usuarios a la db.
    db.add(dbadduser)
    db.commit()
    return jsonify(dbadduser)


"""
@api_.route('/exam')
def get_things():

    thing_objects = session.query(Thing).all()

    # transforming into JSON-serializable objects
    schema = ThingSchema(many=True)
    things = schema.dump(thing_objects)
    # serializing as JSON
    session.close()
    return jsonify(things.data)


@api_.route('/exam', methods=['POST'])
def add_thing():
    # mount thing object
    posted_thing = ThingSchema(only=('title','description')).load(request.get_json())
    thing = Thing(**posted_thing.data,created_by="HTTP post request")

    # persist thing
    db.session.add(thing)
    db.session.commit()

    # return created thing
    new_thing = ThingSchema().dump(thing).data
    db.close()
    return jsonify(new_thing), 201

"""
