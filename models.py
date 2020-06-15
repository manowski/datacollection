import datetime
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://user:password@localhost:5432/database"
db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)
migrate.init_app(app)
CORS(app)


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    sec_uid = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.BIGINT(), nullable=False, unique=True)
    name = db.Column(db.String(), nullable=False)
    full_name = db.Column(db.String())
    signature = db.Column(db.String())
    cover = db.Column(db.String())
    cover_medium = db.Column(db.String())
    country = db.Column(db.String())
    verified = db.Column(db.Boolean())
    following = db.Column(db.BIGINT())
    fans = db.Column(db.BIGINT())
    hearts = db.Column(db.BIGINT())
    video_count = db.Column(db.Integer())
    digg = db.Column(db.BIGINT())
    stats = db.relationship('StatsForUser', backref='days', lazy='dynamic')

    created_date = db.Column(db.DateTime, default=datetime.datetime.now)
    updated = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return f"<User {self.name}>"

    def __init__(self, **kwargs):
        super(UserModel, self).__init__(**kwargs)


class StatsForUser(db.Model):
    __tablename__ = 'statsforuser'
    id = db.Column(db.BIGINT(), primary_key=True)
    user_id = db.Column(db.BIGINT(), db.ForeignKey('users.user_id'))
    signature = db.Column(db.String())
    cover = db.Column(db.String())
    cover_medium = db.Column(db.String())
    following = db.Column(db.BIGINT())
    fans = db.Column(db.BIGINT())
    hearts = db.Column(db.BIGINT())
    video_count = db.Column(db.Integer())
    digg = db.Column(db.BIGINT())
    updated_date = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return f"<User {self.user_id}>"

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "following": self.following,
            "hearts": self.hearts,
            "fans": self.fans,
            "video_count": self.video_count,
            "digg": self.digg,
            "updated_date": self.updated_date,
        }

