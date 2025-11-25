from marshmallow import Schema, fields, validate

class UsersSchema(Schema):

    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=120))
    email = fields.Email(required=True, validate=validate.Length(min=1, max=120))
    password = fields.Str(required=True, validate=validate.Length(min=1, max=60))
    role = fields.Str(required=True, validate=validate.OneOf(["admin", "user"]))
    status = fields.Bool(load_default=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class UserResponseSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    role = fields.Str()
    status = fields.Bool()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

