from dao.editora_dao import EditoraDao
from model.editora import Editora

editora = Editora()
editora.nome = "Novatec"

dao = EditoraDao()
dao.insert(editora)

for m in dao.list_all():
    print(m)