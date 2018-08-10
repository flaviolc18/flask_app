from flask import (Blueprint, render_template, request, flash, redirect, url_for)
from db import db
from blueprints.ads_model import Ad, Rate

#create a blueprint
ads_blueprint = Blueprint('ads', __name__, template_folder='templates')


@ads_blueprint.route("/ads/new", methods=["GET", "POST"])
def new():
  if request.method == "POST":

    data = request.form.to_dict()

    #create the models
    rate = Rate(offensive=data['offen'], misleading=data['misl'], inappropriate=data['inap'])
    ad = Ad(company=data['comp'], service=data['serv'], subject=data['subj'])
    
    #set the relationship
    ad.rate = rate

    db.session.add(ad)
    db.session.add(rate)
    db.session.commit()

    flash("Successfully created Ad!")

    return redirect(url_for('ads.index'))
  else:
    return render_template('new_ad.html', title=u"Create a new Ad")

@ads_blueprint.route("/")
def index():
  all_ads = Ad.query.all()
  return render_template('index.html', all_ads=all_ads)