from marshmallow import Schema, fields, validate, INCLUDE
from datetime import datetime


class UserSchema(Schema):
    name = fields.String(required=True, data_key='user_name')
    email = fields.Email(required=True, data_key='user_email')
    mobilenumber = fields.String(required=True, data_key='user_phone',
     validate=validate.Length(min=10, max=13))
    pasword = fields.String(required=True, data_key='auth_value')
    userName = fields.String(required=True, data_key='user_id')
    email_verified = fields.Bool(required=True, data_keys='email_verified')
    phone_verified = fields.Bool(required=True, data_keys='phone_verified')
    bank_verified = fields.Bool(required=True, data_keys='bank_verified')
    created_at = fields.DateTime(default=datetime.now())

    class Meta:
        unknown = INCLUDE
        # fields = ("user_name", "user_email", "user_phone", "email_verified", 
        # "phone_verified","bank_verified", "created_at" )
        # orderd = True
