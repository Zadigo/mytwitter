from django.utils import timezone
from django.core.exceptions import ValidationError

def validate_scheduling_date(d):
    current_date = timezone.now()
    if d.date() < current_date.date():
        raise ValidationError('Scheduling date cannot be below current date')
    return d
