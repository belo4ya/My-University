from flask import Flask

DATABASE = {
    'name': 'dev.db',
    'engine': 'peewee.SqliteDatabase',
}
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


def register_blueprints():
    from my_app.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')


def create_tables():
    from my_app.models import db, User
    db.database.create_tables([User], fail_silently=True)
