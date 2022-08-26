from flask import Flask
from flask_restx import Api
from app.config import Config
from app.database import db
from app.dao.models.movie_model import Movie
from app.dao.models.director_model import Director
from app.dao.models.genre_model import Genre
from app.views.movie_views import movie_ns
from app.views.director_views import director_ns
from app.views.genre_views import genre_ns


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


def load_data():

    m1 = Movie(id=1,
               title="Джентльмены",
               description="Талантливый выпускник Оксфорда, применив свой уникальный ум и невиданную дерзость, придумал нелегальную схему обогащения с использованием поместья обедневшей английской аристократии. Однако когда он решает продать свой бизнес влиятельному клану миллиардеров из США, на его пути встают не менее обаятельные, но жесткие джентльмены. Намечается обмен любезностями, который точно не обойдется без перестрелок и парочки несчастных случаев",
               trailer="https://www.youtube.com/watch?v=dABPCMxu074",
               year=2020,
               rating=8.5,
               genre_id=1,
               director_id=1)

    m2 = Movie(id=2,
               title="Лицо со шрамом",
               description="Весной 1980 года был открыт порт Мэйриэл Харбор, и тысячи кубинских беженцев ринулись в Соединенные Штаты на поиски Американской Мечты. Один из них нашел ее на залитых солнцем улицах Майами. Богатство, власть и страсть превзошли даже самые невероятные его мечты. Его звали Тони Монтана. Мир запомнил его под другим именем — «Лицо со шрамом»…",
               trailer="https://www.youtube.com/watch?v=mU0DdjbF8IQ",
               year=1983,
               rating=8.3,
               genre_id=1,
               director_id=2)

    m3 = Movie(id=3,
               title="Шерлок Холмс",
               description="Величайший в истории сыщик Шерлок Холмс вместе со своим верным соратником Ватсоном вступают в схватку, требующую нешуточной физической и умственной подготовки, ведь их враг представляет угрозу для всего Лондона.",
               trailer="https://www.youtube.com/watch?v=4Q6f-ZqggYI",
               year=2009,
               rating=8.1,
               genre_id=2,
               director_id=1)

    d1 = Director(id=1, name="Гай Ричи")
    d2 = Director(id=2, name="Брайан Де Пальма")

    g1 = Genre(id=1, name="криминал")
    g2 = Genre(id=2, name="детектив")

    db.create_all()

    with db.session.begin():
        db.session.add_all([m1, m2, m3])
        db.session.add_all([d1, d2])
        db.session.add_all([g1, g2])


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    load_data()
    app.run()
