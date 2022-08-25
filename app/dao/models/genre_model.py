from app.database import db
from marshmallow import Schema, fields


class Genre(db.Model):
    __teblename__ = 'genre'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()
