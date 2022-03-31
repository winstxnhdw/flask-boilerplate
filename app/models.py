from app import db

class Model(db.Model):
    
    __tablename__ = 'Model'
    id = db.Column(db.Integer, primary_key=True)