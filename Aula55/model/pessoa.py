import sqlalchemy as db
from model.base import Base
class Pessoa(Base):
    id=db.Column(db.Integer)
    nome=db.Column(db.String(length=100))
    sobrenome=db.Column(db.String(length=100))
    data_nascimento=db.Column(db.Date)
    naturalidade = db.Column(db.String(length=100))