"""module for currency app models."""

import os
import coinoxr
from django.db import models

from mobile_wallet.common.models import AbstractBase


CURRENCY_CONVERSION_API_KEY = os.getenv('OPENEXCHANGERATEAPI', None)


class Currency(AbstractBase):
    """Model to hold currencies and codes."""

    country = models.CharField(max_length=100)
    currency_iso_code = models.CharField(max_length=5, unique=True)
    currency_name = models.CharField(max_length=100, null=True, blank=True)
    conversion_rate = models.DecimalField(
        max_digits=16, decimal_places=4, null=True, blank=True)


def get_user_currency_rate(currency):
    """Call the  open exchange currency API."""
    coinoxr.app_id = CURRENCY_CONVERSION_API_KEY
    rates = coinoxr.Latest().get(base="USD")
    rates = rates.body['rates']
    return rates.get(currency.currency_iso_code, 0)


def get_usd_amount(rate, amount):
    """Convert the users' currency  to USD."""
    return round(amount / rate, 2)
