from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required 

from db import db
from models.detection.detection_process import DetectionProcessModel
from schemas.detection.detection_process import DetectionProcessSchema


blp = Blueprint("DetectionProcesss", "detection_processs", description="Operations on detection process")


@blp.route("/detection_process/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, DetectionProcessSchema)
    def get(self, item_id):
        item = DetectionProcessModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = DetectionProcessModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Detection process deleted"}, 200

     
    @blp.arguments(DetectionProcessSchema)
    @blp.response(201, DetectionProcessSchema)
    def put(self, item_data, item_id):
        item = DetectionProcessModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = DetectionProcessModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item

@blp.route("/detection_process")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, DetectionProcessSchema(many=True))
    def get(self):
        return DetectionProcessModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(DetectionProcessSchema)
    @blp.response(201, DetectionProcessSchema)
    def post(self, item_data):
        item = DetectionProcessModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A detection process with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the detection process.")

        return item
    
