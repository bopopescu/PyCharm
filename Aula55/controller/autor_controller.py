from controller.base_controller import BaseController
from model.autor import Autor
from dao.autor_dao import AutorDao

class AutorController(BaseController):
    def __init__(self):
        dao = AutorDao()
        super().__init__(dao)