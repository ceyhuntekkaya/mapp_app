from marshmallow import Schema, fields


class PlainMarkerSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    type = fields.Str()
    color = fields.Str()
    sensor_id = fields.Int()
    sign_id = fields.Int()
    symbol_id = fields.Int()
    unit_id = fields.Int()
    description = fields.Str()
    latitude = fields.Float()
    longitude = fields.Float()
    layer_id = fields.Int()
    area_id = fields.Int()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    created_at = fields.Str()


class MarkerSchema(PlainMarkerSchema):
    updated_at = fields.Str()
    deleted_at = fields.Str()
    status = fields.Int()
    created_by = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class MarkerUpdateSchema(PlainMarkerSchema):
    updated_by = fields.Int()
    status = fields.Int()


class MarkerDeleteSchema(Schema):
    id = fields.Int()
    deleted_by = fields.Int()


class MarkerCreateSchema(PlainMarkerSchema):
    created_by = fields.Int()
    status = fields.Int()
