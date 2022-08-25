from app.database import db
from app.dao.movie_dao import MovieDAO
from app.service.movie_service import MovieService
from app.dao.director_dao import DirectorDAO
from app.service.director_service import DirectorService
from app.dao.genre_dao import GenreDAO
from app.service.genre_service import GenreService

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)
