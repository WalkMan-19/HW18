from app.dao.movie_dao import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid: int):
        return self.dao.get_one(mid)

    def get_all(self, params):
        if params != {}:
            return self.dao.filter_data(**params)
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        mid = data.get("id")
        movie = self.dao.get_one(mid)

        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")

        self.dao.update(movie)

    def update_partial(self, data):
        mid = data.get("id")
        movie = self.dao.get_one(mid)

        if "title" in data:
            movie.title = data.get("title")
        if "description" in data:
            movie.description = data.get("description")
        if "trailer" in data:
            movie.trailer = data.get("trailer")
        if "year" in data:
            movie.year = data.get("year")
        if "rating" in data:
            movie.rating = data.get("rating")

        self.dao.update(movie)

    def delete(self, mid):
        self.dao.delete(mid)
