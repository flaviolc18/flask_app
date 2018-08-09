from flask import Flask
from blueprints.ads import ads_blueprint

def create_app(mode):
  app =  Flask("work_tool")
  #default config file
  app.config.from_object("default_settings")
  #production/development config file
  app.config.from_pyfile("%s.cfg" % mode)

  app.register_blueprint(ads_blueprint)
  return app