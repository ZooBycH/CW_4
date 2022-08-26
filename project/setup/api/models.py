from flask_restx import fields, Model


from project.setup.api import api


genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режиссер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Михалков'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Комедия'),
    'description': fields.String(required=True, example='Комедия'),
    'trailer': fields.String(required=True, example='Комедия'),
    'year': fields.Integer(),
    'rating': fields.Float(),
    'genre': fields.Nested(genre),
    'director': fields.Nested(director)
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=100, example='Комедия'),
    'password': fields.String(required=True, max_length=300, example='Комедия'),
    'name': fields.String(required=True, max_length=300, example='Комедия'),
    'surname': fields.String(required=True, max_length=300, example='Комедия'),
    'favourite_genre': fields.Integer(required=True, example=1)
})

favorite: Model = api.model('Избранное', {
    'user_id': fields.Integer(required=True, example=1),
    'movie_id': fields.Integer(required=True, example=1),
    'movies': fields.Nested(movie)
})

