from flask import (Blueprint, render_template, request, flash, redirect, url_for, make_response, session)
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

@ads_blueprint.route("/ads/show_all")
def show_all():
  all_ads = Ad.query.all()
  if all_ads:
    return render_template('show_all_ads.html', all_ads=all_ads)
  else:
    return render_template('show_all_ads.html', error_msg="No ads to show...")

@ads_blueprint.route("/ads", methods=["POST"])
def handler():
  if(request.method == "POST"):

    if(request.form['num_ads']):
      session['num_ads'] = request.form['num_ads']

    return render_template('find_ads.html')

@ads_blueprint.route("/")
def index():
  return render_template('index.html')