import os
import dotenv
from flask import Flask
from dotenv import load_dotenv

#importo el modulo para crear la api-rest
from flask_restful import Api
#importar el modulo para conectarse a una BD
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

api = Api()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    load_dotenv()

    # Cargar variables de entorno
    PATH = os.getenv("DATABASE_PATH")
    DB_NAME =os.getenv("DATABASE_NAME")

    if not os.path.exists(f'{PATH}{DB_NAME}'):
        os.chdir(f'{PATH}')
        file = os.open(f'{DB_NAME}',os.O_CREAT)
    
    #INICIALIZAR LA APP DB
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{PATH}{DB_NAME}'
    db.init_app(app)


    import main.resources as resources
    api.add_resource(resources.ClientesResource,'/clientes')
    api.add_resource(resources.ClienteResource,'/cliente/<id>')
    api.add_resource(resources.UsuariosResource,'/usuarios')
    api.add_resource(resources.UsuarioResource,'/usuario/<id>')

    api.init_app(app)
    return app
