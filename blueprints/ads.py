from flask import (Blueprint, render_template, request)

from db import ads_table

ads_blueprint = Blueprint('ads', __name__, template_folder='templates')

@ads_blueprint.route("/ads/create", methods=["GET", "POST"])
def create():
  if request.method == "POST":
    return render_template('ad_created.html', title=u"Ad created successfully")
  else:
    return render_template('create_ad.html', title=u"Create a new Ad")

@ads_blueprint.route("/")
def index():
  #all_ads = ads_table.all()
  return render_template('index.html', title=u"All ads") 