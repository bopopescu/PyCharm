from dao.produto_dao import ProdutoDao
from model.produto_model import ProdutoModel

dao = ProdutoDao()
produtos = dao.list_all()
print(produtos)
for p in produtos:
    print(p)

