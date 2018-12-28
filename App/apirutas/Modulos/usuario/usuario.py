from flask import request
from flask_restful import Resource

from main import db
from apirutas.base.model import usuario ,Usuario_
 
Usuario_schema = Usuario_(many=True)#ies
usuario_schema = Usuario_() #y

class ResourceUsuario(Resource):

    def get(self):
        M_usuario = usuario.query.all()
        M_usuario = Usuario_schema.dump(M_usuario).data
        return {'status': 'success', 'data': M_usuario}, 200

    def post(self):
        json_data = request.get_json(force=True)
        print(json_data)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = usuario_schema.load(json_data)
        if errors:
            return errors, 422
        M_usuario = usuario.query.filter_by(nombre=data['nombre']).first()
        if M_usuario:
            return {'message': 'Usuario already exists'}, 400
        M_usuario = usuario(
            nombre=json_data['nombre'],
            usuario=json_data['usuario']
            )
        db.session.add(M_usuario)
        db.session.commit()
        result = usuario_schema.dump(M_usuario).data
        return { "status": 'success', 'data': result }, 201

    def put(self):

        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = Usuario_.load(json_data)
        if errors:
            return errors, 422
        M_usuario = usuario.query.filter_by(id=data['id']).first()
        if not M_usuario:
            return {'message': 'Category does not exist'}, 400
        M_usuario.name = data['name']
        db.session.commit()
        result = Usuario_.dump(M_usuario).data
        return { "status": 'success', 'data': result }, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = Usuario_.load(json_data)
        if errors:
            return errors, 422
        M_usuario = usuario.query.filter_by(id=data['id']).delete()
        db.session.commit()
        result = Usuario_.dump(M_usuario).data
        return { "status": 'success', 'data': result}, 204