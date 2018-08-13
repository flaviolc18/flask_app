import os
from flask import Flask
from blueprints.ads_view import ads_blueprint
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_scss import Scss
from db import db



def create_app():
  app =  Flask("work_tool")
 
  app.config['PROJECT_ROOT'] = os.path.abspath(os.path.dirname(__file__))
  app.config['MEDIA_ROOT'] = os.path.join(app.config['PROJECT_ROOT'], 'media_files')
  app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///worktool.sqlite3"
  app.config['SQLALCHEMY_ECHO'] = True
  app.config['SECRET_KEY'] = "jkh-*sd45-+5647*-/5434"

  app.register_blueprint(ads_blueprint)

  db.init_app(app)
  Migrate(app, db)

  Bootstrap(app)

  Scss(app, static_dir='static', asset_dir='assets/scss/')

  @app.before_first_request
  def create_tables():
      from blueprints.ads_model import Ad, Rate
      db.create_all()
  
  return app