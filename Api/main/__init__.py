import os
import dotenv
from flask import Flask
from dotenv import load_dotenv

#importo el modulo para crear la api-rest
from flask_restful import Api

api = Api()

def create_app():
    app = Flask(__name__)

    load_dotenv()

    import main.resources as resources
    api.add_resource(resources.ClienteResource,'/clientes')

    api.init_app(app)
    return app
