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
  img_url = db.Column(db.Text, default=DEFAULT_IMAGE_URL)

def connect_db(app):
  db.app = app
  db.init_app(app)