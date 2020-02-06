from dao.base_dao import BaseDao
from model.produto_model import ProdutoModel


class ProdutoDao(BaseDao):
    def list_all(self):
        return self.sessao.query(ProdutoModel).all()