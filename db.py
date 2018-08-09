from os import path
from flask import current_app
import dataset

def get_table(tablename):
  db_name = current_app.config['DATABASE_NAME']
  db_path = path.join(current_app.config['PROJECT_ROOT'], db_name)
  db = dataset.connect('sqlite:///{0}'.format(db_path))
  return db[tablename]