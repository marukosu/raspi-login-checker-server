from flask_marshmallow.fields import fields

from server.core import ma
from server.models import User


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

    created_at = fields.DateTime('%Y-%m-%dT%H:%M:%S+09:00')
    updated_at = fields.DateTime('%Y-%m-%dT%H:%M:%S+09:00')


def to_json(self, schema=UserSchema()):
    return schema.dump(self).data


setattr(User, 'to_json', to_json)
