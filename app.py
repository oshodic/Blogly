"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

@app.route("/")
def homepage():
  """shows homepage w/ list of all users"""

  users = User.query.order_by(User.last_name, User.first_name).all()

  return render_template("base.html", users=users)

@app.route("/user_form", methods=["GET"])
def user_form():
  """show form to add new user"""

  return render_template("user_form.html")

@app.route("/user_form", methods=["POST"])
def add_user():
  """handle user form"""

  first_name = request.form['first_name']
  last_name = request.form['last name']
  img_url = request.form['profile pic']

  user = User(first_name=first_name, last_name=last_name, img_url=img_url)
  db.session.add(user)
  db.session.commit()

  return redirect("/")

@app.route("/users/<int:user_id>")
def show_user(user_id):
  """shows user profile"""
  
  user = User.query.get_or_404(user_id)
  return render_template('/show_user.html', user=user)

@app.route("/users/<int:user_id>/edit", methods=["POST"])
def edit_user(user_id):
  """handles user info edit"""

  user = User.query.get_or_404(user_id)
  user.first_name = request.form['first_name']
  user.last_name = request.form['last name']
  user.img_url = request.form['profile pic']

  db.session.add(user)
  db.session.commit()

  return redirect("/")

@app.route("/users/<int:user_id>/edit", methods=["GET"])
def edit_user_get(user_id):
  """handles user info edit"""

  user = User.query.get_or_404(user_id)

  return render_template("edit_user.html", user=user)

@app.route("/users/<int:user_id>/delete")
def delete_user(user_id):
  """delete user profile"""

  user = User.query.get_or_404(user_id)
  db.session.delete(user)
  db.session.commit()

  return redirect("/")


