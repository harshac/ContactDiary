import re
from django.core.exceptions import ValidationError

def validate_string(name):
    if re.search('^[A-Za-z]+$', name) is None:
        raise ValidationError('Invalid First Name')


def validate_number(value):
    if re.search('^[0-9]+$', value) is None:
        raise ValidationError('Invalid Number')