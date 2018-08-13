from db import db

class Ad(db.Model):

  __tablename__ = 'ads'

  id = db.Column(db.Integer, primary_key=True)
  company = db.Column(db.String(50))
  service = db.Column(db.String(50))
  subject = db.Column(db.String(100))
  rate_id = db.Column(db.Integer, db.ForeignKey("rates.id"))
  rate = db.relationship("Rate")

  def serialize(self):
    return {
    "id": self.id,
    "company": self.company,
    "service": self.service,
    "rate_id": self.rate_id,
    "rate": self.rate.serialize()
    }


class Rate(db.Model):

  __tablename__ = 'rates'

  id = db.Column(db.Integer, primary_key=True)
  offensive = db.Column(db.String(20))
  misleading = db.Column(db.String(20))
  inappropriate = db.Column(db.String(20))
  overall = db.Column(db.String(20))
  '''
  reason = db.Column(db.String(500))
  explaining = db.Column(db.String(500))
  addition = db.Column(db.String(500))
  '''
  comment = db.Column(db.String(1000))

  def serialize(self):
    return {
    "id": self.id,
    "offensive": self.offensive,
    "misleading": self.misleading,
    "inappropriate": self.inappropriate,
    "overall": self.overall,
    '''
    "reason": self.reason,
    "explaining": self.explaining,
    "addition": self.addition,
    '''
    "comment": self.comment
    }
