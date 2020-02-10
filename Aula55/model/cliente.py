import sqlalchemy as db
from model.base import Base

class Cliente(Pessoa):
    __tablename__ = 'LIVRARIA_CLIENTE'
    endereco=db.Column(db.String(length=200))
    numero_documento=db.Column(db.String(length=50))
    telefone=db.Column(db.String(length=20))