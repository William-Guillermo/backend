from flask_restful import Resource
from flask import jsonify

clientes = [
    {
    "id":1,
    "nombre":"William",
    "apellido":"Guillermo"
    },
       {
    "id":2,
    "nombre":"Romario",
    "apellido":"Guillermo"
    }

]

#crear recurso se vana a trabajar  Get, post, delete, Put(editar)

class Clientes(Resource):
    def get(self):

            return jsonify(
                {
                    "clientes":clientes
                }

            )
