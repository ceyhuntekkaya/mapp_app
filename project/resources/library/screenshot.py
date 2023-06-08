from flask.views import MethodView
from flask_smorest import Blueprint, abort
from project.service.library.screenshot import ScreenshotService
from flask_jwt_extended import jwt_required
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException
from db import db
from project.schemas.library.screenshot import ScreenshotSchema

blp = Blueprint("Screenshots", "screenshots", description="Operations on screenshot")

main_route = "screenshot"


@blp.route(f"/{main_route}/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, ScreenshotSchema)
    def get(self, item_id):
        service = ScreenshotService(db.session)
        item = service.getById(item_id)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @jwt_required()
    def delete(self, item_id):
        service = ScreenshotService(db.session)
        item = service.delete(item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @blp.arguments(ScreenshotSchema)
    @blp.response(201, ScreenshotSchema)
    def put(self, item_data, item_id):
        service = ScreenshotService(db.session)
        item = service.update(item_data, item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item


@blp.route(f"/{main_route}")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, ScreenshotSchema(many=True))
    def get(self):
        service = ScreenshotService(db.session)
        return service.getAll()

    @jwt_required(fresh=True)
    @blp.arguments(ScreenshotSchema)
    @blp.response(201, ScreenshotSchema)
    def post(self, item_data):
        service = ScreenshotService(db.session)
        item = service.add(item_data, 1)
        if type(item) == UnexpectedEntityException:
            abort(409, message="Error: {}".format(item))
        return item
