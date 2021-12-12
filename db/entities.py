from flask_sqlalchemy import SQLAlchemy

# Initialise the ORM.
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, db.Identity(always=False, start=1, cycle=False), primary_key=True)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f"User(id={self.id!r}, user_name={self.user_name!r})"

class Data(db.Model):
    __tablename__ = 'data'

    id = db.Column(db.Integer, db.Identity(always=False, start=1, cycle=False), primary_key=True)
    userId = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    body = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return super().__repr__()
