from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import EventModel
from schemas import EventSchema

blp = Blueprint("events", __name__, description="Operations on events")

@blp.route("/event/<int:id>")
class Event(MethodView):
    @blp.response(200, EventSchema)
    def get(self, id):
        event = EventModel.query.get_or_404(id)
        return event
    
    def delete(self, id):
        event = EventModel.query.get_or_404(id)
        
        try:
            db.session.delete(event)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Could not delete event.")
            
        return {"message": f"Event '{event.name}' deleted."}
    
    
@blp.route("/event")
class EventList(MethodView):
    @blp.response(200, EventSchema(many=True))
    def get(self):
        return EventModel.query.all()
    
    @blp.arguments(EventSchema)
    @blp.response(200, EventSchema)
    def post(self, event_data):
        event = EventModel(**event_data)
        
        try:
            db.session.add(event) # Add data that we want to commit to database
            db.session.commit() # Commit all added items
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting an event.")
        
        return event