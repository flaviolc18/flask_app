from flask import Flask
from blueprints.ads import ads_blueprint

def create_app(config_filename=None):
  app =  Flask("work_tool")
  if config_filename:
    app.config.from_pyfile(config_filename)

  app.register_blueprint(ads_blueprint)
  return app