from db import db
from sqlalchemy.orm import Mapped

class AthleteModel(db.Model):
    __tablename__ = "dim_athlete"
    
    id: Mapped[int] = db.Column(db.Integer, primary_key=True)
    name: Mapped[str] = db.Column(db.String(80), unique=True, nullable=False)
    
    results = db.relationship("ResultModel", back_populates="athlete", lazy="dynamic", cascade="all, delete")