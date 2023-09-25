import json 

from db_config import db


class User(db.Model):
    __tablename__ = 'users'
    username = db.Column(db.String(100), primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def json(self):
        return {'username': self.username, 'email': self.email}
    

    @staticmethod
    def get_all_users():
        response = [User.json(user) for user in User.query.all()]
        return response
    

    @staticmethod
    def get_user(_username):
        query = User.query.filter_by(username= _username).first()
        return query
    

    @staticmethod
    def add_user(_username, _email):
        news_user = User(username = _username, email = _email)
        db.session.add(news_user)
        db.session.commit()

    
    @staticmethod
    def update_user(_username, _email):
        user_to_update = User.query.filter_by(username = _username).first()
        user_to_update.email = _email
        db.session.commit()