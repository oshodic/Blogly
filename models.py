"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"


def connect_db(app):
  """Connect to database"""

  db.app = app
  db.init_app(app)

class User(db.Model):
  """Blogly Users"""

  ___tablename___ = "users"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  first_name = db.Column(db.String(50), nullable=False)
  last_name = db.Column(db.String(50), nullable=False)                
  img_url = db.Column(db.Text, default=DEFAULT_IMAGE_URL, nullable=False)

  def __repr__(self):
    """"show info about user"""
    u = self
    return f"User {u.id} {u.first_name} {u.last_name} {u.img_url}"


def connect_db(app):
  db.app = app
  db.init_app(app)