from marshmallow import Schema, fields, validate, INCLUDE


class LoginSchema(Schema):
    pasword = fields.String(required=True, data_key='auth_value')
    userName = fields.String(required=True, data_key='user_id')
