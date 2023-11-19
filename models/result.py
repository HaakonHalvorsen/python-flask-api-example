from db import db
from sqlalchemy.orm import Mapped

class ResultModel(db.Model):
    __tablename__ = "fact_result"
    
    athlete_id: Mapped[int] = db.Column(db.Integer, db.ForeignKey("dim_athlete.id"), primary_key=True)
    event_id: Mapped[int] = db.Column(db.Integer, db.ForeignKey("dim_event.id"), primary_key=True)
    rank: Mapped[int] = db.Column(db.Integer)
    
    event = db.relationship("EventModel", back_populates="results")
    athlete = db.relationship("AthleteModel", back_populates="results")
    
    