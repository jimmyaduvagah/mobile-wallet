"""Configuration module for currency app."""

from django.apps import AppConfig


class CurrencyConfig(AppConfig):
    """Configuration class for currency app."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mobile_wallet.currency'
