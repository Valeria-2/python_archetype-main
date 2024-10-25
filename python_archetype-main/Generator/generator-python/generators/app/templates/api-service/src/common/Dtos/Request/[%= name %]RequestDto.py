from marshmallow import Schema, fields

class [%= name %]RequestDto(Schema): 
    id = fields.Int(required=False)
    email = fields.Str(required=True)
    name = fields.Str(required=True)
    roleId = fields.Int(required=True)
    username = fields.Str(required=True)
    active = fields.Boolean(required=True)