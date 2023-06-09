from marshmallow import Schema, fields


class PlainRoleSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    active = fields.Bool(required=False, default=True)


class RoleSchema(PlainRoleSchema):
    create_at = fields.Int(required=True)
    update_at = fields.Int(required=False)
    delete_at = fields.Int(required=False)
    create_by = fields.Int(required=False)
    update_by = fields.Int(required=False)
    delete_by = fields.Int(required=False)


