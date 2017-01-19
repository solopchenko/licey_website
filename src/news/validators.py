from django.core.exceptions import ValidationError
from app.utils import get_now

def no_future_date(date):
    if date > get_now():
        raise ValidationError("Дата не может быть больше текущей")
    return date