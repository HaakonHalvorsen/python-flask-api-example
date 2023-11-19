from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import ResultModel
from schemas import ResultSchema

blp = Blueprint("results", __name__, description="Operations on results")

@blp.route("/event/<int:event_id>/athlete/<int:athlete_id>")
class Result(MethodView):
    @blp.response(200, ResultSchema)
    def get(self, event_id, athlete_id):
        result = ResultModel.query.get_or_404(event_id, athlete_id)
        return result
    
    def delete(self, event_id, athlete_id):
        result = ResultModel.query.get_or_404(event_id, athlete_id)
        
        try:
            db.session.delete(result)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Could not delete result.")
            
        return {"message": f"Result deleted."}
    
    
@blp.route("/result")
class ResultList(MethodView):
    @blp.response(200, ResultSchema(many=True))
    def get(self):
        return ResultModel.query.all()
    
    @blp.arguments(ResultSchema)
    @blp.response(200, ResultSchema)
    def post(self, result_data):
        result = ResultModel(**result_data)
        
        try:
            db.session.add(result)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting a result.")
        
        return result