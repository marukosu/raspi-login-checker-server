from flask_marshmallow.fields import fields

from server.core import ma
from server.models import Card


class CardSchema(ma.ModelSchema):
    class Meta:
        model = Card

    created_at = fields.DateTime('%Y-%m-%dT%H:%M:%S+09:00')
    updated_at = fields.DateTime('%Y-%m-%dT%H:%M:%S+09:00')


def to_json(self, schema=CardSchema()):
    return schema.dump(self).data


setattr(Card, 'to_json', to_json)
