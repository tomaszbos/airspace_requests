from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date, datetime, timedelta
import pytz


utc = pytz.UTC


def aup_validator_since(date_since):
    if date_since > date.today() + timedelta(days=1):
        raise ValidationError(
            _(f"{date_since} is too far ahead! Create AUP for the next day only!")
        )
    if date_since <= date.today():
        raise ValidationError(
            _(f"{date_since} is too soon or in the past! Create AUP for the next day only!")
        )


def aup_validator_to(date_to):
    if date_to > date.today() + timedelta(days=1):
        raise ValidationError(
            _(f"{date_to} is too far ahead! Prepare AUP with proper advance!")
        )
    if date_to <= date.today():
        raise ValidationError(
            _(f"{date_to} is too soon! Prepare AUP with proper advance!")
        )


def reservation_validator_since(reservation_since):
    if reservation_since <= utc.localize(datetime.today()):
        raise ValidationError(
            _(f"{reservation_since} too soon! Make reservation with proper advance!")
        )
    if reservation_since > utc.localize(datetime.today() + timedelta(days=1)):
        raise ValidationError(
            _(f"{reservation_since} too long advance! Make reservation with proper advance!")
        )


def reservation_validator_to(reservation_to):
    if reservation_to > utc.localize(datetime.today() + timedelta(days=1)):
        raise ValidationError(
            _(f"{reservation_to} too late! Make reservation with proper advance!")
        )
    if reservation_to <= utc.localize(datetime.today()):
        raise ValidationError(
            _(f"{reservation_to} too soon! Make reservation with proper advance!")
        )
