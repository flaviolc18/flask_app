from flask import render_template
from flask_appbuilder import ModelView
from flask_appbuilder.models.mongoengine.interface import MongoEngineInterface
from app import appbuilder

@app.route('/')
def index():
  return render_template("index.html", name="test user")


@app.route('/handlead', methods=["GET", "POST"])
def handlead():
  if request.method == "POST":
    comp = request.form['comp']
    serv = request.form['serv']
    if comp and serv:
      #invés de comp e serv, teremos objetos ad
      return render_template("main.html", comp=comp, serv=serv)
    else:
      return render_template("main.html", error_msg="Fill all the the form")
  return render_template("main.html")


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

