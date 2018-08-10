from db import db

class Ad(db.Model):

  __tablename__ = 'ads'

  id = db.Column(db.Integer, primary_key=True)
  company = db.Column(db.String(50))
  service = db.Column(db.String(50))
  subject = db.Column(db.String(100))
  rate_id = db.Column(db.Integer, db.ForeignKey("rates.id"))
  rate = db.relationship("Rate")

'''
  __init__(self, comp, serv, subj):
    self.company = comp
    self.service = serv
    self.subject = subj
'''

class Rate(db.Model):

  __tablename__ = 'rates'

  id = db.Column(db.Integer, primary_key=True)
  offensive = db.Column(db.String(20))
  misleading = db.Column(db.String(20))
  inappropriate = db.Column(db.String(20))
  overall = db.Column(db.String(20))
  reason = db.Column(db.String(500))
  explaining = db.Column(db.String(500))
  addition = db.Column(db.String(500))
  comment = db.Column(db.String(500))

'''
  __init__(self, offensive, misleading, inappropriate, overall, reason, explaining, addition, comment):
    self.offensive = None
    self.misleading = None
    self.inappropriate = None
    self.overall = None
    self.reason = None
    self.explaining = None
    self.addition = None
    self.comment = None
'''