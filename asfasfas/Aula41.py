from flask import Flask
from flask_restful import Api
from Controllers.pessoa_controller import PessoaController

app = Flask(__name__)
api = Api(app)

api.add_resource(PessoaController, '/api/pessoa', endpoint='pessoas')
api.add_resource(PessoaController, '/api/pessoa/<int:id>', endpoint='pessoa')


@app.route('/')
def inicio():
    return 'Bem vindo a Controller'

app.run(debug=True, port=80)