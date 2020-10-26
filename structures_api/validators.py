from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date, timedelta
import pytz


utc = pytz.UTC


def aup_validator_since(date_since):
    """
    Validator for AUP model.
    Args:
        date_since: date entered by user

    Returns: None or raises a ValidationError
    """
    if date_since > date.today() + timedelta(days=1):
        raise ValidationError(
            _(f"{date_since} is too far ahead! Create AUP for the next day only!")
        )
    if date_since <= date.today():
        raise ValidationError(
            _(f"{date_since} is too soon or in the past! Create AUP for the next day only!")
        )


def aup_validator_to(date_to):
    """
    Validator for AUP model.
    Args:
        date_to: date entered by user

    Returns: None or raises a ValidationError
    """
    if date_to > date.today() + timedelta(days=1):
        raise ValidationError(
            _(f"{date_to} is too far ahead! Prepare AUP with proper advance!")
        )
    if date_to <= date.today():
        raise ValidationError(
            _(f"{date_to} is too soon! Prepare AUP with proper advance!")
        )


def reservation_validator_since(reservation_since):
    """
    Validator for reservation model.
    Args:
        reservation_since: date entered by user

    Returns: None or raises a ValidationError
    """
    if reservation_since <= date.today():
        raise ValidationError(
            _(f"{reservation_since} too soon! Make reservation with proper advance!")
        )
    if reservation_since > date.today() + timedelta(days=1):
        raise ValidationError(
            _(f"{reservation_since} too long advance! Make reservation with proper advance!")
        )


def reservation_validator_to(reservation_to):
    """
    Validator for reservation model.
    Args:
        reservation_to: date entered by user

    Returns: None or raises a ValidationError
    """
    if reservation_to > date.today() + timedelta(days=1):
        raise ValidationError(
            _(f"{reservation_to} too late! Make reservation with proper advance!")
        )
    if reservation_to <= date.today():
        raise ValidationError(
            _(f"{reservation_to} too soon! Make reservation with proper advance!")
        )
