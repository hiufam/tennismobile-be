from marshmallow import fields, Schema, validates, ValidationError

from api.database import session
from api.models.user import User

class PhoneNumberSchema(Schema):
    phone_number = fields.Integer()
        
    @validates('phone_number')
    def validate_phone_number(self, phone_number):
        if not phone_number:
            raise ValidationError('No phone number provided')

        if session.query(User).filter(User.phone_number == phone_number).scalar() is not None:
            raise ValidationError('Phone number has already been registered') 
        
        if not str(phone_number).isdigit():
            raise ValidationError('Phone number contains character')

        if len(str(phone_number)) != 10:
            raise ValidationError('Phone number requires 10 digits') 
        
        return phone_number