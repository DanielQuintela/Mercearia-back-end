from marshmallow import Schema, fields, validate

class CategoriesSchema(Schema):

    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    status = fields.Bool(load_default=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
