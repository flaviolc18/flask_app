from flask import (Blueprint, render_template, request)

from db import get_table

ads_blueprint = Blueprint('ads', __name__, template_folder='templates')

@ads_blueprint.route("/ads/create", methods=["GET", "POST"])
def create():
  if request.method == "POST":
    ads_table = get_table('ads') 
    
    data = request.form.to_dict()

    id_new_ad = ads_table.insert(data)

    return render_template('ad_created.html', title=u"Ad created successfully", id_new_ad=id_new_ad)
  else:
    return render_template('create_ad.html', title=u"Create a new Ad")

@ads_blueprint.route("/")
def index():
  ads_table = get_table('ads') 

  if(ads_table):
    return render_template('index.html', title=u"All ads", ads=ads_table)
  else:
    return render_template('index.html', title=u"All ads")