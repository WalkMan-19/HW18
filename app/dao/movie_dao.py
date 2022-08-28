from app.dao.models.movie_model import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid: int):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        return self.session.query(Movie).all()

    def filter_data(self, **params):
        if params.get("director_id"):
            return self.session.query(Movie).filter(Movie.director_id == params.get("director_id"))
        if params.get("genre_id"):
            return self.session.query(Movie).filter(Movie.genre_id == params.get("genre_id"))
        if params.get("year"):
            return self.session.query(Movie).filter(Movie.year == params.get("year"))

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()
