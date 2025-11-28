from marshmallow import Schema, fields, validate

class PromotionSchema(Schema):

    id = fields.Str(dump_only=True)
    name = fields.Str(required=True,validate=validate.Length(min=1, max=50))
    status = fields.Bool(load_default=True)
    starts_at = fields.DateTime(required=True,format="%Y-%m-%dT%H:%M:%S")
    ends_at = fields.DateTime(allow_none=True,format="%Y-%m-%dT%H:%M:%S")
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
