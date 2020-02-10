import sqlalchemy  as db
from sqlalchemy.orm.session import sessionmaker, query
class BaseDao:
    def __init__(self, table):
        self.table = table
        engine = db.create_engine("mysql+mysqlconnector://topkills01:ts2019@mysql.topskills.dev:3306/topskills01")
        session_mk = sessionmaker()
        session_mk.configure(bind=engine)
        self.session = session_mk()

    def list_all(self):
        list_model = self.session.query(self.table).all()
        return list_model
    def get_by_id(self,id):
        model=self.session.query(self.table).filter_by(id=id).one()
        return model
    def insert(self, model):
        self.session.add(model)
        self.session.commit()
        return f"objeto inserido com sucesso! objeto :{model.id}"

    def update(self, model):
        self.session.merge(model)
        self.session.commit()
        return f"objeto alterado com sucesso! objeto :{model}"

    def delete(self, id):
        model = self.session.query(self.get_by_id(id))
        return f"objeto deletado com sucesso!"