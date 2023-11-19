from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import AthleteModel
from schemas import AthleteSchema

blp = Blueprint("athletes", __name__, description="Operations on athletes")

@blp.route("/athlete/<int:id>")
class Athlete(MethodView):
    @blp.response(200, AthleteSchema)
    def get(self, id):
        athlete = AthleteModel.query.get_or_404(id)
        return athlete
    
    def delete(self, id):
        athlete = AthleteModel.query.get_or_404(id)
        
        try:
            db.session.delete(athlete)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Could not delete athlete.")
            
        return {"message": f"Athlete '{athlete.name}' deleted."}
    
    
@blp.route("/athlete")
class AthleteList(MethodView):
    @blp.response(200, AthleteSchema(many=True))
    def get(self):
        return AthleteModel.query.all()
    
    @blp.arguments(AthleteSchema)
    @blp.response(200, AthleteSchema)
    def post(self, athlete_data):
        athlete = AthleteModel(**athlete_data) # Make athlete with data in body (only name in this case)
        
        try:
            db.session.add(athlete) # Add data that we want to commit to database
            db.session.commit() # Commit all added items
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting an athlete.")
        
        return athlete
            
        
    