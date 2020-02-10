import sqlalchemy as db
from model.pessoa import Pessoa

class Autor(Pessoa):
    __tablename__ = 'LIVRARIA_AUTOR'
    pseudonimo=db.Column(db.String(length=200))
    descricao=db.Column(db.String(length=200))
