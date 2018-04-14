from flask_sqlalchemy import SQLAlchemy

# database
db = SQLAlchemy()

class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.String(100), nullable=False)
    comment_user = db.Column(db.String(200))
    comment_rating = db.Column(db.Integer)
    comment_content = db.Column(db.Text)
    comment_time = db.Column(db.String(100))
