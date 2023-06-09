from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required 

from db import db
from models.library.screenshot import ScreenshotModel
from schemas.library.screenshot import ScreenshotSchema


blp = Blueprint("Screenshots", "screenshots", description="Operations on screenshot")


@blp.route("/screenshot/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, ScreenshotSchema)
    def get(self, item_id):
        item = ScreenshotModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = ScreenshotModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Screenshot deleted"}, 200

     
    @blp.arguments(ScreenshotSchema)
    @blp.response(201, ScreenshotSchema)
    def put(self, item_data, item_id):
        item = ScreenshotModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = ScreenshotModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item

@blp.route("/screenshot")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, ScreenshotSchema(many=True))
    def get(self):
        return ScreenshotModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(ScreenshotSchema)
    @blp.response(201, ScreenshotSchema)
    def post(self, item_data):
        item = ScreenshotModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A screenshot with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the screenshot.")

        return item
    
