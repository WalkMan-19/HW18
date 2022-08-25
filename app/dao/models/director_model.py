from app.database import db
from marshmallow import Schema, fields


class Director(db.Model):
    __teblename__ = 'director'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
