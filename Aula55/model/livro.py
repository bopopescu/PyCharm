from model.autor import Autor
from model.editora import Editora
from model.genero import Genero
import sqlalchemy as db
from sqlalchemy.orm import relationship

class Livro(Base):
    id = db.Column(db.Integer, primary_key=True)
    titulo=db.Column(db.String(length=100))
    sinopse=db.Column(db.String(length=100))
    data_primeira_pubicacao=db.Column(db.DATE)
    autor_id=db.Column(db.Integer, db.ForeignKey('LIVRARIA_AUTOR.ID'))
    autor=relationship(Autor)
    editora_id=db.Column(db.Integer, db.ForeignKey())
    Editora = relationship(Editora)
    genero_id=db.Column(db.Integer, db.ForeignKey())
    genero = relationship(Genero)