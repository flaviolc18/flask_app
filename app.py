from flask import Flask
from blueprints.ads import ads_blueprints

def create_app(config_file=None):
  app =  Flask("work_tool")
  if config_filename:
    app.config.from_py_file(config_filename)

  app.register_blueprint(ads_blueprints)
  return app