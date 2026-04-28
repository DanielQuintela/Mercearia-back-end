from marshmallow import Schema, fields, validate

class ProductSchema(Schema):

    id = fields.Str(dump_only=True)
    categories_id = fields.Str(required=True, validate=validate.Length(min=1))
    producer_id = fields.Str(required=True, validate=validate.Length(min=1))
    name = fields.Str(required=True, validate=validate.Length(min=1, max=120))
    barcode = fields.Str(required=True, validate=validate.Length(min=8, max=13))
    measure = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    weight = fields.Float(validate=validate.Range(min=0))
    length = fields.Float(validate=validate.Range(min=0))
    image = fields.Str(validate=validate.Length(max=255))
    status = fields.Bool(load_default=True)
    price = fields.Decimal(as_string=True, validate=validate.Range(min=0))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
