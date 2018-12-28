from flask_restful import Resource 

class prueva (Resource):

    def get(self):
        return {"mensaje Gt": "respuesta=>,ola"}
        
    def post (self):
        return{"mensaje,Ps":"respueata => ola ola"}

