from marshmallow import Schema, fields


class PlainAnomalyRouteSchema(Schema):
    id = fields.Int()
    anomaly_id = fields.Int()
    latitude = fields.Float()
    longitude = fields.Int()
    description = fields.Str()
    anomaly_at = fields.Int()
    anomaly_level = fields.Int()


class AnomalyRouteSchema(PlainAnomalyRouteSchema):
    created_at = fields.Str()
    deleted_at = fields.Str()
    deleted_by = fields.Int()


class AnomalyRouteUpdateSchema(Schema):
    id = fields.Int()
    anomaly_id = fields.Int()
    latitude = fields.Float()
    longitude = fields.Int()
    description = fields.Str()
    anomaly_at = fields.Int()
    anomaly_level = fields.Int()


class AnomalyRouteDeleteSchema(PlainAnomalyRouteSchema):
    id = fields.Int()
    deleted_by = fields.Int()


class AnomalyRouteCreateSchema(PlainAnomalyRouteSchema):
    id = fields.Int()
    anomaly_id = fields.Int()
    latitude = fields.Float()
    longitude = fields.Int()
    description = fields.Str()
    anomaly_at = fields.Int()
    anomaly_level = fields.Int()
