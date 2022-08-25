from app.dao.models.director_model import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did: int):
        return self.session.query(Director).get(did)

    def get_all(self):
        return self.session.query(Director).all()

    def create(self, data):
        director = Director(**data)
        self.session.add(director)
        self.session.commit()
        return director

    def update(self, director):
        self.session.add(director)
        self.session.commit()

    def delete(self, did):
        director = self.get_one(did)
        self.session.delete(director)
        self.session.commit()
