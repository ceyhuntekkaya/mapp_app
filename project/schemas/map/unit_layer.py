from marshmallow import Schema, fields


class PlainUnitLayerSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    created_at = fields.Str()


class UnitLayerSchema(PlainUnitLayerSchema):
    updated_at = fields.Str()
    deleted_at = fields.Str()
    status = fields.Int()
    created_by = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class UnitLayerUpdateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    updated_by = fields.Int()


class UnitLayerDeleteSchema(PlainUnitLayerSchema):
    id = fields.Int()
    deleted_by = fields.Int()


class UnitLayerCreateSchema(PlainUnitLayerSchema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    created_by = fields.Int()