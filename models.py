from flask_login import UserMixin
from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(255), nullable=True, unique=True)
    password_hash = db.Column(db.String(128))
    image = db.Column(db.LargeBinary, nullable=True)
    caption = db.Column(db.String(1000), nullable=True)
    follow_count = db.Column(db.Integer, nullable=True, default=0) #フォローの数
    follower_count = db.Column(db.Integer, nullable=True, default=0) #フォロワーの数
    randaction_count = db.Column(db.Integer, nullable=True, default=0) #投稿の数

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(1000), nullable=True)
    image_data = db.Column(db.LargeBinary, nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, default=1)
    fav_count = db.Column(db.Integer, nullable=True, default=0) #いいねの数
    mission_title = db.Column(db.String(1000), nullable=True)
    # mission = db.relationship('Mission', backref=db.backref('posts', lazy='dynamic'))



    def to_dict(self):
        return {
            'caption' : self.caption,
            'image_data' : self.image_data,
            'created_at' : self.created_at,
            'mission_title' : self.mission.title if self.mission else None,
            'fav_count':self.fav_count,  #いいね数（db未実装）
        }

class Favorite(db.Model):
    __tablename__ = "favorites"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, default=1)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False, default=1)
    created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())


class Mission(db.Model):
    __tablename__ = "missions"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(225), nullable=False, default="ミッション")
    # content = db.Column(db.String(1000), nullable=True) #missionの詳細ページを作成するなら必要。nullでもOK
    count = db.Column(db.Integer, nullable=False, default=0)
    start_time = db.Column(db.DateTime, nullable=True) #Pythonのコードで日本のDateTimeに直してからデータベースに格納すること
    end_time = db.Column(db.DateTime, nullable=True) #Pythonのコードで日本のDateTimeに直してからデータベースに格納すること

class Follow(db.Model):
    __tablename__ = "follows"
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    followed_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())

