from flask import (Blueprint, render_template, request, flash, redirect, url_for, make_response, session, jsonify)
from db import db
from blueprints.ads_model import Ad, Rate
from bot.bot import Bot

#create a blueprint
ads_blueprint = Blueprint('ads', __name__, template_folder='templates')

@ads_blueprint.route("/ads", methods=["POST", "GET"])
def handler():
  if(request.method == "POST"):

    if("num_ads" in request.form):
      session['num_ads'] = request.form['num_ads']
      session['num_made_ads'] = 0

    return render_template('find_ads.html')
  else:
    return render_template('find_ads.html')

@ads_blueprint.route("/ads/new", methods=["GET", "POST"])
def new():
  if request.method == "POST":

    data = request.form.to_dict()

    #create the models
    rate = Rate(offensive=data['offen'], misleading=data['misl'], inappropriate=data['inap'], comment=data['comment'])
    ad = Ad(company=data['comp'], service=data['serv'])
    
    #set the relationship
    ad.rate = rate

    db.session.add(ad)
    db.session.add(rate)
    db.session.commit()

    flash("Successfully created Ad!")

    return redirect(url_for('ads.index'))
  else:
    threeRate = {"1":"not at all", "2":"somewhat", "3":"very"}
    fiveRate = {"1":"definitely should not see", "2":"maybe should not see", "3":"not sure if people should or should not see", "4":"maybe should see", "5":"definitely should see"}
    return render_template('new_ad.html', threeRate=threeRate, fiveRate=fiveRate)

@ads_blueprint.route("/ads/show_all")
def show_all():
  if(request.args.get('option') == "get_ads"):

    all_ads = Ad.query.filter(Ad.company.like("%"+request.args.get('comp')+"%"), Ad.service.like("%"+request.args.get('serv')+"%"), Rate.comment.like("%"+request.args.get('key')+"%")).all()

    session["comp"] = request.args.get('comp')
    session["serv"] = request.args.get('serv')

    return jsonify([a.serialize() for a in all_ads])
  else:

    all_ads = Ad.query.all()
    if all_ads:
      return render_template('show_all_ads.html', all_ads=all_ads)
    else:
      return render_template('show_all_ads.html', error_msg="No ads to show...")

@ads_blueprint.route("/ads/show")
def show():
  if("ad_id" in request.args):

    ad = Ad.query.filter_by(id=request.args['ad_id']).first()

    bot = Bot()
    if(bot.get_ready()):

      bot.send_msg(ad.rate.comment)
      flash("Message sent successfully!")
      session['num_made_ads'] += 1
    else:
      flash("Fail send message, start the bot in the Telegram chat...")

    #here I must show all ad properties
    return render_template("show_ad.html", id_ad_selected=request.args['ad_id'])
  else:
    return render_template("show_ad.html")

@ads_blueprint.route("/ads/next")
def next():
  session['comp'] = ""
  session['serv'] = ""
  #setar depois no login para nao ter possibilidade de acesso sem estar setada
  session['num_made_ads'] += 1
  return redirect(url_for('ads.handler'))


@ads_blueprint.route("/")
def index():
  return render_template('index.html')