from flask_marshmallow.fields import fields

from server.core import ma
from server.models import Login


class LoginSchema(ma.ModelSchema):
    class Meta:
        model = Login

    created_at = fields.DateTime('%Y-%m-%dT%H:%M:%S+09:00')
    updated_at = fields.DateTime('%Y-%m-%dT%H:%M:%S+09:00')


def to_json(self, schema=LoginSchema()):
    return schema.dump(self).data


setattr(Login, 'to_json', to_json)

